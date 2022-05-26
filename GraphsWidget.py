# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets, QtCharts, QtGui, QtCore


class GraphsWidget(QtWidgets.QWidget):
    def __init__(self, rows, columns):
        super(GraphsWidget, self).__init__()

        self.graphGrid = QtWidgets.QGridLayout()
        self.charts = {}
        self.rows = rows
        self.columns = columns
        self.setLayout(self.graphGrid)

    def init_chart(self, chart_title):
        chart_view = QtCharts.QChartView()
        chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        chart_view.chart().legend().setVisible(False)
        chart_view.chart().setTitle(chart_title)
        chart_view.chart().setAnimationOptions(QtCharts.QChart.AllAnimations)
        return chart_view

    def add_graph(self, graph_name, X_list, Y_list):
        self.charts[graph_name] = self.init_chart(graph_name)
        current_index = list(self.charts.keys()).index(graph_name)
        current_row = current_index // self.rows
        current_column = current_index % self.columns
        self.graphGrid.addWidget(self.charts[graph_name], current_row, current_column)
        
        series = QtCharts.QLineSeries()
        for x, y in zip(X_list, Y_list):
            series.append(x, y)
        self.charts[graph_name].chart().addSeries(series)
        
        x_axis, y_axis = QtCharts.QValueAxis(), QtCharts.QValueAxis()
        x_axis.setTitleText("Time, sec")
        y_axis.setTitleText(graph_name)
        self.charts[graph_name].chart().createDefaultAxes()
        self.charts[graph_name].chart().setAxisX(x_axis, series)
        self.charts[graph_name].chart().setAxisY(y_axis, series)
        
