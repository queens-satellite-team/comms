# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# Documented code creating front end UI (to be continued)

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        
        #set main window object name and size
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)

        #main window widget init and called "central widget"
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        #create and position "ARO" label in UI
        self.ARO_label = QtWidgets.QLabel(self.centralwidget)
        self.ARO_label.setGeometry(QtCore.QRect(10, 0, 31, 31))
        self.ARO_label.setObjectName("ARO_label")

        #create and position "MCC" Label in UI
        self.MCC_label = QtWidgets.QLabel(self.centralwidget)
        self.MCC_label.setGeometry(QtCore.QRect(420, 10, 31, 20))
        self.MCC_label.setObjectName("MCC_Label")


        #COMMAND 1 WIDGETS:
        #-----------------------------------------------------------------------------
        #create and position "Command 1" Label in UI
        self.command1_label = QtWidgets.QLabel(self.centralwidget)
        self.command1_label.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.command1_label.setObjectName("command1_label")

        #create plain text input box under Command 1 label
        self.command_plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.command_plainTextEdit.setGeometry(QtCore.QRect(10, 230, 261, 31))
        self.command_plainTextEdit.setObjectName("plainTextEdit")

        #create and position Command 1 "Run" checkbox in UI
        self.command1_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.command1_checkBox.setGeometry(QtCore.QRect(90, 30, 81, 20))
        self.command1_checkBox.setObjectName("command1_checkBox")

        #create and position command 1 progress bar 
        self.cmd1_progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.cmd1_progressBar.setGeometry(QtCore.QRect(280, 50, 118, 31))
        self.cmd1_progressBar.setProperty("value", 24)
        self.cmd1_progressBar.setObjectName("cmd1_progressBar")
        #------------------------------------------------------------------------------


        #COMMAND 2 WIDGETS:
        #------------------------------------------------------------------------------
        #create and position "Command 2" label in UI
        self.command2_label = QtWidgets.QLabel(self.centralwidget)
        self.command2_label.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.command2_label.setObjectName("command2_label")

        #create plain text input box under Command 2 label
        self.command_plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.command_plainTextEdit_2.setGeometry(QtCore.QRect(10, 170, 261, 31))
        self.command_plainTextEdit_2.setObjectName("plainTextEdit_2")

        #create and position Command 2 "Run" checkbox in UI
        self.command2_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.command2_checkBox.setGeometry(QtCore.QRect(90, 90, 81, 20))
        self.command2_checkBox.setObjectName("command2_checkBox")

        #create and position command 2 progress bar 
        self.cmd2_progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.cmd2_progressBar.setGeometry(QtCore.QRect(280, 110, 118, 31))
        self.cmd2_progressBar.setProperty("value", 24)
        self.cmd2_progressBar.setObjectName("cmd2_progressBar")
        #------------------------------------------------------------------------------


        #COMMAND 3 WIDGETS:
        #------------------------------------------------------------------------------
        #create and position "Command 3" Label in UI
        self.command3_label = QtWidgets.QLabel(self.centralwidget)
        self.command3_label.setGeometry(QtCore.QRect(10, 150, 91, 16))
        self.command3_label.setObjectName("command3_label")

        #create plain text input box under Command 3 label
        self.command_plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.command_plainTextEdit_3.setGeometry(QtCore.QRect(10, 110, 261, 31))
        self.command_plainTextEdit_3.setObjectName("plainTextEdit_3")

        #create and position Command 3 "Run" checkbox in UI
        self.command3_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.command3_checkBox.setGeometry(QtCore.QRect(90, 150, 81, 20))
        self.command3_checkBox.setObjectName("command3_checkBox")

        #create and position command 3 progress bar 
        self.cmd3_progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.cmd3_progressBar.setGeometry(QtCore.QRect(280, 170, 118, 31))
        self.cmd3_progressBar.setProperty("value", 24)
        self.cmd3_progressBar.setObjectName("cmd3_progressBar")
        #------------------------------------------------------------------------------


        #COMMAND 4 WIDGETS:
        #------------------------------------------------------------------------------
        #create and position "Command 4" Label in UI
        self.command4_label = QtWidgets.QLabel(self.centralwidget)
        self.command4_label.setGeometry(QtCore.QRect(10, 210, 91, 16))
        self.command4_label.setObjectName("command4_label")

        #create plain text input box under Command 4 label
        self.command_plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.command_plainTextEdit_4.setGeometry(QtCore.QRect(10, 50, 261, 31))
        self.command_plainTextEdit_4.setObjectName("plainTextEdit_4")

        #create and position Command 4 "Run" checkbox in UI
        self.command4_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.command4_checkBox.setGeometry(QtCore.QRect(90, 210, 81, 20))
        self.command4_checkBox.setObjectName("command4_checkBox")

        #create and position command 4 progress bar 
        self.cmd4_progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.cmd4_progressBar.setGeometry(QtCore.QRect(280, 230, 118, 31))
        self.cmd4_progressBar.setProperty("value", 24)
        self.cmd4_progressBar.setObjectName("cmd4_progressBar")
        #------------------------------------------------------------------------------


        #PASSWORD I/O WIDGETS
        #------------------------------------------------------------------------------
        #create and position "PASSWORD" label
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(10, 280, 91, 16))
        self.password_label.setObjectName("password_label")

        #create and position password plain text input
        self.password_plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.password_plainTextEdit.setGeometry(QtCore.QRect(10, 300, 261, 31))
        self.password_plainTextEdit.setObjectName("password_input")

        #create and position password authentication visual (ARO)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(420, 50, 361, 231))
        self.graphicsView_3.setObjectName("graphicsView_3")

        #create and position password submit push button
        self.pass_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pass_pushButton.setGeometry(QtCore.QRect(100, 340, 93, 28))
        self.pass_pushButton.setObjectName("pass_pushButton")
        #------------------------------------------------------------------------------


        #position horizontal line under command password input
        self.horiz_line = QtWidgets.QFrame(self.centralwidget)
        self.horiz_line.setGeometry(QtCore.QRect(0, 370, 401, 20))
        self.horiz_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.horiz_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horiz_line.setObjectName("line")


        #COMMAND HISTORY AND SERIAL OUTPUT WIDGETS
        #------------------------------------------------------------------------------
        #create and position "Command History" label for scroll area
        self.cmd_history_label = QtWidgets.QLabel(self.centralwidget)
        self.cmd_history_label.setGeometry(QtCore.QRect(10, 380, 111, 16))
        self.cmd_history_label.setObjectName("cmd_history_label")

        #create and position Command history scroll area and scroll bar
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 400, 371, 61))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 59))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(339, 0, 31, 81))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #create and position "Serial Output" label for scroll area
        self.serial_out_label = QtWidgets.QLabel(self.centralwidget)
        self.serial_out_label.setGeometry(QtCore.QRect(10, 460, 111, 16))
        self.serial_out_label.setObjectName("serial_out_label")

        #create and position Serial Output scroll area
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 480, 371, 61))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 369, 59))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(339, 0, 31, 81))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        #------------------------------------------------------------------------------


        #MCC SELFIE SAT AND MAP WIDGETS:
        #------------------------------------------------------------------------------
        #create and position "Sat Selfie" label (MCC)
        self.sat_selfie_label = QtWidgets.QLabel(self.centralwidget)
        self.sat_selfie_label.setGeometry(QtCore.QRect(570, 30, 61, 16))
        self.sat_selfie_label.setObjectName("sat_selfie_label")

        #create and position MCC "Selfie Sat" graphics view
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(310, 300, 31, 31))
        self.graphicsView.setObjectName("graphicsView")

        #create and position "Map" label (MCC)
        self.map_label = QtWidgets.QLabel(self.centralwidget)
        self.map_label.setGeometry(QtCore.QRect(590, 290, 31, 16))
        self.map_label.setObjectName("map_label")

        #create and position "Map" graphics view (MCC)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(420, 311, 361, 231))
        self.graphicsView_2.setObjectName("graphicsView_2")
        #------------------------------------------------------------------------------
        
        self.MCC_label.raise_()
        self.command1_label.raise_()
        self.command2_label.raise_()
        self.command3_label.raise_()
        self.command4_label.raise_()
        self.ARO_label.raise_()
        self.command_plainTextEdit.raise_()
        self.command_plainTextEdit_2.raise_()
        self.command_plainTextEdit_3.raise_()
        self.command_plainTextEdit_4.raise_()
        self.command1_checkBox.raise_()
        self.horiz_line.raise_()
        self.command2_checkBox.raise_()
        self.command3_checkBox.raise_()
        self.command4_checkBox.raise_()
        self.scrollArea.raise_()
        self.password_plainTextEdit.raise_()
        self.password_label.raise_()
        self.pass_pushButton.raise_()
        self.cmd1_progressBar.raise_()
        self.cmd2_progressBar.raise_()
        self.cmd3_progressBar.raise_()
        self.cmd4_progressBar.raise_()
        self.graphicsView.raise_()
        self.scrollArea_2.raise_()
        self.cmd_history_label.raise_()
        self.serial_out_label.raise_()
        self.graphicsView_2.raise_()
        self.map_label.raise_()
        self.graphicsView_3.raise_()
        self.sat_selfie_label.raise_()


        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.ARO_label.setText(_translate("main_window", "ARO"))
        self.MCC_label.setText(_translate("main_window", "MCC"))
        self.command1_label.setText(_translate("main_window", "Command 1"))
        self.command2_label.setText(_translate("main_window", "Command 2"))
        self.command3_label.setText(_translate("main_window", "Command 3"))
        self.command4_label.setText(_translate("main_window", "Command 4"))
        self.command1_checkBox.setText(_translate("main_window", "Run"))
        self.command2_checkBox.setText(_translate("main_window", "Run"))
        self.command3_checkBox.setText(_translate("main_window", "Run"))
        self.command4_checkBox.setText(_translate("main_window", "Run"))
        self.password_label.setText(_translate("main_window", "PASSWORD:"))
        self.pass_pushButton.setText(_translate("main_window", "SUBMIT"))
        self.cmd_history_label.setText(_translate("main_window", "Command History"))
        self.serial_out_label.setText(_translate("main_window", "Serial Output"))
        self.map_label.setText(_translate("main_window", "Map"))
        self.sat_selfie_label.setText(_translate("main_window", "Sat Selfie "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())