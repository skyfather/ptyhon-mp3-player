import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QApplication,QLabel
from PyQt5.QtCore import QSize,QRect
import pygame


# pygame.mixer.init()
# clock = pygame.time.Clock()
# pygame.mixer.music.load('near_the_cross.mp3')
# pygame.mixer.music.play(0)
#
# while pygame.mixer.music.get_busy():
#     clock.tick(30)

class MusicPlayer(QWidget):
    """docstring for MusicPlayer."""

    def __init__(self):
        super(MusicPlayer, self).__init__()
        
        #initializing the mixer
        freq = 44100     # audio CD quality
        bitsize = -16    # unsigned 16 bit
        channels = 2     # 1 is mono, 2 is stereo
        buffer = 2048    # number of samples (experiment to get best sound)
        # pygame.mixer.init(freq,bitsize,channels,buffer)


        QWidget.resize(self,QSize(500,400))
        QWidget.setWindowTitle(self,"Music")

        self.lblTitle = QLabel("Song Title",self)
        self.lblTitle.setGeometry(QRect(50,0,400,50))
        self.btnPlay = QPushButton('Play',self)
        self.btnPlay.move(30,280)
        self.btnStop = QPushButton('Stop',self)
        self.btnStop.move(130,280)

        #clicking the play button plays the music
        self.btnPlay.clicked.connect(self.playMusic)
        #clicking the stop button stops the music
        self.btnStop.clicked.connect(self.stopMusic)

    def playMusic(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.mixer.init()
        pygame.mixer.music.load('near_the_cross.mp3')
        # self.mixer.music.load('near_the_cross.mp3')
        pygame.mixer.music.play(0)
        # self.mixer.music.play(0)
        
        # while pygame.mixer.music.get_busy():
        #     self.clock.tick(30)

    def stopMusic(self):
        pygame.mixer.music.stop()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec_())
