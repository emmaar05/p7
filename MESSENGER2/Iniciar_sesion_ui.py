# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Iniciar_sesion.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Mensajeria(object):
    def setupUi(self, Mensajeria):
        if not Mensajeria.objectName():
            Mensajeria.setObjectName(u"Mensajeria")
        Mensajeria.resize(765, 609)
        self.centralwidget = QWidget(Mensajeria)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Frame_Messenger = QFrame(self.centralwidget)
        self.Frame_Messenger.setObjectName(u"Frame_Messenger")
        self.Frame_Messenger.setStyleSheet(u"#Frame_Messenger {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #cde5fa, stop:0.5 #eaf6ff, stop:1 #ffffff);\n"
"}\n"
"")
        self.Frame_Messenger.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_Messenger.setFrameShadow(QFrame.Shadow.Raised)
        self.label_iniciar_sesion = QLabel(self.Frame_Messenger)
        self.label_iniciar_sesion.setObjectName(u"label_iniciar_sesion")
        self.label_iniciar_sesion.setGeometry(QRect(210, 40, 341, 61))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Book"])
        font.setPointSize(36)
        font.setItalic(True)
        self.label_iniciar_sesion.setFont(font)
        self.label_iniciar_sesion_2 = QLabel(self.Frame_Messenger)
        self.label_iniciar_sesion_2.setObjectName(u"label_iniciar_sesion_2")
        self.label_iniciar_sesion_2.setGeometry(QRect(200, 100, 521, 61))
        self.label_iniciar_sesion_2.setFont(font)
        self.Foto_usuario = QLabel(self.Frame_Messenger)
        self.Foto_usuario.setObjectName(u"Foto_usuario")
        self.Foto_usuario.setGeometry(QRect(90, 220, 181, 181))
        self.Foto_usuario.setPixmap(QPixmap(u"Usuario_sin_registrar.png"))
        self.Foto_usuario.setScaledContents(True)
        self.label_Logo = QLabel(self.Frame_Messenger)
        self.label_Logo.setObjectName(u"label_Logo")
        self.label_Logo.setGeometry(QRect(20, 10, 171, 171))
        self.label_Logo.setPixmap(QPixmap(u"Logo_Windows_Live_Messenger(2).png"))
        self.label_Logo.setScaledContents(True)
        self.label = QLabel(self.Frame_Messenger)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 240, 171, 21))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic"])
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.textEdit = QTextEdit(self.Frame_Messenger)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(300, 270, 341, 31))
        self.pushButton = QPushButton(self.Frame_Messenger)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 440, 171, 24))
        self.pushButton_2 = QPushButton(self.Frame_Messenger)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(560, 480, 75, 24))
        self.pushButton_2.setFont(font1)
        self.label_2 = QLabel(self.Frame_Messenger)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 320, 91, 21))
        self.label_2.setFont(font1)
        self.Selector_Edad = QSpinBox(self.Frame_Messenger)
        self.Selector_Edad.setObjectName(u"Selector_Edad")
        self.Selector_Edad.setGeometry(QRect(400, 320, 67, 24))
        self.Selector_Edad.setMaximum(200)
        self.combo_Sexo = QComboBox(self.Frame_Messenger)
        self.combo_Sexo.addItem("")
        self.combo_Sexo.addItem("")
        self.combo_Sexo.addItem("")
        self.combo_Sexo.setObjectName(u"combo_Sexo")
        self.combo_Sexo.setGeometry(QRect(340, 370, 101, 24))
        self.combo_Sexo.setEditable(False)
        self.label_3 = QLabel(self.Frame_Messenger)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 370, 41, 21))
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.Frame_Messenger)

        Mensajeria.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Mensajeria)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 765, 33))
        Mensajeria.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Mensajeria)
        self.statusbar.setObjectName(u"statusbar")
        Mensajeria.setStatusBar(self.statusbar)

        self.retranslateUi(Mensajeria)

        QMetaObject.connectSlotsByName(Mensajeria)
    # setupUi

    def retranslateUi(self, Mensajeria):
        Mensajeria.setWindowTitle(QCoreApplication.translate("Mensajeria", u"MainWindow", None))
        self.label_iniciar_sesion.setText(QCoreApplication.translate("Mensajeria", u"Iniciar sesi\u00f3n en ", None))
        self.label_iniciar_sesion_2.setText(QCoreApplication.translate("Mensajeria", u"Windows Live Messenger", None))
        self.Foto_usuario.setText("")
        self.label_Logo.setText("")
        self.label.setText(QCoreApplication.translate("Mensajeria", u"Ingrese su Nombre de Usuario:", None))
        self.pushButton.setText(QCoreApplication.translate("Mensajeria", u"Seleccionar Foto de Perfil", None))
        self.pushButton_2.setText(QCoreApplication.translate("Mensajeria", u"Ingresar", None))
        self.label_2.setText(QCoreApplication.translate("Mensajeria", u"Ingrese su Edad", None))
        self.combo_Sexo.setItemText(0, QCoreApplication.translate("Mensajeria", u"Masculino", None))
        self.combo_Sexo.setItemText(1, QCoreApplication.translate("Mensajeria", u"Femenino", None))
        self.combo_Sexo.setItemText(2, QCoreApplication.translate("Mensajeria", u"Sin Especificar", None))

        self.label_3.setText(QCoreApplication.translate("Mensajeria", u"Sexo:", None))
    # retranslateUi

