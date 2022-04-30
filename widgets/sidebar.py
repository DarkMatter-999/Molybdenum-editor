from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint

class SideBar(QWidget):
    def __init__(self, parent):
        super(SideBar, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(1)

        self.buttonh = 30
        self.buttonw = 40

        self.btnminimize = QPushButton("-")
        self.btnminimize.setFixedSize(self.buttonw, self.buttonh)

        self.btnmaximize = QPushButton("=")
        self.btnmaximize.setFixedSize(self.buttonw, self.buttonh)

        self.btnclose = QPushButton("x")
        self.btnclose.setFixedSize(self.buttonw, self.buttonh)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout.addWidget(self.btnminimize)
        self.layout.addWidget(self.btnmaximize)
        self.layout.addWidget(self.btnclose)
        self.layout.addItem(self.spacer)

        self.setLayout(self.layout)
        