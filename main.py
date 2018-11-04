import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from map import *
from FindCom import *
from livedatafeed import LiveDataFeed
from com_monitor import ComMonitorThread
import logging
import Colorer
import CommonUtility as cu
import inspect

import Queue

'''
Genrate the map.py
E:\Python27\Lib\site-packages\PyQt4\pyuic4.bat -x "H:\Python workspace\Electronic_map_of_india\map.ui" -o "H:\Python workspace\Electronic_map_of_india\map.py"
'''

class Populate_Map(QMainWindow, Ui_MainWindow):
    logger = logging.getLogger(__name__)
    def __init__(self,log):
        self.logger=log
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        '''logo adding'''
        self.sincgrid_logo.setPixmap(QtGui.QPixmap("LOGOv9_100.png"))
        self.sincgrid_logo.setScaledContents(False)
        
        self.cedt_logo.setPixmap(QtGui.QPixmap("cedt.png"))
        self.cedt_logo.setScaledContents(False)

        '''COM port'''
        self.portname=None
        self.monitor_active = False
        self.com_monitor = None
        self.com_data_q = None
        self.com_error_q = None
        self.livefeed = LiveDataFeed()
        # self.set_actions_enable_state()
        '''populate the com port'''
        ports=available_serial_ports()
        for items in (ports):
            # print (items)
            self.Select_port_comboBox.addItem(items)
        self.Select_port_comboBox.currentIndexChanged.connect(self.selectionchange)

        self.timer = QtCore.QTimer()

        self.pushButton.clicked.connect(self.on_start)

    def selectionchange(self,i):
        # print "Items in the list are :"
            
        # for count in range(self.Select_port_comboBox.count()):
        #     print self.Select_port_comboBox.itemText(count)
        try:
            self.logger.critical("Current index {} selection changed ".format(self.Select_port_comboBox.currentText()))
            self.map_log.setText("{} is selected".format(self.Select_port_comboBox.currentText()))
            self.logger.critical("Type self.Select_port_comboBox.currentText() is {}\n and data is {}".format(type(self.Select_port_comboBox.currentText()),self.Select_port_comboBox.currentText()))
            self.portname=str(self.Select_port_comboBox.currentText())
            self.logger.critical("Type self.portname is {}\n and data is {}".format(type(self.portname),self.portname))
            self.set_actions_enable_state()
        except Exception as e:
            self.logger.error(str(e))
    def on_timer(self):
        """ Executed periodically when the monitor update timer
            is fired.
        """
        self.read_serial_data()
        self.update_monitor()
    
    def on_stop(self):
        """ Stop the monitor
        """
        if self.com_monitor is not None:
            self.com_monitor.join(0.01)
            self.com_monitor = None

        self.monitor_active = False
        self.timer.stop()
        self.set_actions_enable_state()
        
        self.map_log.setText('Monitor idle')

    def on_start(self):
        """ Start the monitor: com_monitor thread and the update
            timer
        """
        self.logger.warning("start button is pressed")
        if self.com_monitor is not None or self.portname == '':
            return
        try:
            self.data_q = Queue.Queue()
            self.error_q = Queue.Queue()
            self.com_monitor = ComMonitorThread(
                self.logger,
                self.data_q,
                self.error_q,
                self.portname,
                9600)
            self.com_monitor.start()
        except Exception as e:
            self.logger.error(str(e))
        com_error = cu.get_item_from_queue(self.error_q)
        if com_error is not None:
            QtCore.QMessageBox.critical(self, 'ComMonitorThread error',
                com_error)
            self.com_monitor = None

        self.monitor_active = True
        self.set_actions_enable_state()
        
        self.timer = QtCore.QTimer()
        self.connect(self.timer, SIGNAL('timeout()'), self.on_timer)
        
        update_freq = self.updatespeed_knob.value()
        if update_freq > 0:
            self.timer.start(1000.0 / update_freq)
        
        self.map_log.setText('Monitor running')

    def set_actions_enable_state(self):
        if self.portname.text() == None:
            start_enable = stop_enable = False
        else:
            start_enable = not self.monitor_active
            stop_enable = self.monitor_active
        
        self.start_action.setEnabled(start_enable)
        self.stop_action.setEnabled(stop_enable)

if __name__ =="__main__":
    # print(inspect.getsource(logging))
    logger = logging.getLogger(__name__)
    cu.init_logging_commands(logger)
    logger.critical("Logging started in {} mode".format('yo yo'))
    app = QtGui.QApplication(sys.argv)
    # MainWindow = QtGui.QMainWindow()
    ui = Populate_Map(logger)
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    ui.show()
    sys.exit(app.exec_())