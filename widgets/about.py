from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint

class About(QDialog):
    def __init__(self):
        super(About, self).__init__()
        self.layout = QVBoxLayout()
        
        self.setWindowTitle("About")
        self.setMinimumSize(500,300)

        self.setStyleSheet("""
        QLabel {
            background-color: #282a36;
            font-size: 20px;
        }
        
        QPushButton {
            color: #f8f8f2;
            border: 1px solid transparent;
            border-radius: 5px;
            font-size: 30px;
            font: bold;
        }

        QPushButton:hover {
            color: #f8f8f2;
            background: #ff5555;
            border: 1px solid  #ff5555;
        }
        
        """)

        self.layout = QVBoxLayout()
        self.btnclose = QPushButton("Close")
        self.btnclose.clicked.connect(self.accept)
        self.btnclose.setFixedWidth(100)
        message = QLabel("A Simple Markdown editor by : DarkMatter999")
        message.setAlignment(Qt.AlignCenter)
        message.setFixedHeight(50)
        message2 = QLabel("")
        message2.setOpenExternalLinks(True)
        message2.setText("Github: https://github.com/DarkMatter-999")
        message2.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(message)
        self.layout.addWidget(message2)
        self.layout.addWidget(self.btnclose, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
