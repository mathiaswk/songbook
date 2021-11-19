"""
    songbook.gui
    ~~~~~~~~~~~~

    A one line summary of the module or program, terminated by a period.

    :copyright: Copyright 2007-2021 by the Sphinx team, see AUTHORS.
    :license: MIT, see LICENSE for details.
"""

import sys
from PySide6.QtCore import Qt, QCoreApplication, QEventLoop, QTimer, Slot
from PySide6.QtWidgets import QApplication, QLabel, QWizard, QWizardPage, QCheckBox, QVBoxLayout, QProgressBar

from songbook.core import Songbook


class SongbookGui(QWizard):
    """

    """

    def __init__(self, songbook=None):
        """Creates a `SongbookGui`.

        Args:
            songbook:
        """
        super(SongbookWizard, self).__init__(parent)

        self.addPage(IntroductionPage(self.songbook))
        self.addPage(SongSelectionPage(self.songbook))
        self.addPage(FormPage(self.songbook))
        self.addPage(PerformCompilationPage(self.songbook))
        self.addPage(FinishedPage(self.songbook))

        self.setWindowTitle("PyQt5 Wizard Example - pythonspot.com")
        self.setWizardStyle(QWizard.WizardStyle.ModernStyle)
        self.resize(800, 600)

    def run(self):



class IntroductionPage(QWizardPage):
    def __init__(self, songbook):
        self.setObjectName("IntroductionPage")
        # self.setColoredTitle()

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        msgLabel = QLabel(self)
        msgLabel.setWordWrap(True)
        msgLabel.setObjectName("MessageLabel")
        msgLabel.setText("Welcome to the Songbook Setup Wizard.")

        widget = QWidget(self)
        boxLayout = QVBoxLayout(widget)




class SongSelectionPage(QWizardPage):
    pass


class FormPage(QWizardPage):
    def __init__(self, songbook=None):
        setPixmap

        self.setCommitPage(True)


class PerformCompilationPage(QWizardPage):
    def __init__(self, songbook=None):
        self.progressBar = QProgressBar(self)
        self.progressBar.setObjectName("ProgressBar")

        layout = QVBoxLayout(self)
        layout.addWidget(self.progressBar)
        self.setLayout(layout)

        self.setCommitPage(True)

    def entering(self):
        """Initializes the page."""
        QTimer.singleShot(0, self.start)

    def start(self):
        sb = Songbook()
        sb.build(progress_update=self.progressBar.setValue, progress_total=self.progressBar.setMaximum)


class FinishedPage(QWizardPage):
    def __init__(self, parent=None):
        super(FinishedPage, self).__init__(parent)

        self.setObjectName("FinishedPage")
        # self.setColoredTitle("Completing the Songbook Wizard")
        # self.setPageListTitle("Finished")

        self.msgLabel = QLabel(self)
        self.msgLabel.setWordWrap(True)
        self.msgLabel.setObjectName("MessageLabel")

        self.runItCheckBox = QCheckBox(self)
        self.runItCheckBox.setObjectName("RunItCheckBox")
        self.runItCheckBox.setChecked(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.msgLabel)
        layout.addWidget(self.runItCheckBox)
        self.setLayout(layout)

        self.setCommitPage(True)

    def initializePage(self):
        self.msgLabel.setText("Click Finish to exit the Songbook Wizard.")
        self.runItCheckBox.setText("Run songbook now.")


def run_gui():
    app = QApplication(sys.argv)
    wizard = SongbookWizard()
    wizard.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
