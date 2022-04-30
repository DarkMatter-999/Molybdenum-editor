from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint
import os

class SideBar(QWidget):
    def __init__(self, parent):
        super(SideBar, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(10)

        self.buttonh = 30
        self.buttonw = 40

        self.path = None

        self.btnnew = QPushButton("N")
        self.btnnew.clicked.connect(self.file_new)
        self.btnnew.setFixedSize(self.buttonw, self.buttonh)

        self.btnopen = QPushButton("O")
        self.btnopen.clicked.connect(self.file_open)
        self.btnopen.setFixedSize(self.buttonw, self.buttonh)

        self.btnsave = QPushButton("S")
        self.btnsave.clicked.connect(self.file_save)
        self.btnsave.setFixedSize(self.buttonw, self.buttonh)

        self.btnsaveas = QPushButton("Sa")
        self.btnsaveas.clicked.connect(self.file_saveas)
        self.btnsaveas.setFixedSize(self.buttonw, self.buttonh)

        self.btnabout = QPushButton("A")
        self.btnabout.setFixedSize(self.buttonw, self.buttonh)

        self.spacer = QSpacerItem(30, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout.addWidget(self.btnnew)
        self.layout.addWidget(self.btnopen)
        self.layout.addWidget(self.btnsave)
        self.layout.addWidget(self.btnsaveas)
        self.layout.addItem(self.spacer)
        self.layout.addWidget(self.btnabout)

        self.setLayout(self.layout)

    def file_new(self):
        self.parent.editor.setText("")
        self.parent.parent.titlebar.updatetitle("Untitled")

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.md );; All files (*.*)")
        if path:
            # try opening path
            try:
                with open(path, 'rU') as f:
                    text = f.read()
 
            except Exception as e:
                # show error using critical method
                self.dialog_critical(str(e))
            else:
                self.path = path

                # update the textedit
                self.parent.editor.setPlainText(text)
                self.parent.parent.titlebar.updatetitle(os.path.basename(self.path) if self.path else "Untitled")

    def file_save(self):
 
        if self.path is None:
 
            return self.file_saveas()
        self._save_to_path(self.path)
 
    def file_saveas(self):

        path, _ = QFileDialog.getSaveFileName(self, "Save file", "",
                             "Text documents (*.md );; All files (*.*)")

        if not path:
            return
 
        self._save_to_path(path)
 
    def _save_to_path(self, path):
 
        text = self.parent.editor.toPlainText()

        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))
        else:
            self.path = path
            self.parent.parent.titlebar.updatetitle(os.path.basename(self.path) if self.path else "Untitled")