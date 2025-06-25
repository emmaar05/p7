# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MiPeril.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_miperfil(object):
    def setupUi(self, miperfil):
        if not miperfil.objectName():
            miperfil.setObjectName(u"miperfil")
        miperfil.resize(798, 616)
        self.centralwidget = QWidget(miperfil)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Frame_PerfilFondo = QFrame(self.centralwidget)
        self.Frame_PerfilFondo.setObjectName(u"Frame_PerfilFondo")
        self.Frame_PerfilFondo.setStyleSheet(u"#Frame_PerfilFondo {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #cde5fa, stop:0.5 #eaf6ff, stop:1 #ffffff);\n"
"}")
        self.Frame_PerfilFondo.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_PerfilFondo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Frame_PerfilFondo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Frame_Titulo = QFrame(self.Frame_PerfilFondo)
        self.Frame_Titulo.setObjectName(u"Frame_Titulo")
        self.Frame_Titulo.setStyleSheet(u"#Frame_Titulo {\n"
"    background: transparent;\n"
"    border: none;  /* Opcional: elimina el borde si tambi\u00e9n lo quieres transparente */\n"
"}\n"
"")
        self.Frame_Titulo.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_Titulo.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.Frame_Titulo)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 101, 101))
        self.label.setPixmap(QPixmap(u"Logo_Windows_Live_Messenger(2).png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.Frame_Titulo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 30, 371, 41))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Book"])
        font.setPointSize(26)
        font.setItalic(True)
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.Frame_Titulo)

        self.Frame_FondoPrincipal = QFrame(self.Frame_PerfilFondo)
        self.Frame_FondoPrincipal.setObjectName(u"Frame_FondoPrincipal")
        self.Frame_FondoPrincipal.setStyleSheet(u"#Frame_FondoPrincipal {\n"
"    background: transparent;\n"
"    border: none;  /* Opcional: elimina el borde si tambi\u00e9n lo quieres transparente */\n"
"}\n"
"")
        self.Frame_FondoPrincipal.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_FondoPrincipal.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frame_FondoPrincipal)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Frame_FotoFondo = QFrame(self.Frame_FondoPrincipal)
        self.Frame_FotoFondo.setObjectName(u"Frame_FotoFondo")
        self.Frame_FotoFondo.setStyleSheet(u"#Frame_FotoFondo {\n"
"    background: transparent;\n"
"    border: none;  /* Opcional: elimina el borde si tambi\u00e9n lo quieres transparente */\n"
"}\n"
"")
        self.Frame_FotoFondo.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_FotoFondo.setFrameShadow(QFrame.Shadow.Raised)
        self.label_nombre = QLabel(self.Frame_FotoFondo)
        self.label_nombre.setObjectName(u"label_nombre")
        self.label_nombre.setGeometry(QRect(220, 20, 171, 16))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Book"])
        font1.setPointSize(12)
        font1.setItalic(True)
        self.label_nombre.setFont(font1)
        self.label_imagen = QLabel(self.Frame_FotoFondo)
        self.label_imagen.setObjectName(u"label_imagen")
        self.label_imagen.setGeometry(QRect(110, 50, 391, 341))
        self.label_imagen.setStyleSheet(u"background-color: rgb(200, 200, 200);")

        self.horizontalLayout.addWidget(self.Frame_FotoFondo)

        self.Frame_Datos = QFrame(self.Frame_FondoPrincipal)
        self.Frame_Datos.setObjectName(u"Frame_Datos")
        self.Frame_Datos.setStyleSheet(u"#Frame_Datos {\n"
"    background: transparent;\n"
"    border: none;  /* Opcional: elimina el borde si tambi\u00e9n lo quieres transparente */\n"
"}\n"
"")
        self.Frame_Datos.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_Datos.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.Frame_Datos)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 380, 131, 21))
        font2 = QFont()
        font2.setFamilies([u"Terminal"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.label_5.setFont(font2)
        self.Boton_Salir = QPushButton(self.Frame_Datos)
        self.Boton_Salir.setObjectName(u"Boton_Salir")
        self.Boton_Salir.setGeometry(QRect(10, 10, 121, 24))
        font3 = QFont()
        font3.setFamilies([u"Trebuchet MS"])
        font3.setPointSize(11)
        self.Boton_Salir.setFont(font3)
        self.Boton_Salir.setStyleSheet(u"background-color: rgb(255, 26, 26);\n"
"color: rgb(255, 255, 255);\n"
"    ")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLogOut))
        self.Boton_Salir.setIcon(icon)
        self.Boton_RegresarM = QPushButton(self.Frame_Datos)
        self.Boton_RegresarM.setObjectName(u"Boton_RegresarM")
        self.Boton_RegresarM.setGeometry(QRect(10, 40, 121, 24))
        self.Boton_RegresarM.setFont(font3)
        self.Boton_RegresarM.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailReplySender))
        self.Boton_RegresarM.setIcon(icon1)

        self.horizontalLayout.addWidget(self.Frame_Datos)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.Frame_FondoPrincipal)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)

        self.verticalLayout.addWidget(self.Frame_PerfilFondo)

        miperfil.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(miperfil)
        self.statusbar.setObjectName(u"statusbar")
        miperfil.setStatusBar(self.statusbar)

        self.retranslateUi(miperfil)

        QMetaObject.connectSlotsByName(miperfil)
    # setupUi

    def retranslateUi(self, miperfil):
        miperfil.setWindowTitle(QCoreApplication.translate("miperfil", u"miperfil", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("miperfil", u"Windows Live Messenger", None))
        self.label_nombre.setText(QCoreApplication.translate("miperfil", u"Bienvenido: Usuario1235", None))
        self.label_imagen.setText("")
        self.label_5.setText(QCoreApplication.translate("miperfil", u"PUERTO:", None))
        self.Boton_Salir.setText(QCoreApplication.translate("miperfil", u"Salir", None))
        self.Boton_RegresarM.setText(QCoreApplication.translate("miperfil", u"Mensajeria", None))
    # retranslateUi

