# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
# from matplotlib.backends.backend_qt5agg import \
#     NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pandas as pd

matplotlib.use('Qt5Agg')


class Mpl_Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=100):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Mpl_Canvas, self).__init__(fig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 614)
        self.initialWidget = QtWidgets.QWidget(MainWindow)
        self.initialWidget.setObjectName("initialWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.initialWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 190, 761, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mpl_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mpl_layout.setContentsMargins(0, 0, 0, 0)
        self.mpl_layout.setObjectName("mpl_layout")
        self.canvas = Mpl_Canvas(self, dpi=100)
        self.mpl_layout.addWidget(self.canvas)
        self.widget = QtWidgets.QWidget(self.initialWidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 761, 151))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.func2 = QtWidgets.QRadioButton(self.widget)
        self.func2.setObjectName("func2")
        self.gridLayout.addWidget(
            self.func2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.func2label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.func2label.setFont(font)
        self.func2label.setObjectName("func2label")
        self.gridLayout.addWidget(
            self.func2label, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.calcular = QtWidgets.QPushButton(self.widget)
        self.calcular.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.calcular.setAutoDefault(False)
        self.calcular.setFlat(True)
        self.calcular.setObjectName("calcular")
        self.calcular.clicked.connect(self.selected_function)
        self.gridLayout.addWidget(self.calcular, 2, 1, 1, 1)
        self.func1label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.func1label.setFont(font)
        self.func1label.setObjectName("func1label")
        self.gridLayout.addWidget(
            self.func1label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.func3 = QtWidgets.QRadioButton(self.widget)
        self.func3.setObjectName("func3")
        self.gridLayout.addWidget(
            self.func3, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.func3label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.func3label.setFont(font)
        self.func3label.setObjectName("func3label")
        self.gridLayout.addWidget(
            self.func3label, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.func1 = QtWidgets.QRadioButton(self.widget)
        self.func1.setStyleSheet("padding: 20px;")
        self.func1.setChecked(True)
        self.func1.setObjectName("func1")
        self.gridLayout.addWidget(
            self.func1, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.resultado = QtWidgets.QLabel(self.widget)
        self.resultado.setText("")
        self.resultado.setObjectName("resultado")
        self.gridLayout.addWidget(
            self.resultado, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.cantidad = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cantidad.sizePolicy().hasHeightForWidth())
        self.cantidad.setSizePolicy(sizePolicy)
        self.cantidad.setObjectName("cantidad")
        self.cantidad.setAlignment(QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(
            self.cantidad, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.initialWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def make_plot(self, function, n=100):
        X = np.linspace(0.5, 5.5, 1000)
        r, x, y, c = self.integral_montecarlo(0.5, 5.5, function, n)
        df = pd.DataFrame()
        df['x'] = x
        df['y'] = y
        df['c'] = c
        self.canvas.axes.plot(X, function(X))
        self.canvas.axes.set_xticks(np.arange(0.5, 5.5+1, 0.5))
        self.canvas.axes.scatter(df[df['c'] == 0]['x'],
                                 df[df['c'] == 0]['y'], color='red')
        self.canvas.axes.scatter(df[df['c'] == 1]['x'],
                                 df[df['c'] == 1]['y'], color='green')
        return r

    def plot_montecarlo(self, function):
        self.canvas.axes.cla()
        r = self.make_plot(function, int(self.cantidad.text()))
        self.canvas.draw()
        self.resultado.setText(str(round(r, 4)))
        return

    def selected_function(self):
        if self.func1.isChecked():
            self.plot_montecarlo(self.function1)
            return

        if self.func2.isChecked():
            self.plot_montecarlo(self.function2)
            return

        if self.func3.isChecked():
            self.plot_montecarlo(self.function3)
            return

    def function1(self, x):
        # R=100.417
        return((x**2)+(2*x)+3)

    def function2(self, x):
        # R=732.031
        return((1/2)*(x**3)*(x+2))

    def function3(self, x):
        # R=0.809833
        return 1/((x**(1/3))+(x**2)*(x**(1/2)))

    def integral_montecarlo(self, x1, x2, func, n=100000):
        X = np.linspace(x1, x2, 1000)
        y1 = 0
        y2 = max(func(X))+1
        area = (x2-x1)*(y2-y1)
        check = []
        xs = []
        ys = []
        for i in range(n):
            x = np.random.uniform(x1, x2, 1)
            xs.append(x)
            y = np.random.uniform(y1, y2, 1)
            ys.append(y)
            if abs(y) > abs(func(x)) or y < 0:
                check.append(0)
            else:
                check.append(1)
        return(np.mean(check)*area, xs, ys, check)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Simulación Montecarlo | Área bajo la curva"))
        self.func2.setText(_translate("MainWindow", "Función #2"))
        self.func2label.setText(_translate("MainWindow", "(½x³)(x+2)"))
        self.calcular.setText(_translate("MainWindow", "Calcular"))
        self.func1label.setText(_translate("MainWindow", "x²+2x+3"))
        self.func3.setText(_translate("MainWindow", "Función #3"))
        self.func3label.setText(_translate("MainWindow", "1/(∛x+(x²)(√x))"))
        self.func1.setText(_translate("MainWindow", "Función #1"))
        self.cantidad.setText(_translate("MainWindow", "100"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
