# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'offer_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(424, 346)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Alien.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog {\n"
"background-color: qconicalgradient(cx:0.8125, cy:0.761, angle:0, stop:0 rgba(191, 218, 15, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(172, 172, 172, 255));}")
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setGeometry(QtCore.QRect(160, 230, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ok_button.setFont(font)
        self.ok_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ok_button.setAcceptDrops(False)
        self.ok_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.994, y1:0.869318, x2:1, y2:0, stop:0 rgba(173, 173, 173, 255), stop:1 rgba(227, 227, 227, 255));")
        self.ok_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon1)
        self.ok_button.setIconSize(QtCore.QSize(32, 32))
        self.ok_button.setCheckable(False)
        self.ok_button.setObjectName("ok_button")
        self.fichero_oferta = QtWidgets.QLineEdit(Dialog)
        self.fichero_oferta.setGeometry(QtCore.QRect(30, 170, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fichero_oferta.setFont(font)
        self.fichero_oferta.setAlignment(QtCore.Qt.AlignCenter)
        self.fichero_oferta.setObjectName("fichero_oferta")
        self.browse_Button = QtWidgets.QPushButton(Dialog)
        self.browse_Button.setGeometry(QtCore.QRect(360, 170, 31, 31))
        self.browse_Button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browse_Button.setIcon(icon2)
        self.browse_Button.setObjectName("browse_Button")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(320, 20, 81, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/didata.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 25, 201, 81))
        self.label_2.setStyleSheet("color:rgb(23, 77, 255)")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(39, 230, 101, 41))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setGeometry(QtCore.QRect(260, 230, 101, 41))
        self.widget_3.setObjectName("widget_3")
        self.solo_mantenimiento = QtWidgets.QRadioButton(Dialog)
        self.solo_mantenimiento.setGeometry(QtCore.QRect(120, 130, 171, 17))
        font = QtGui.QFont()
        font.setItalic(True)
        self.solo_mantenimiento.setFont(font)
        self.solo_mantenimiento.setStyleSheet("color:rgb(170, 0, 0)")
        self.solo_mantenimiento.setObjectName("solo_mantenimiento")
        self.version = QtWidgets.QLabel(Dialog)
        self.version.setGeometry(QtCore.QRect(290, 305, 111, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.version.setFont(font)
        self.version.setStyleSheet("color:rgb(0, 85, 255)")
        self.version.setText("")
        self.version.setObjectName("version")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ofertas multifabricante"))
        self.fichero_oferta.setPlaceholderText(_translate("Dialog", "Fichero de oferta"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Conversión de ofertas</span></p><p align=\"center\"><span style=\" font-size:14pt;\">a formato Direct</span></p></body></html>"))
        self.solo_mantenimiento.setText(_translate("Dialog", "Procesar sólo mantenimientos"))

import icons_rc
