from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint
from widgets.titlebar import TitleBar
from widgets.workspace import Workspace

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.layout = QVBoxLayout()
        # Add Widgets here
        self.titlebar = TitleBar(self)
        self.workspace = Workspace(self)

        self.workspace.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        self.layout.addWidget(self.titlebar)
        self.layout.addWidget(self.workspace)


        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.setMinimumSize(800,500)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.gripSize = 8
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)
      

    def resizeEvent(self, QResizeEvent):
        super(MainWindow, self).resizeEvent(QResizeEvent)
        rect = self.rect()
        # top right
        self.grips[1].move(rect.right() - self.gripSize, 0)
        # bottom right
        self.grips[2].move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        # bottom left
        self.grips[3].move(0, rect.bottom() - self.gripSize)