from PyQt4.QtGui import *
from PyQt4 import QtCore
import sys

class Communicate(QtCore.QObject):
    closeApp = QtCore.pyqtSignal()


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(QtCore.Qt.Horizontal, self)
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('signal & slot')

        btn1 = QPushButton('button 1', self)
        btn2 = QPushButton('button 2', self)
        btn2.move(150, 100)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        print sender

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, e):
        self.c.closeApp.emit()

def main():
    app = QApplication(sys.argv)
    test = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()