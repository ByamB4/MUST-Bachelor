from PyQt5 import QtCore, QtGui, QtWidgets
import pygame

FREQ = 44100   
BITSIZE = -16  
CHANNELS = 2   
BUFFER = 1024  
FRAMERATE = 60 
morsetab = {
    'a': '.- ',     'b': '-... ',
    'c': '-.-. ',   'd': '-.. ',
    'e': '. ',      'f': '..-. ',
    'g': '--. ',    'h': '.... ',
    'i': '.. ',     'j': '.--- ',
    'k': '-.- ',    'l': '.-.. ',
    'm': '-- ',     'n': '-. ',
    'o': '--- ',    'p': '.--. ',
    'q': '--.- ',   'r': '.-. ',
    's': '... ',    't': '- ',
    'u': '..- ',    'v': '...- ',
    'w': '.-- ',    'x': '-..- ',
    'y': '-.-- ',   'z': '--.. ',
    '0': '----- ',  ',': '--..-- ',
    '1': '.---- ',  '.': '.-.-.- ',
    '2': '..--- ',  '?': '..--.. ',
    '3': '...-- ',  ';': '-.-.-. ',
    '4': '....- ',  ':': '---... ',
    '5': '..... ',  "'": '.----. ',
    '6': '-.... ',  '-': '-....- ',
    '7': '--... ',  '/': '-..-. ',
    '8': '---.. ',  '(': '-.--.- ',
    '9': '----. ',  ')': '-.--.- ',
    ' ': '|',       '_': '..--.- ',
}

morse_sound = {
    '.': 'dot.ogg',
    '-': 'dash.ogg',
    ' ': 'short_silence.ogg',
    '*': 'very_short_silence.ogg',
    '|': 'long_silence.ogg',
}

pygame.init()
pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 296)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))

        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(56, 60, 74);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 120, 121, 28))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.TextToMorse)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 120, 141, 28))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.playSoundMain)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 461, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 180, 461, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Morse converter"))
        self.pushButton.setText(_translate("MainWindow", "Morse хувиргах"))
        self.pushButton_2.setText(_translate("MainWindow", "Дуут дохио болгох"))

    def TextToMorse(self):
        text, cipher = self.textEdit.toPlainText().lower(), ''
        for letter in text: 
            if letter.upper() != ' ':  cipher += morsetab[letter] + ' '
            else: cipher += ' '
        self.textEdit_2.document().setPlainText(cipher)
    def playSoundMain(self):
        self.textEdit_2.document().setPlainText('Playing audio please wait')
        convert_string = self.textEdit.toPlainText().lower()
        self.decoded = self.string_to_code(convert_string)
        self.play_morse_sound(self.code_to_sound_code(self.decoded))
        self.textEdit_2.document().setPlainText(self.decoded)

    def playsound(self, soundfile):
        """Play sound through default mixer channel in blocking manner.
        This will load the whole sound into memory before playback
        """
        sound = pygame.mixer.Sound(soundfile)
        clock = pygame.time.Clock()
        sound.play()
        while pygame.mixer.get_busy():
            clock.tick(FRAMERATE)

    def play_morse_sound(self, code):
        for channel_id, dip in enumerate(code):
            try:
                sound = pygame.mixer.Sound(morse_sound[dip])
            except KeyError:
                sound = pygame.mixer.Sound(morse_sound[' '])
            self.playsound(sound)


    def code_to_sound_code(self, code):
        res = code.replace('..', '.*.').replace('--', '-*-').replace('.-', '.*-').replace('-.', '-*.').replace('..', '.*.').replace('--', '-*-').replace('.-', '.*-').replace('-.', '-*.')
        return res

    def string_to_code(self, convert_string):
        res = ''
        for c in convert_string:
            try:
                res += morsetab[c]
            except KeyError:
                pass
        return res

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
