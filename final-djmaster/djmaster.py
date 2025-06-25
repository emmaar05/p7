import sys
import requests
import vlc
import os 
import time

from PyQt6.QtWidgets import QApplication, QMainWindow,QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QLabel, QSlider, QStyle
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from bs4 import BeautifulSoup

vlc_path = r'C:/Program Files/VideoLAN/VLC/libvlc.dll'
# Crear instancia usando la ruta específica
instance = vlc.Instance(f'--plugin-path={os.path.dirname(vlc_path)}')
stream_url = "https://cento02.mipanelradio.com/proxy/fussionr?mp=/stream"

# Crear el reproductor
player = instance.media_player_new()
media = instance.media_new(stream_url)
player.set_media(media)


class ReproductorFussion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DJ Master")
        self.setGeometry(200, 200, 600, 300)
        self.setWindowIcon(QIcon("fussion.ico"))

        self.setStyleSheet('''
    QMainWindow {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                          stop:0 #5FB3E5, stop:1 #335555);
    }

    #labelTitulo {
        font-family: "Montserrat";
        font-size: 36px;
        font-weight: bold;
        color: #31CDB0;
    }

    #labelTitulo2 {
        font-family: "Montserrat";
        font-size: 28px;
        font-weight: bold;
        color: #3551A4;
        qproperty-alignment: 'AlignCenter';
    }

    #enVivo {
        font-family: "Source Sans Pro";
        font-size: 20px;
        font-weight: bold;
        color: #FF3B30; /* rojo brillante estilo alerta */
    }

    QPushButton {
        background-color: #F6F6F6;
        border: 1px solid #CCCCCC;
        border-radius: 8px;
        padding: 5px 10px;
    }

    QPushButton:hover {
        background-color: #E1F5FE;
    }

    QPushButton:pressed {
        background-color: #B3E5FC;
    }

    QToolBox::tab {
        font-family: "Montserrat";
        font-size: 14px;
        background: #E0F7FA;
        padding: 5px;
        margin: 2px;
    }

    QToolBox::tab:selected {
        background: #4DD0E1;
        font-weight: bold;
    }

    QPlainTextEdit {
        background-color: #FFFFFF;
        color: #333333;
        font-size: 20px;
        border-radius: 4px;
        padding: 5px;
    }
''')

        # Widget central para contener todo
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout principal (vertical)
        main_layout = QVBoxLayout(central_widget)

        # --- Layout vertical con color ---
        vertical_container = QWidget()  # Contenedor para aplicar color
        vertical_layout = QVBoxLayout(vertical_container)
        #vertical_container.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
        # --- Layout horizontal con color ---
        horizontal_container = QWidget()  # Contenedor para aplicar color
        horizontal_layout = QHBoxLayout(horizontal_container)
        horizontal_container.setStyleSheet("background-color: #a9a9a9; border: 5px solid #aaa;")

        layout1 = QVBoxLayout()


        #titulo
        self.label_contenido = QLabel("La Voz de una Época,")
        self.label_contenido.setObjectName("labelTitulo")
        self.label_contenido.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #subtitulo
        self.label_contenido2 = QLabel("el Sonido de Hoy")
        self.label_contenido2.setObjectName("labelTitulo2")
        self.label_contenido2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Etiqueta para mostrar la URL actual
        self.label_Servidor = QLabel("Conectando al servidor...")

        self.label_enVivo = QLabel("EN VIVO")
        self.label_enVivo.setObjectName("enVivo")
        self.label_enVivo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_cancion = QLabel("")
        
        self.play_button = QPushButton("")
        self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        #self.stop_button = QPushButton()
        #self.stop_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaStop))
        
        vertical_layout.addWidget(self.label_contenido)
        vertical_layout.addWidget(self.label_contenido2)
        
        vertical_layout.addWidget(self.label_enVivo)
        vertical_layout.addLayout(horizontal_layout)
        horizontal_layout.addWidget(self.label_Servidor)
        horizontal_layout.addWidget(self.play_button)
        #horizontal_layout.addWidget(self.stop_button)
        horizontal_layout.addWidget(self.label_cancion)

        #Actualización del nombre de la cancion cada 10 segundos
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.nombre_cancion)  # Conecta el timer a la función
        self.timer.start(10000)  
        # Primera actualización inmediata
        self.nombre_cancion()


        QMediaPlayer.activeAudioTrack
        self.slider_button = QSlider()
        self.slider_button.setOrientation(Qt.Orientation.Horizontal)


        vertical_layout.addWidget(self.slider_button)

        # # Widget central
        # container = QWidget()
        # container.setLayout(layout)
        # self.setCentralWidget(container)

         # Agregar los dos layouts al principal
        main_layout.addWidget(vertical_container)
        main_layout.addWidget(horizontal_container)       

        # Estado inicial: pausado
        self.is_playing = True 

        # Conectar botones
        self.play_button.clicked.connect(self.toggle_play_pause)
        self.play_button.clicked.connect(self.nombre_cancion)
        #self.stop_button.clicked.connect(self.stop_audio)

    def nombre_cancion(self):
        urlCancion = 'https://cento02.mipanelradio.com/proxy/fussionr/7.html'
        pageCancion = requests.get(urlCancion)
        soupCancion = BeautifulSoup(pageCancion.text,'html')  
        nameSong = soupCancion.find("body").string
        finalSong = nameSong[::-1].rsplit(",")
        print(finalSong[0][::-1]) 
        #Cancion final  
        self.label_cancion.setText(finalSong[0][::-1])


    # --- Alternar entre Play y Pause ---
    def toggle_play_pause(self):
        if self.is_playing:
            # Cambiar a pausa
            self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaStop))
            #self.play_button.setText("Reproducir")
            player.play()
            #agregar el fetch de la cancion actual
            self.label_Servidor.setText("Reproduciendo Fussion Radio")
            print("Pausa")
        else:
            # Cambiar a reproducción
            self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
            print("Reproduciendo")
            player.stop()

        # Cambiar el estado
        self.is_playing = not self.is_playing

    # def play_audio(self):
    #     player.play()
    #     #agregar el fetch de la cancion actual
    #     self.label_Servidor.setText("Reproduciendo Fussion Radio")


    # def stop_audio(self):
    #     """ Detiene el audio """
    #     player.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReproductorFussion()
    window.show()
    sys.exit(app.exec())
