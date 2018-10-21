import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.label = QLabel(king, self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("QLabel {background-color: black;color: rgb(32, 192, 14);}")

        self.label2 = QLabel("Label2", self)
        self.label2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("QLabel {background-color: black;color: rgb(32, 192, 14);}")


        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.label2, 1, 2)

        self.setLayout(self.layout)
        self.showFullScreen()
        #self.show()


var1= "TEST"
var2 = "TEST2"

king = var1 + " Is the master of the domain"
app = QApplication(sys.argv)
win = Window()


sys.exit(app.exec_())