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
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, -5, 1011, 131))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3_top_log_and_domain = QtGui.QHBoxLayout()
        self.horizontalLayout_3_top_log_and_domain.setObjectName(_fromUtf8("horizontalLayout_3_top_log_and_domain"))
        self.sincgrid_logo = QtGui.QLabel(self.verticalLayoutWidget)
        self.sincgrid_logo.setText(_fromUtf8(""))
        self.sincgrid_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/F:/Gdrive/sincgrid_gdrive/Sincgrid- MAIN/Administrative/logo/LOGOv9_100.png")))
        self.sincgrid_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.sincgrid_logo.setObjectName(_fromUtf8("sincgrid_logo"))
        self.horizontalLayout_3_top_log_and_domain.addWidget(self.sincgrid_logo)
        self.url = QtGui.QLabel(self.verticalLayoutWidget)
        self.url.setObjectName(_fromUtf8("url"))
        self.horizontalLayout_3_top_log_and_domain.addWidget(self.url, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cedt_logo = QtGui.QLabel(self.verticalLayoutWidget)
        self.cedt_logo.setText(_fromUtf8(""))
        self.cedt_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/F:/Downloads/cedt1.png")))
        self.cedt_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.cedt_logo.setObjectName(_fromUtf8("cedt_logo"))
        self.horizontalLayout_3_top_log_and_domain.addWidget(self.cedt_logo)
        self.verticalLayout.addLayout(self.horizontalLayout_3_top_log_and_domain)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 510, 621, 91))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2_log = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2_log.setObjectName(_fromUtf8("verticalLayout_2_log"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(640, 510, 381, 89))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.SelectCom = QtGui.QTextEdit(self.horizontalLayoutWidget_4)
        self.SelectCom.setObjectName(_fromUtf8("SelectCom"))
        self.horizontalLayout_2.addWidget(self.SelectCom)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.map_log = QtGui.QLabel(self.centralwidget)
        self.map_log.setGeometry(QtCore.QRect(10, 508, 619, 71))
        self.map_log.setObjectName(_fromUtf8("map_log"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 150, 1011, 351))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.map_data = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.map_data.setEnabled(True)
        self.map_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.map_data.setObjectName(_fromUtf8("map_data"))
        self.verticalLayout_2.addWidget(self.map_data)
        self.verticalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.map_log.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Electronics map of india - By sincgrid.com", None))
        self.url.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; vertical-align:super;\">www.sincgrid.com</span></p></body></html>", None))
        self.SelectCom.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; vertical-align:super;\">Type Com port</span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.map_log.setText(_translate("MainWindow", "map_log", None))
        self.map_data.setText(_translate("MainWindow", "map_data", None))

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

