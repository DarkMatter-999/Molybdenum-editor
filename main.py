import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mm = QMainWindow()
    mm.show()
    sys.exit(app.exec_())