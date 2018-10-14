import sys
from PyQt4 import QtGui, QtSvg
from PyQt4.QtCore import QThread, SIGNAL
import map
# app = QtGui.QApplication(sys.argv) 
# svgWidget = QtSvg.QSvgWidget('./india.svg')
# svgWidget.setGeometry(50,50,759,668)

# svgWidget.show()
class getPostsThread(QThread):
    def __init__(self,mapId,Content,log):
        QThread.__init__(self)
        self.mapId=mapId
        self.Content=Content
        self.log=log

    def __del__(self):
        self.wait()
    
    def _get_new_serial_data(self):
        pass
    def run(self):
        pass
class ThreadingUpdate(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None, flags=0):
        return super(ThreadingUpdate, self).__init__(parent, flags)
def gui_init():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    gui_init()

    ui.setMapToUpdate(2,"xyz")
