from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint

class TitleBar(QWidget):
    def __init__(self, parent):
        super(TitleBar, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        
        self.buttonh = 30
        self.buttonw = 40

        self.title = QLabel("~File Name~")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setObjectName("titletext")

        self.btnminimize = QPushButton("-")
        self.btnminimize.clicked.connect(self.minimize)
        self.btnminimize.setFixedSize(self.buttonw, self.buttonh)

        self.btnmaximize = QPushButton("=")
        self.btnmaximize.clicked.connect(self.maximize)
        self.btnmaximize.setFixedSize(self.buttonw, self.buttonh)
        self.ismaximised = False

        self.btnclose = QPushButton("x")
        self.btnclose.clicked.connect(self.close)
        self.btnclose.setFixedSize(self.buttonw, self.buttonh)

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btnminimize)
        self.layout.addWidget(self.btnmaximize)
        self.layout.addWidget(self.btnclose)
        

        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def minimize(self):
        self.parent.showMinimized()

    def maximize(self):
        if self.ismaximised:
            self.parent.showNormal()
            self.ismaximised = False
        else:
            self.parent.showMaximized()
            self.ismaximised = True
        
    def close(self):
        self.parent.close()

    # Resize and Move window
    def resizeEvent(self, QResizeEvent):
        super(TitleBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False
