from PyQt5.QtWidgets import *
from PyQt5 import uic
import pandas as pd
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure


class miEditor(QMainWindow):
    
    

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('graficos.ui',self)
        self.show()
        self.setWindowTitle("Gráficos")
        self.actionCargar_datos.triggered.connect(lambda: self.Cargar())
        self.comboGraf.activated.connect(lambda: self.tGraf("line"))
        self.graficar.clicked.connect(lambda: self.dibujo(X=self.comboX.currentText(),
        Y=self.Serie.currentText()))


    def tGraf(self,tipo):
        tipoGraf = tipo
        print(tipoGraf)

    def dibujo(self,X,Y):
        archivo = self.label_4.text()
        tipoArch = archivo[-3:]
        self.label_4.setText(archivo)
        if tipoArch == "csv":
            data = pd.read_csv(archivo)
            
        elif (tipoArch == "xls" or tipoArch == "lsx"):
            data = pd.read_excel(archivo)
            
        elif tipoArch == "tml":
            data = pd.read_html(archivo)
            
        self.otraClase.canvas.axes.clear()
        
        self.otraClase.canvas.axes.plot(data[X], data[Y])
        self.otraClase.canvas.draw()

        
    def Cargar(self):
        options = QFileDialog().Options()
        archivo , _= QFileDialog().getOpenFileName()
        tipoArch = archivo[-3:]
        self.label_4.setText(archivo)

        if tipoArch == "csv":
            data = pd.read_csv(archivo)
            self.Series(data=data)
        elif (tipoArch == "xls" or tipoArch == "lsx"):
            data = pd.read_excel(archivo)
            self.Series(data=data)
        elif tipoArch == "tml":
            data = pd.read_html(archivo)
            self.Series(data=data)
        else:
            self.label_4.setText("No se pudo cargar el archivo")
        
    def Series(self,data):
        columnas = data.columns
        self.Serie.clear()
        self.Serie_2.clear()
        self.Serie_3.clear()
        self.Serie_4.clear()
        self.comboX.clear()

        self.Serie.addItem("")
        self.Serie_2.addItem("")
        self.Serie_3.addItem("")
        self.Serie_4.addItem("")
        self.comboX.addItem("")
        for i in columnas:
            self.Serie.addItem(i)
            self.Serie_2.addItem(i)
            self.Serie_3.addItem(i)
            self.Serie_4.addItem(i)
            self.comboX.addItem(i)

app = QApplication([])
window = miEditor()
window.show()
app.exec_()


class otraClase(QWidget):
                    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)