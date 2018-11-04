# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\Python workspace\Electronic_map_of_india\map.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1042, 635)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3_top_log_and_domain = QtGui.QHBoxLayout()
        self.horizontalLayout_3_top_log_and_domain.setObjectName(_fromUtf8("horizontalLayout_3_top_log_and_domain"))
        self.sincgrid_logo = QtGui.QLabel(self.centralwidget)
        self.sincgrid_logo.setText(_fromUtf8(""))
        self.sincgrid_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/F:/Gdrive/sincgrid_gdrive/Sincgrid- MAIN/Administrative/logo/LOGOv9_100.png")))
        self.sincgrid_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.sincgrid_logo.setObjectName(_fromUtf8("sincgrid_logo"))
        self.horizontalLayout_3_top_log_and_domain.addWidget(self.sincgrid_logo)
        self.url = QtGui.QLabel(self.centralwidget)
        self.url.setObjectName(_fromUtf8("url"))
        self.horizontalLayout_3_top_log_and_domain.addWidget(self.url, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cedt_logo = QtGui.QLabel(self.centralwidget)
        self.cedt_logo.setText(_fromUtf8(""))
        self.cedt_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/F:/Downloads/cedt1.png")))
        self.cedt_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.cedt_logo.setObjectName(_fromUtf8("cedt_logo"))
        self.horizontalLayout_3_top_log_and_domain.addWidget(self.cedt_logo)
        self.verticalLayout.addLayout(self.horizontalLayout_3_top_log_and_domain)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.map_data = QtGui.QLabel(self.centralwidget)
        self.map_data.setEnabled(True)
        self.map_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.map_data.setObjectName(_fromUtf8("map_data"))
        self.verticalLayout_2.addWidget(self.map_data)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 2)
        self.verticalLayout_2_log = QtGui.QVBoxLayout()
        self.verticalLayout_2_log.setObjectName(_fromUtf8("verticalLayout_2_log"))
        self.map_log = QtGui.QLabel(self.centralwidget)
        self.map_log.setObjectName(_fromUtf8("map_log"))
        self.verticalLayout_2_log.addWidget(self.map_log)
        self.gridLayout.addLayout(self.verticalLayout_2_log, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Select_port_comboBox = QtGui.QComboBox(self.centralwidget)
        self.Select_port_comboBox.setEditable(False)
        self.Select_port_comboBox.setObjectName(_fromUtf8("Select_port_comboBox"))
        self.Select_port_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.Select_port_comboBox)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Electronics map of india - By sincgrid.com", None))
        self.url.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; vertical-align:super;\">www.sincgrid.com</span></p></body></html>", None))
        self.map_data.setText(_translate("MainWindow", "map_data", None))
        self.map_log.setText(_translate("MainWindow", "map_log", None))
        self.Select_port_comboBox.setItemText(0, _translate("MainWindow", "Select COM", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

