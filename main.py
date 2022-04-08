from PyQt5.QtWidgets import QSlider, QLabel
from PyQt5 import QtWidgets, uic 
import sys 



class Ui(QtWidgets.QMainWindow):
  def __init__(self):
    super(Ui, self).__init__()
    uic.loadUi('D:\program_pola\MainWindowSample1.ui', self)
    self.show()
    self.ui = Ui
    self.dlugoscOdcinkaSlider = self.findChild(QSlider, "dlugoscOdcinkaSlider")
    self.labelDlugoscOdcinka = self.findChild(QLabel, "labelDlugoscOdcinka")
    self.dlugoscOdcinkaSlider.valueChanged.connect(self.number_changed)

  def number_changed(self):
    new_value = str(self.dlugoscOdcinkaSlider.value())
    self.labelDlugoscOdcinka.setText(new_value)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()