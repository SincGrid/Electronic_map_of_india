# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\test\map.ui'
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
        MainWindow.resize(1040, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1021, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3_top_log_and_domain = QtGui.QHBoxLayout()
        self.horizontalLayout_3_top_log_and_domain.setObjectName(_fromUtf8("horizontalLayout_3_top_log_and_domain"))
        self.logo = QtGui.QLabel(self.verticalLayoutWidget)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.horizontalLayout_3_top_log_and_domain.addWidget(self.logo, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.url = QtGui.QLabel(self.verticalLayoutWidget)
        self.url.setObjectName(_fromUtf8("url"))
        self.horizontalLayout_3_top_log_and_domain.addWidget(self.url, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_3_top_log_and_domain)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 481, 371))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.map_image_object = QtGui.QLabel(self.horizontalLayoutWidget)
        self.map_image_object.setTextFormat(QtCore.Qt.PlainText)
        self.map_image_object.setObjectName(_fromUtf8("map_image_object"))
        self.horizontalLayout.addWidget(self.map_image_object)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(500, 130, 521, 371))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2_map_detail = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2_map_detail.setObjectName(_fromUtf8("horizontalLayout_2_map_detail"))
        self.map_data = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.map_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.map_data.setObjectName(_fromUtf8("map_data"))
        self.horizontalLayout_2_map_detail.addWidget(self.map_data)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 510, 1011, 51))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2_log = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2_log.setObjectName(_fromUtf8("verticalLayout_2_log"))
        self.map_log = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.map_log.setObjectName(_fromUtf8("map_log"))
        self.verticalLayout_2_log.addWidget(self.map_log)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.setMapTo(1,"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def setMapTo(self,mapId,Content):
        pixmap = QtGui.QPixmap("images/{}.png".format(str(mapId)))
        pixmap_image = QtGui.QPixmap(pixmap)
        self.map_image_object.setPixmap(pixmap_image)
        self.map_image_object.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.map_image_object.setScaledContents(True)
        self.map_image_object.setMinimumSize(1,1)

        self.map_data.setText(Content)
        self.map_data.setWordWrap(True)
        self.map_log.setText("working log - delhi selected")


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Electronics map of india - By sincgrid.com", None))
        self.logo.setText(_translate("MainWindow", "logo", None))
        pixmap = QtGui.QPixmap('LOGOv9_100.png')
        pixmap_image = QtGui.QPixmap(pixmap)
        self.logo.setPixmap(pixmap_image)
        self.logo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.logo.setScaledContents(False)
        self.logo.setMinimumSize(1,1)
        self.url.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:24pt; vertical-align:center;\">www.sincgrid.com</span></p></body></html>", None))
        self.url.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.map_image_object.setText(_translate("MainWindow", "Map_image", None))
        self.map_data.setText(_translate("MainWindow", "map_data", None))
        self.map_log.setText(_translate("MainWindow", "map_log", None))

        self.map_log.setText("log")

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

