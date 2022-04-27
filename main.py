import sys
from PyQt5.QtWidgets import *
from widgets.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open('./widgets/styles.css').read())
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())