'''
GUI file generated using Qt Designer.
Some buttons were added by me manually.
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 330)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.label.setObjectName("label")

        self.logs = QtWidgets.QTextBrowser(Dialog)
        self.logs.setGeometry(QtCore.QRect(10, 90, 381, 231))
        self.logs.setObjectName("logs")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_2.setObjectName("label_2")

        self.host = QtWidgets.QTextBrowser(Dialog)
        self.host.setGeometry(QtCore.QRect(50, 10, 211, 21))
        self.host.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.host.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.host.setObjectName("host")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(270, 10, 41, 21))
        self.label_3.setObjectName("label_3")

        self.port = QtWidgets.QTextBrowser(Dialog)
        self.port.setGeometry(QtCore.QRect(310, 10, 81, 21))
        self.port.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.port.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.port.setObjectName("port")

        self.startServer = QtWidgets.QPushButton(Dialog)
        self.startServer.setGeometry(QtCore.QRect(155, 45, 75, 21))
        self.startServer.setObjectName("startServer")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "HOST:"))
        self.label_2.setText(_translate("Dialog", "System log:"))
        self.label_3.setText(_translate("Dialog", "PORT:"))
        self.startServer.setText(_translate("Dialog", "Start"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
