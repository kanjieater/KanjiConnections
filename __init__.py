#
# Copyright: Robert Polz <robert.polz.cz@gmail.com>
# Batch-mode optimized by Vempele
# Maintained by KanjiEater
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
#
# Automatic RTK keyword generation.
#
from . import rtkkw
from anki.hooks import addHook
from PyQt6.QtGui import QAction

def start(browser):
    from importlib import reload
    from . import rtkkw
    reload(rtkkw)
    rtkkw.onRegenerate(browser)

def setupMenu(browser):

    a = QAction("Bulk-add Kanji Connections", browser)
    a.triggered.connect(lambda: start(browser))
    browser.form.menuEdit.addSeparator()
    browser.form.menuEdit.addAction(a)
    browser.form.menuEdit.addSeparator()
# addHook('editFocusLost', onFocusLost) #sometimes it adds EEEEEEEEVerything
addHook("browser.setupMenus", setupMenu)

