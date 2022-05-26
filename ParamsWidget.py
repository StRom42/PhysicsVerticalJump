# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets, QtCore
from params_ui import Ui_ParamsUi

class ParamsWidget(QtWidgets.QWidget):
    calc_signal = QtCore.Signal()
    def __init__(self):
        super(ParamsWidget, self).__init__()

        self.ui = Ui_ParamsUi()
        self.ui.setupUi(self)

        self.ui.calc_button.clicked.connect(self.start_calculations)

    def start_calculations(self):
        print("calculations started")
        self.calc_signal.emit()
        
    def get_data(self):
        data = {
            "mass": int(self.ui.mass_input.text()),
            "height": int(self.ui.height_input.text())
        }
        
        return data
