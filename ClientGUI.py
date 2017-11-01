'''
TCP Client - Nishant Thakur
University of Texas at Arlington - UID: 1001544591
Studied socket programming from YouTube. Sendex tutorial for socket programming.
Studied PyQt GUI development from YouTube. Sendex tutorial for PyQt GUI development.
'''
from PyQt5 import QtCore, QtGui, QtWidgets

#class where the GUI is designed and program logic is initiated.
class Ui_ClientDialog(object):
    #function to make GUI
    def setupUi(self, ClientDialog):
        ClientDialog.setObjectName("ClientDialog")
        ClientDialog.resize(380, 212)

        self.userWord = QtWidgets.QLineEdit(ClientDialog)
        self.userWord.setGeometry(QtCore.QRect(60, 30, 211, 21))
        self.userWord.setInputMask("")
        self.userWord.setObjectName("userWord")

        self.searchWord = QtWidgets.QPushButton(ClientDialog)
        self.searchWord.setGeometry(QtCore.QRect(280, 30, 75, 21))
        self.searchWord.setObjectName("searchWord")
        self.searchWord.clicked.connect(self.requestWord)

        self.label = QtWidgets.QLabel(ClientDialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 46, 21))
        self.label.setObjectName("label")

        self.wordSynonyms = QtWidgets.QTextBrowser(ClientDialog)
        self.wordSynonyms.setGeometry(QtCore.QRect(90, 70, 261, 81))
        self.wordSynonyms.setObjectName("wordSynonyms")

        self.label_2 = QtWidgets.QLabel(ClientDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 61, 16))
        self.label_2.setObjectName("label_2")

        self.exit = QtWidgets.QPushButton(ClientDialog)
        self.exit.setGeometry(QtCore.QRect(100, 170, 75, 23))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.cleartxt = QtWidgets.QPushButton(ClientDialog)
        self.cleartxt.setGeometry(QtCore.QRect(180, 170, 75, 23))
        self.cleartxt.setObjectName("exit")
        self.cleartxt.clicked.connect(self.clearTXT)

        self.retranslateUi(ClientDialog)
        QtCore.QMetaObject.connectSlotsByName(ClientDialog)

    #changing names of the labels and objects in GUI with this function
    def retranslateUi(self, ClientDialog):
        _translate = QtCore.QCoreApplication.translate
        ClientDialog.setWindowTitle(_translate("ClientDialog", "ClientGUI"))
        self.userWord.setPlaceholderText(_translate("ClientDialog", "Enter a word!"))
        self.searchWord.setText(_translate("ClientDialog", "Search"))
        self.label.setText(_translate("ClientDialog", "Word:"))
        self.label_2.setText(_translate("ClientDialog", "Synonyms:"))
        self.exit.setText(_translate("ClientDialog", "Exit"))
        self.cleartxt.setText(_translate("ClientDialog", "Clear"))

    #logic for clearing the search box and Synonyms box
    def clearTXT(self):
        self.userWord.setText("")
        self.wordSynonyms.setText("")

    #function to request the synonyms of word from the Server
    def requestWord(self):
        # print("hello word search clicked!!")
        word = self.userWord.text()
        if len(word) == 0:
            print("Please enter a word!")
        else:
            s.send(str.encode(word))
            # Receive no more than 1024 bytes
            tm = s.recv(1024)
            print(tm.decode("utf-8"))
            self.wordSynonyms.setText(tm.decode("utf-8"))

    #function to append the response of the server to the Synonyms text box
    def append_text(self, text):
        self.logs.append(text)

#program execution starts here
if __name__ == "__main__":
    import sys
    import socket

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 8888

    # connection to host on the port.
    s.connect((host, port))
    # print(s.recv(1024))

    app = QtWidgets.QApplication(sys.argv)
    ClientDialog = QtWidgets.QDialog()

    ui = Ui_ClientDialog()
    ui.setupUi(ClientDialog)
    ClientDialog.show()
    sys.exit(app.exec_())
