
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QAction

from aqt import mw
from anki.decks import DeckManager
from anki.notes import Note
from aqt.utils import showInfo
from anki.utils import stripHTML
import re 


CONFIG = mw.addonManager.getConfig(__name__)

srcFields = CONFIG['source']
dstField = CONFIG['destination']
rtkModel = CONFIG['rtkModel']
rtkKanjiField = CONFIG['rtkKanjiField']
rtkKeywordField = CONFIG['rtkKeywordField']
rtkKeywordDict = CONFIG['rtkKeywordDict']
vocabField = CONFIG['vocabField']
vocabUrl= CONFIG['vocabUrl']
kanjiUrl = CONFIG['kanjiUrl']
rtkDeck = CONFIG['rtkDeck']
OVERRIDE = CONFIG['override'] 


def getMessage(note):
    kanji = note[rtkKanjiField]
    keyword = note[rtkKeywordField]
    message = "<a title='{}' href='{}{}'>{} - {}</a><br>".format(keyword, kanjiUrl, kanji, kanji, keyword)
    if note[vocabField]:
        search_string = re.sub("\[.*?\]", '', stripHTML(note[vocabField]))
        furikw = ''
        if keyword:
            furikw = f'[{keyword}]'
        message = f"<a class='keyword' href='{vocabUrl}{search_string}'>{kanji}{furikw}  - </a><a class='keyword-vocab' href='{vocabUrl}{search_string}'> {note[vocabField]}</a><br>"
    return message, kanji

def generateCache(cache):
    try:
        model = mw.col.models.byName(rtkModel)
    except Exception as e:
        showInfo('Failed to generate cache, does your model exist?')
        raise e
    mf = "mid:" + str(model['id'])
    ids = mw.col.findNotes(mf)
    for id in ids:
        note = mw.col.getNote(id)
        (message, kanji) = getMessage(note)
        if kanji in cache:
            cache[kanji] += message
        else:
            cache[kanji]  = message
    return cache

def getKanjiFromText(text):
    regex = u'[\u4E00-\u9FFF]' # == u'[一-龠々]+'
    match = re.findall(regex, text)
    # showInfo(str(match.group())+'1')
    # showInfo(text+'2')
    return match
    

def getKeywordsFast(expression, cache):
    kw = ""
    notFound = set()
    kanjis = getKanjiFromText(expression)
    # showInfo(str(kanjis) +'3')
    for e in kanjis:
        # showInfo(e)
        # showInfo(cache['毛'])
        # showInfo(str(e in cache))

        if e in cache:
            # showInfo(cache[e])
            if cache[e] not in kw:
                kw += cache[e]
        else:
            notFound.add(e)
    return kw, notFound

def getKeyword(nids):
    try:
        defGen = __import__('1655992655')
    except:
        return None
        # raise Exception('Failed to import migaku module')
    DESIRED_DICT = keywordDictionary
    dictDict = {}
    tempdicts = []
    for d in mw.miDictDB.getAllDicts():
        dictName = mw.miDictDB.cleanDictName(d)
        dictDict[dictName] = d
        tempdicts.append(dictName)
    #|159name新明解国語辞典第五版v3
    cleanName =mw.miDictDB.cleanDictName(DESIRED_DICT)
    #og, dest, addType, dictNs, howMany, notes, generateWidget, rawNames
    defGen.main.exportDefinitions(rtkKanjiField, rtkKeywordField, 'If Empty', [dictDict[cleanName]], 1, nids, None, [cleanName])
    return None

def setKanjiVocab():
    return None

def makeCards(kanjiSet):
    model = mw.col.models.byName(rtkModel)
    notes = []
    for kanji in kanjiSet:
        note = Note(mw.col, model)
        note[rtkKanjiField] = kanji
        # note[rtkKeywordField] = getKeyword()
        # setKanjiVocab()
        mw.col.addNote(note)
        note.addTag('autoKanji')
        cids = [c.id for c in note.cards()]
        dm = DeckManager(mw.col)
        deckId = mw.col.decks.id(rtkDeck)
        dm.setDeck(cids, deckId)

        note.flush()
        notes.append(note)
    # getKeyword([n.id for n in notes])
    return notes

        


def regenerateKeywords(nids):
    cache = generateCache({})
    
    notFound = set()
    mw.checkpoint("Bulk-add RTK Keywords")
    mw.progress.start()
    for nid in nids:
        note = mw.col.getNote(nid)
        if note[dstField] and not OVERRIDE:
            # already contains data, skip
            continue
        combinedSrc = ''
        for srcField in srcFields:
            # src = None
            # showInfo(srcField)
            # for fld in srcField:
            #     if fld in note:
            #         src = fld
            #         break
                
            # if not src:
            #     # no src field
            #     continue
            # dst = None
            # for fld in dstFields:
            #     if fld in note:
            #         dst = fld
            #         break
            # if not dst:
            #     # no dst field
            #     continue

            srcTxt = mw.col.media.strip(note[srcField])
            if not srcTxt.strip():
                continue
            combinedSrc += srcTxt 
        # try:
        note[dstField], needsCards = getKeywordsFast(combinedSrc, cache)
        # showInfo(note[dstField]+'1')
        note.flush()

        # showInfo(note[dstField])
        if needsCards and CONFIG['generateKanjiCards']:
            # showInfo(needsCards+'2')
            notes = makeCards(needsCards)
            for n in notes:
                (message, kanji) = getMessage(n)
                cache[kanji]  = message
                note[dstField] = getKeywordsFast(combinedSrc, cache)
                # note.flush()
            # except Exception as e:
            #     raise
    mw.progress.finish()
    mw.reset()

def onRegenerate(browser):
    regenerateKeywords(browser.selectedNotes())

    


