# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mensajeria.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 614)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Frame_FondoMensajeria = QFrame(self.centralwidget)
        self.Frame_FondoMensajeria.setObjectName(u"Frame_FondoMensajeria")
        self.Frame_FondoMensajeria.setStyleSheet(u"#Frame_FondoMensajeria {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #cde5fa, stop:0.5 #eaf6ff, stop:1 #ffffff);\n"
"}")
        self.Frame_FondoMensajeria.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_FondoMensajeria.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Frame_FondoMensajeria)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Frame_TituloMensajeria = QFrame(self.Frame_FondoMensajeria)
        self.Frame_TituloMensajeria.setObjectName(u"Frame_TituloMensajeria")
        self.Frame_TituloMensajeria.setStyleSheet(u"    background: transparent;\n"
"    border: none;  /* Opcional: elimina el borde si tambi\u00e9n lo quieres transparente *")
        self.Frame_TituloMensajeria.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_TituloMensajeria.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.Frame_TituloMensajeria)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 311, 31))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Book"])
        font.setPointSize(20)
        font.setItalic(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.Frame_TituloMensajeria)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 81, 71))
        self.label_2.setPixmap(QPixmap(u"Logo_Windows_Live_Messenger(2).png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.Frame_TituloMensajeria)

        self.Frame_FondoPrincipal = QFrame(self.Frame_FondoMensajeria)
        self.Frame_FondoPrincipal.setObjectName(u"Frame_FondoPrincipal")
        self.Frame_FondoPrincipal.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_FondoPrincipal.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frame_FondoPrincipal)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.Frame_FondoPrincipal)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 20, 101, 16))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Book"])
        font1.setPointSize(10)
        font1.setItalic(True)
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 40, 131, 121))
        self.label_6.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.Boton_Perfil = QPushButton(self.frame_2)
        self.Boton_Perfil.setObjectName(u"Boton_Perfil")
        self.Boton_Perfil.setGeometry(QRect(40, 180, 131, 24))
        self.Boton_Perfil.setFont(font1)
        self.Boton_Perfil.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        self.Boton_Perfil.setIcon(icon)
        self.Boton_ChatG = QPushButton(self.frame_2)
        self.Boton_ChatG.setObjectName(u"Boton_ChatG")
        self.Boton_ChatG.setGeometry(QRect(40, 210, 131, 24))
        self.Boton_ChatG.setFont(font1)
        self.Boton_ChatG.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 255, 0);")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.Boton_ChatG.setIcon(icon1)
        self.Boton_NuevoChat = QPushButton(self.frame_2)
        self.Boton_NuevoChat.setObjectName(u"Boton_NuevoChat")
        self.Boton_NuevoChat.setGeometry(QRect(40, 240, 131, 24))
        self.Boton_NuevoChat.setFont(font1)
        self.Boton_NuevoChat.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        self.Boton_NuevoChat.setIcon(icon2)
        self.Boton_Grupos = QPushButton(self.frame_2)
        self.Boton_Grupos.setObjectName(u"Boton_Grupos")
        self.Boton_Grupos.setGeometry(QRect(40, 270, 131, 24))
        self.Boton_Grupos.setFont(font1)
        self.Boton_Grupos.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 40, 30);")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.NetworkOffline))
        self.Boton_Grupos.setIcon(icon3)
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(40, 360, 131, 24))
        font2 = QFont()
        font2.setFamilies([u"Terminal"])
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 255);")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditSelectAll))
        self.pushButton_5.setIcon(icon4)
        self.Boton_Grupos_2 = QPushButton(self.frame_2)
        self.Boton_Grupos_2.setObjectName(u"Boton_Grupos_2")
        self.Boton_Grupos_2.setGeometry(QRect(40, 300, 131, 24))
        self.Boton_Grupos_2.setFont(font1)
        self.Boton_Grupos_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 15, 135);")
        self.Boton_Grupos_2.setIcon(icon3)
        self.Boton_Grupos_3 = QPushButton(self.frame_2)
        self.Boton_Grupos_3.setObjectName(u"Boton_Grupos_3")
        self.Boton_Grupos_3.setGeometry(QRect(40, 330, 131, 24))
        self.Boton_Grupos_3.setFont(font1)
        self.Boton_Grupos_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(155, 5, 0);")
        self.Boton_Grupos_3.setIcon(icon3)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.Frame_FondoPrincipal)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 30, 471, 331))
        self.plainTextEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(147, 147, 147);")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 370, 381, 21))
        self.Boton_Enviar = QPushButton(self.frame)
        self.Boton_Enviar.setObjectName(u"Boton_Enviar")
        self.Boton_Enviar.setGeometry(QRect(400, 370, 75, 24))
        self.Boton_Enviar.setFont(font1)
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSend))
        self.Boton_Enviar.setIcon(icon5)
        self.Boton_Zumbido = QPushButton(self.frame)
        self.Boton_Zumbido.setObjectName(u"Boton_Zumbido")
        self.Boton_Zumbido.setGeometry(QRect(410, 0, 75, 24))
        self.Boton_Zumbido.setFont(font1)
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.CallStart))
        self.Boton_Zumbido.setIcon(icon6)

        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.Frame_FondoPrincipal)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 5)

        self.verticalLayout.addWidget(self.Frame_FondoMensajeria)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 798, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Windows Live Messenger", None))
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hola: Usuario123!", None))
        self.label_6.setText("")
        self.Boton_Perfil.setText(QCoreApplication.translate("MainWindow", u"Mi Perfil", None))
        self.Boton_ChatG.setText(QCoreApplication.translate("MainWindow", u"Chat General", None))
        self.Boton_NuevoChat.setText(QCoreApplication.translate("MainWindow", u"Nuevo Chat", None))
        self.Boton_Grupos.setText(QCoreApplication.translate("MainWindow", u"Nuevo Grupo", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Aplicaciones", None))
        self.Boton_Grupos_2.setText(QCoreApplication.translate("MainWindow", u"Grupos", None))
        self.Boton_Grupos_3.setText(QCoreApplication.translate("MainWindow", u"Salir de grupo", None))
        self.Boton_Enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.Boton_Zumbido.setText(QCoreApplication.translate("MainWindow", u"Timbre", None))
    # retranslateUi

