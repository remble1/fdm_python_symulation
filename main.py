from PyQt5.QtWidgets import QSlider, QLabel, QDoubleSpinBox, QSpinBox, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, uic, QtGui
import sys 
import numpy as np
import matplotlib.pyplot as plt
from simulation import makeSimulation
# from PySide2.QtGui import QIcon

class Ui(QtWidgets.QMainWindow):
  def __init__(self):
    super(Ui, self).__init__()

    uic.loadUi('D:\program_pola\MainWindowSample3.ui', self)
    self.setFixedSize(653, 527)
    self.show()
    self.ui = Ui
    self.setWindowIcon(QtGui.QIcon('icons/duckicon.png')) 

    self.labelWarning = self.findChild(QLabel, "label_warning")
    self.imageLabel = self.findChild(QLabel, "imageLabel")

    self.countButton = self.findChild(QPushButton, "pushButton")
    self.countButton.clicked.connect(self.buttonEvent)

    self.sliderDlugoscOdcinka = self.findChild(QSlider, "dlugoscOdcinkaSlider")
    self.labelDlugoscOdcinka = self.findChild(QLabel, "labelDlugoscOdcinka")
    self.iloscWezlowSlider = self.findChild(QSlider, "iloscWezlowSlider")
    self.labelloscWezlow = self.findChild(QLabel, "labelloscWezlow")

    self.krokCzasowy = self.findChild(QDoubleSpinBox, "krokCzasowyDoubleSpinBox")
    self.konczowyCzasObl = self.findChild(QDoubleSpinBox, "koncowyCzasDoubleSpinBox")

    self.setTempL = self.findChild(QSpinBox, "setTempL")
    self.setTempP = self.findChild(QSpinBox, "setTempP")
    self.setTempM = self.findChild(QSpinBox, "setTempM")

    self.sliderDlugoscOdcinka.valueChanged.connect(self.dlugosc_changed)
    self.iloscWezlowSlider.valueChanged.connect(self.wezly_changed)
    self.krokCzasowy.valueChanged.connect(self.doKrok)
    self.konczowyCzasObl.valueChanged.connect(self.doCzasObl)

    self.setTempL.valueChanged.connect(self.doSetTempL)
    self.setTempP.valueChanged.connect(self.doSetTempP)
    self.setTempM.valueChanged.connect(self.doSetTempM)

  def doKrok(self):
    print(f"Krok czasowy: {self.krokCzasowy.value()}")

  def doCzasObl(self):
    print(f"Końcowy czas obliczeń: {self.konczowyCzasObl.value()}")

  def doSetTempL(self):
    print(f"Temperatura na lewym końcu wynosi: {self.setTempL.value()}")

  def doSetTempP(self):
    print(f"Temperatura na prawym końcu wynosi: {self.setTempP.value()}")

  def doSetTempM(self):
    print(f"Temperatura całego drutu wynosi: {self.setTempM.value()}")

  def dlugosc_changed(self):
    new_value = str(self.dlugoscOdcinkaSlider.value()*10)
    self.labelDlugoscOdcinka.setText(f"{new_value} cm")

  def wezly_changed(self):
    new_value = str(self.iloscWezlowSlider.value())
    self.labelloscWezlow.setText(new_value)

  def buttonEvent(self):
    """here is all stuff to count, after clicked"""
    dlugoscOdcinka = float(self.dlugoscOdcinkaSlider.value())/10
    iloscWezlow = float(self.iloscWezlowSlider.value())
    czasObliczen = float(self.konczowyCzasObl.value())
    krokObliczen = float(self.krokCzasowy.value())
    nodeTempL = float(self.setTempL.value())
    nodeTempInit = float(self.setTempM.value())
    nodeTempR = float(self.setTempP.value())
  
    a = self.iloscWezlowSlider.value()

    if a != '':
      try:
        a = int(a)    
        if 2 < a < 51 :
            n_x = 291 // (int(a) - 1)
            grid = np.ones((291, 111)) * 255 # make white blank pic 
            grid[::][::n_x] = 0
            grid = grid.T
            img_path = 'icons/test.png'
            plt.imsave(img_path, grid, cmap='gray', vmin=0, vmax=255)
            self.imageLabel.setPixmap(QPixmap(img_path))
      except Exception as ex:
          print(ex)    

    if czasObliczen and krokObliczen != 0:
      self.labelWarning.setText(f"")
      step = ((dlugoscOdcinka)/(iloscWezlow-1))

      #               dlugosc,       step, czas_all,      czas_step,  left_temp = 273.15, initial_temp = 293.15, right_temp
      makeSimulation(dlugoscOdcinka, step, czasObliczen, krokObliczen, nodeTempL, nodeTempInit, nodeTempR)

    else: 
      self.labelWarning.setText(f"Krok czasowy ani czas obliczeń nie może wynosić zero.")



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()