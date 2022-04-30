from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint

from widgets.sidebar import SideBar

class Workspace(QWidget):
    def __init__(self, parent):
        super(Workspace, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(1)

        self.editor = QPlainTextEdit()
        
        self.layout.addWidget(SideBar(self))
        self.layout.addWidget(self.editor)
        self.layout.addWidget(QPlainTextEdit())


        self.setLayout(self.layout)