# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Apps.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Apps(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(512, 396)
        Dialog.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 30, 221, 21))
        font = QFont()
        font.setFamilies([u"BankGothic Lt BT"])
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.Boton_Ajedrez = QPushButton(self.frame_3)
        self.Boton_Ajedrez.setObjectName(u"Boton_Ajedrez")
        self.Boton_Ajedrez.setGeometry(QRect(20, 30, 131, 51))
        font1 = QFont()
        font1.setFamilies([u"BankGothic Lt BT"])
        font1.setPointSize(14)
        self.Boton_Ajedrez.setFont(font1)
        self.Boton_Ajedrez.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(8, 121, 197);")
        icon = QIcon()
        icon.addFile(u"LOGO_AJEDREZ.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Boton_Ajedrez.setIcon(icon)
        self.Boton_Gato = QPushButton(self.frame_3)
        self.Boton_Gato.setObjectName(u"Boton_Gato")
        self.Boton_Gato.setGeometry(QRect(170, 30, 131, 51))
        self.Boton_Gato.setFont(font1)
        self.Boton_Gato.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 126, 14);")
        icon1 = QIcon()
        icon1.addFile(u"logo_Gato4.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Boton_Gato.setIcon(icon1)
        self.Boton_Batimovil = QPushButton(self.frame_3)
        self.Boton_Batimovil.setObjectName(u"Boton_Batimovil")
        self.Boton_Batimovil.setGeometry(QRect(330, 30, 131, 51))
        self.Boton_Batimovil.setFont(font1)
        self.Boton_Batimovil.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        icon2 = QIcon()
        icon2.addFile(u"logoBtmn.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Boton_Batimovil.setIcon(icon2)
        self.Boton_Regresar = QPushButton(self.frame_3)
        self.Boton_Regresar.setObjectName(u"Boton_Regresar")
        self.Boton_Regresar.setGeometry(QRect(170, 210, 131, 51))
        self.Boton_Regresar.setFont(font1)
        self.Boton_Regresar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 79, 10);")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditUndo))
        self.Boton_Regresar.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Aplicaciones", None))
        self.Boton_Ajedrez.setText(QCoreApplication.translate("Dialog", u"Ajedrez", None))
        self.Boton_Gato.setText(QCoreApplication.translate("Dialog", u"Gato", None))
        self.Boton_Batimovil.setText(QCoreApplication.translate("Dialog", u"Batimovil", None))
        self.Boton_Regresar.setText(QCoreApplication.translate("Dialog", u"Regresar", None))
    # retranslateUi

