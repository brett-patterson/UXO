# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'uxo_dialog.ui'
#
# Created: Wed Jan 04 22:07:35 2012
#      by: PyQt4 UI code generator 4.8.6


"""
CUSTOM EDITS INSIDE!!!!!
BE VERY CAREFUL WHEN GENERATING A NEW .PY FILE FROM .UI
"""

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_uxo_dialog(object):
    def setupUi(self, uxo_dialog):
        uxo_dialog.setObjectName(_fromUtf8("uxo_dialog"))
        uxo_dialog.resize(404, 443)
        uxo_dialog.setWindowTitle(QtGui.QApplication.translate("uxo_dialog", "UXO", None, QtGui.QApplication.UnicodeUTF8))
        uxo_dialog.setModal(True)
        self.buttonSafe = QtGui.QPushButton(uxo_dialog)
        self.buttonSafe.setGeometry(QtCore.QRect(40, 391, 71, 41))
        self.buttonSafe.setText(QtGui.QApplication.translate("uxo_dialog", "Safe", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("res/img/safe.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSafe.setIcon(icon)
        self.buttonSafe.setIconSize(QtCore.QSize(32, 32))
        self.buttonSafe.setObjectName(_fromUtf8("buttonSafe"))
        self.buttonNotSafe = QtGui.QPushButton(uxo_dialog)
        self.buttonNotSafe.setGeometry(QtCore.QRect(290, 391, 71, 41))
        self.buttonNotSafe.setText(QtGui.QApplication.translate("uxo_dialog", "UXO", None, QtGui.QApplication.UnicodeUTF8))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("res/img/not_safe.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNotSafe.setIcon(icon1)
        self.buttonNotSafe.setIconSize(QtCore.QSize(32, 32))
        self.buttonNotSafe.setObjectName(_fromUtf8("buttonNotSafe"))
        self.buttonZoom = QtGui.QPushButton(uxo_dialog)
        self.buttonZoom.setGeometry(QtCore.QRect(175, 340, 51, 41))
        self.buttonZoom.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("res/img/zoom.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonZoom.setIcon(icon2)
        self.buttonZoom.setIconSize(QtCore.QSize(32, 32))
        self.buttonZoom.setObjectName(_fromUtf8("buttonZoom"))
        self.label = QtGui.QLabel(uxo_dialog)
        self.label.setGeometry(QtCore.QRect(16, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("uxo_dialog", "You happen across an object lying on the ground...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(uxo_dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 380, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("uxo_dialog", "Is it safe?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.scrollArea = QtGui.QScrollArea(uxo_dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 381, 271))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.imageLabel = QtGui.QLabel()
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, 361, 251))
        self.imageLabel.setText(_fromUtf8(""))
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.scrollArea.setWidget(self.imageLabel)

        self.retranslateUi(uxo_dialog)
        QtCore.QMetaObject.connectSlotsByName(uxo_dialog)

    def retranslateUi(self, uxo_dialog):
        pass

