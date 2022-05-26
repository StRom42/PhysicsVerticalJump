from PySide6 import QtWidgets, QtGui
from ParamsWidget import ParamsWidget
from GraphsWidget import GraphsWidget
from Calculator import JumpCalculator

class MainWindow (QtWidgets.QWidget):
    def __init__(self, ):
        super(MainWindow, self).__init__()
        self.params_widget = ParamsWidget()
        self.graphs_widget = GraphsWidget(rows = 2, columns =2)
        self.time_label = QtWidgets.QLabel()
        self.time_label.setFont(QtGui.QFont("Arial", 20))
        self.time_label.setWordWrap(True)
        
        self.layout = QtWidgets.QGridLayout()
        
        self.layout.addWidget(self.params_widget, 0, 0, 1, 1)
        self.layout.addWidget(self.graphs_widget, 0, 1, 2, 4)
        self.layout.addWidget(self.time_label, 1, 0, 1, 1)
        
        self.setLayout(self.layout)
        
        self.params_widget.calc_signal.connect(self.start_calculations)
    
    def start_calculations(self):
        data = self.params_widget.get_data()
        jump_calculator = JumpCalculator(mass=data["mass"],
                                         height=data["height"])
        data_trace, time_in_air = jump_calculator.calc_jump_characteristics(duration=10,
                                                  time_step=1e-2)
        
        measure_units = {
            "velocity": "meters per sec",
            "height": "meters",
            "RFD": "Neutons",
            "RPD": "Watts"
        }
        
        for key in data_trace.keys():
            if key != "time":
                self.graphs_widget.add_graph(f"{key}, {measure_units[key]}", data_trace["time"], data_trace[key])
        self.time_label.setText(f"Время в воздухе составило {round(time_in_air, 2)} секунд")
        
        