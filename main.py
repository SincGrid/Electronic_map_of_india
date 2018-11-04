import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from map import *

'''
Genrate the map.py
E:\Python27\Lib\site-packages\PyQt4\pyuic4.bat -x "H:\Python workspace\Electronic_map_of_india\map.ui" -o "H:\Python workspace\Electronic_map_of_india\map.py"
'''

class Populate_Map(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #logo adding
        self.sincgrid_logo.setPixmap(QtGui.QPixmap("LOGOv9_100.png"))
        # self.sincgrid_logo.setAlignment(QtCore.)
        self.sincgrid_logo.setScaledContents(False)
        # self.label_logo.setMinimumSize(1,1)

        self.cedt_logo.setPixmap(QtGui.QPixmap("cedt.png"))
        self.cedt_logo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.cedt_logo.setScaledContents(False)
        # self.label_logo.setMinimumSize(1,1)

if __name__ =="__main__":
    app = QtGui.QApplication(sys.argv)
    # MainWindow = QtGui.QMainWindow()
    ui = Populate_Map()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    ui.show()
    sys.exit(app.exec_())