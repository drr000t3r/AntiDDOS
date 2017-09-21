# -*- coding: utf-8 -*-
import sys
import time
from netifaces import ifaddresses, AF_INET

import pyautogui
import winreg as wr
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL, pyqtSlot, QObject, SLOT
from PyQt4.QtGui import *



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
    def envirementDesktop(self):
        self.scx, self.scy = pyautogui.size()
        self.widthSize = (3 * self.scx) / 4
        self.hiegthSize = (3 * self.scy) / 4
        self.scale = 0.75

    def setupUi(self, MainWindow):
        self.envirementDesktop()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        # palette = QtGui.QPalette()
        # palette.setColor(QtGui.QPalette.Background, QtCore.Qt.red)
        # MainWindow.setPalette(palette)
        MainWindow.resize(self.widthSize, self.hiegthSize)
        MainWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0.02 * self.widthSize, 10, 1200, 90))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.itemSelect = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.itemSelect.setObjectName(_fromUtf8("ItemSelect"))
        self.horizontalLayout.addWidget(self.itemSelect)
        self.btnMonitoring = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnMonitoring.setObjectName(_fromUtf8("btnMonitoring"))
        self.horizontalLayout.addWidget(self.btnMonitoring)
        self.btnStop = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.btnStop.setVisible(False)
        self.horizontalLayout.addWidget(self.btnStop)
        # self.tableView = MyTableView(self.centralwidget)
        self.tableView.setGeometry(
            QtCore.QRect(0.025 * self.widthSize, 0.1 * self.hiegthSize, 0.95 * self.widthSize, 0.80 * self.hiegthSize))
        # self.tableView.setHorizontalHeader(QHeaderView(Qt.Horizontal, self.tableView))
        self.headers = ["time", "Source IP", "Destination IP", "Protocol", "Length", "Info"]
        self.model = QStandardItemModel()
        self.model.setColumnCount(5)
        self.model.setHorizontalHeaderLabels(self.headers)
        # self.tableView.setModel(self.model)
        # self.tableView.setColumnWidth(0, 200)
        # self.tableView.setColumnWidth(1, 400)
        # self.tableView.setColumnWidth(2, 400)
        # self.tableView.setColumnWidth(3, 150)
        # self.tableView.setColumnWidth(4, 150)
        # self.tableView.setColumnWidth(5, 800)
        # self.tableView.setObjectName(_fromUtf8("tableView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setShortcut(QKeySequence("Ctrl+N"))
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setShortcut(QKeySequence("Ctrl+Q"))
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionFullScreen = QtGui.QAction(MainWindow)
        self.actionFullScreen.setShortcut(QKeySequence("Ctrl+F"))
        self.actionFullScreen.setObjectName(_fromUtf8("actionFullScreen"))
        self.actionOption = QtGui.QAction(MainWindow)
        self.actionOption.setObjectName(_fromUtf8("actionOption"))
        self.actionTelnet = QtGui.QAction(MainWindow)
        self.actionTelnet.setObjectName(_fromUtf8("actionTelnet"))
        self.actionHTTP = QtGui.QAction(MainWindow)
        self.actionHTTP.setObjectName(_fromUtf8("actionHTTP"))
        self.actionDocument = QtGui.QAction(MainWindow)
        self.actionDocument.setObjectName(_fromUtf8("actionDocument"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionFullScreen)
        self.menuTools.addAction(self.actionTelnet)
        self.menuTools.addAction(self.actionHTTP)
        self.menuTools.addAction(self.actionOption)
        self.menuAbout.addAction(self.actionDocument)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        MainWindow.setWindowIcon(QtGui.QIcon('asset/Icon.png'))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Trafice and  Analyz and monitoring", None))
        self.btnMonitoring.setText(_translate("MainWindow", "Monitoring", None))
        self.btnStop.setText(_translate("MainWindow", "Stop", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuTools.setTitle(_translate("MainWindow", "tools", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionFullScreen.setText(_translate("MainWindow", "FullScreen", None))
        self.actionOption.setText(_translate("MainWindow", "Option", None))
        self.actionTelnet.setText(_translate("MainWindow", "Telnet", None))
        self.actionHTTP.setText(_translate("MainWindow", "HTTP", None))
        self.actionDocument.setText(_translate("MainWindow", "Document", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

    def initialTableView(self):
        self.model.setColumnCount(5)
        self.model.setHorizontalHeaderLabels(self.headers)
        # self.tableView.setModel(self.model)
        # self.tableView.setColumnWidth(0, 200)
        # self.tableView.setColumnWidth(1, 400)
        # self.tableView.setColumnWidth(2, 400)
        # self.tableView.setColumnWidth(3, 150)
        # self.tableView.setColumnWidth(4, 150)
        # self.tableView.setColumnWidth(5, 800)


class ViewMain(QtGui.QMainWindow, Ui_MainWindow):
    pass
