'''
Multithreaded TCP Server - Nishant Thakur
University of Texas at Arlington - UID: 1001544591
Studied socket programming from YouTube. Sendex tutorial for socket programming.
Studied PyQt GUI development from YouTube. Sendex tutorial for PyQt GUI development.
Studied Thread in Qt from the official PyQt documentation.
'''

from queue import Queue
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QThread
from PyQt5.QtGui import QTextCursor

import ServerGUI
import sys, os

'''
This is the main class from where the GUI starts.
When the object of the main class is initiated the GUI is rendered in the memory.
Thread to handel multiple connection are initiated in this class.
'''
class MainUiClass(QtWidgets.QMainWindow, ServerGUI.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)
        self.host.setText(host)
        self.port.setText(str(port))
        self.startServer.clicked.connect(self.connectClients)

    # function is called when the 'Start' button is pressed.
    def connectClients(self):
        self.thread = QThread()
        self.long_running_thing = AcceptConnections()
        self.long_running_thing.moveToThread(self.thread)
        self.thread.started.connect(self.long_running_thing.run)
        self.thread.start()
        self.logs.setText("Waiting for connection! \n")

    # appending the logs to the QTextBrowser with the following function.
    @pyqtSlot(str)
    def append_text(self,text):
        self.logs.moveCursor(QTextCursor.End)
        self.logs.insertPlainText(text)

#######################################################################################
#this classes are use to redirect all the sys.stdout to the PyQt QTextBrowser Widget
#from StackOverFlow : https://stackoverflow.com/questions/21071448/redirecting-stdout-and-stderr-to-a-pyqt4-qtextedit-from-a-secondary-thread
class WriteStream(object):
    def __init__(self,queue):
        self.queue = queue
    def write(self, text):
        self.queue.put(text)


class MessageBox(QObject):
    cmd_signal = pyqtSignal(str)

    def __init__(self,queue,*args,**kwargs):
        QObject.__init__(self,*args,**kwargs)
        self.queue = queue

    @pyqtSlot()
    def run(self):
        while True:
            text = self.queue.get()
            self.cmd_signal.emit(text)
#######################################################################################

#Thread for each client is in the following class
class ClientThread(QObject):
    def __init__(self, conn, *args, **kwargs):
        QObject.__init__(self, *args, **kwargs)
        self.conn = conn

    @pyqtSlot()
    def run(self):
        while True:
            data = self.conn.recv(2048)
            if not data:
                break
            word = data.decode('utf-8')
            try:
                reply = str(dictionary[word])
                text = 'Client requested word: ' + str(word)
                print(text)

            except KeyError:
                reply = ('Word not available in dictionary')
                print(reply)

            self.conn.sendall(str.encode(reply))
        self.conn.close()

#thread for accepting the clients continiously is in the following class
class AcceptConnections(QObject):
    @pyqtSlot()
    def run(self):
        while True:
            conn, addr = s.accept()
            print('connected to: ' + addr[0] + ':' + str(addr[1]))
            self.thread = QThread()
            self.my_receiver = ClientThread(conn)
            self.my_receiver.moveToThread(self.thread)
            self.thread.started.connect(self.my_receiver.run)
            self.thread.start()

#initiatization of the program starts here
if __name__ == '__main__':

    import socket
    from _thread import *
    import ast

    host = '127.0.0.1'
    port = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(s)
    #bind the socket to the specified host and port.
    try:
        s.bind((host, port))
    except socket.error as e:
        print(str(e))

    #number of valid connection allowed at a given time
    s.listen(5)

    #save the dictionary file in a variable
    with open('my-thesaurus.txt') as f:
        lines = f.readlines()
    dictionary = ast.literal_eval(lines[0])

    # Create Queue and redirect sys.stdout to this queue
    queue = Queue()
    sys.stdout = WriteStream(queue)

    a = QtWidgets.QApplication(sys.argv)
    app = MainUiClass()
    app.show()

    thread = QThread()
    msg_receiver = MessageBox(queue)
    msg_receiver.cmd_signal.connect(app.append_text)
    msg_receiver.moveToThread(thread)
    thread.started.connect(msg_receiver.run)
    thread.start()

    a.exec_()
