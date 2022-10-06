
from PyQt5 import QtWidgets, QtGui, QtCore

from demo1_UI import Ui_Form

class Ui_Form_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.ui.pushButton.clicked.connect(self.hello_world)

    def hello_world(self):
        print("Hello world!")
