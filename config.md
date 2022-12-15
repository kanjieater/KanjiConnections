## Important Information
This addon requires **TWO** separate decks to work.   
The deck you're reviewing (which contains your sentence cards) and a Deck that will be the source for your RTK Keywords. By default we are using the [Japanese Heisigs RTK all-in-one](https://ankiweb.net/shared/info/1532278975) shared deck available in ankiweb. 

It also needs the [Japanese Support](https://ankiweb.net/shared/info/3918629684) [`3918629684`] addon to extract the kanji from your sentences.

Additionally, if you would like for Vocab to be included alongside your keywords, you also need to install [KanjiVocab](https://github.com/HelenFoster/KanjiVocab) [`1600796261`], otherwise it will display only the Kanji and its English keyword (with a link to the dictionary configured here).

Please consult the readme for detailed instructions on how to set everything up.
****
### These are the settings you can customize:
*Most of these settings work without needing to restart Anki, but if you changed a setting and something isn't working as intended, restart Anki before continuing.*  

**"destination":**  This is the Field where the addon will write the Keywords in your review deck.

**"override":**  If this variable is set to `false` it will *not*  update cards if the destination field is not empty. Set to `true` if you want to replace the existing contents of that field. **USE WITH CAUTION!**

**"source":**  These are the Fields in your review/sentence deck that have kanji (eg. in sentences) and that you would like to generate keywords from, multiple fields can be added, separated by a comma, but with no comma after the last entry. 

If you have a `"Vocab"` field with 其の and an `"Expression"` field with その本は面白い, the output in the Keywords field will include 其,本,面,白 - combining the two (or more) fields. If you only have one field you would like to generate from, you can just erase the other one.

**"generateKanjiCards":**  If you try to generate keywords for a Kanji that is *not*  currently in your source RTK Deck, this Add-on can create a card on it with that Kanji. Set to `true`  to enable, or `false`  if you don't want new cards to be generated.

**"rtkDeck":**  This is the exact name of your RTK Deck where your Kanji cards are. This is the Deck from which Kanji keywords will be referenced from, and also where cards will be generated to if `"generateKanjiCards"`  is set to `true`. Make sure you're copying it exactly.

**"rtkModel":**  This is the exact name of the Note type of your RTK Deck. This is where Kanji keywords will be referenced from, and also where cards will be generated to if `"generateKanjiCards"`  is set to `true`. Make sure you're copying it exactly.

**"kanjiUrl":**  This is the online dictionary that your keywords will link to. By the default, it links to http://kanji.koohii.com/study/kanji/, but you can change it to https://jisho.org/search/ or your preferred dictionary here.

**"rtkKanjiField":**  This is the name of the field in your RTK Deck where the Kanji (a single Kanji) is located.

**"rtkKeywordField":**  This is the name of the field in your RTK Deck where the English keyword for the Kanji is located (they'll display next to the kanji).

**"vocabField":**  This the field where the KanjiVocab add-on has already generated Vocab to, **This field must be added to your RTK Deck even if you're not using KanjiVocab.**

**"vocabUrl":**  If you used KanjiVocab, this is where all the vocab words in your Destination field will link to (in a single link). Eg. If the Vocab is x漢字 and 練習 it will link to "https://jisho.org/search/漢字%20練習", the vocab is always appended at the end of the link. By the default, it links to the Kanji [keyword] first, and then to the Vocab. Keyword and Vocab may have their own dictionary link.

**"rtkKeywordDict":**  Not currently implemented, do ignore this field.

**"separator":**  Change the separator between the keyword and the vocab (eg.a dash or whatever symbol/spaces you want, " - " would make it output as 全 - 全体) - If you don't want a separator at all (eg. if you'd prefer to manually style margins from the css instead of using a space), leave it as "".  


****
### Advanced CSS Styling:
Each Keyword and its accompanying vocab are outputted to their own paragraph `<p>` using a `"kw"` class that can be styled from your Card Template CSS.

Keywords use the `"keyword"` class, and Vocab uses the `"keyword-vocab"` class, so each can be styled separately to match your visual preferences.

The separator uses the `"kw-separator"` class.

Visual settings for KanjiVocab and customizations according to card maturity are also customizable through CSS from your card template.  
For more in-depth help, please consult the Readme.