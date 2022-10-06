
from PyQt5 import QtWidgets

from demo1_controller import Ui_Form_controller

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Form_controller()
    window.show()
    sys.exit(app.exec_())

