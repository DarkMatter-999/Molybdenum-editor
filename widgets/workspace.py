from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint

from widgets.sidebar import SideBar

class Workspace(QWidget):
    def __init__(self, parent):
        super(Workspace, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(5)

        self.editor = QTextEdit()
        self.preview = QTextEdit()
        self.sidebar = SideBar(self)
        # self.preview.setDisabled(True)
        self.editor.textChanged.connect(self.set_mdText)
        
        self.layout.addWidget(self.sidebar)
        self.layout.addWidget(self.editor)
        self.layout.addWidget(self.preview)


        self.setLayout(self.layout)

    def set_mdText(self):
        self.preview.setMarkdown(self.editor.toPlainText())
