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
        self.ARO_label = create_label(self, 10, 0, 31, 31, "ARO", "ARO_Label")

        #create and position "MCC" Label in UI
        self.MCC_label = create_label(self, 420, 10, 31, 20, "MCC", "MCC_Label")


        #COMMAND 1 WIDGETS:
        #-----------------------------------------------------------------------------
        #create and position "Command 1" Label in UI
        self.cmd1_label = create_label(self, 10, 30, 91, 16, "Command 1", "cmd1_label")

        #create plain text input box under Command 1 label
        self.cmd1_plainTextEdit = create_plain_text_edit(self, 10, 230, 261, 31, "cmd1_plainTextEdit")

        #create and position Command 1 "Run" checkbox in UI
        self.cmd1_checkBox = create_checkBox(self, 90, 30, 81, 20, "Run", "cmd1_checkbox")

        #create and position command 1 progress bar 
        self.cmd1_progressBar = create_progressBar(self, 280, 50, 118, 31, "cmd3_progressBar")
        #------------------------------------------------------------------------------


        #COMMAND 2 WIDGETS:
        #------------------------------------------------------------------------------
        #create and position "Command 2" label in UI
        self.cmd2_label = create_label(self, 10, 90, 91, 16, "Command 2", "cmd2_label")

        #create plain text input box under Command 2 label
        self.cmd2_plainTextEdit = create_plain_text_edit(self, 10, 170, 261, 31, "cmd2_plainTextEdit")

        #create and position Command 2 "Run" checkbox in UI
        self.cmd2_checkBox = create_checkBox(self, 90, 90, 81, 20, "Run", "cmd2_checkBox")

        #create and position command 2 progress bar 
        self.cmd2_progressBar = create_progressBar(self, 280, 110, 118, 31, "cmd2_progressBar")
        #------------------------------------------------------------------------------


        #COMMAND 3 WIDGETS:
        #------------------------------------------------------------------------------
        #create and position "Command 3" Label in UI
        self.cmd3_label = create_label(self, 10, 150, 91, 16, "Command 3", "cmd3_label")

        #create plain text input box under Command 3 label
        self.cmd3_plainTextEdit = create_plain_text_edit(self, 10, 110, 261, 31, "cmd3_plainTextEdit")

        #create and position Command 3 "Run" checkbox in UI
        self.cmd3_checkBox = create_checkBox(self, 90, 150, 81, 20, "Run", "cmd3_checkBox")

        #create and position command 3 progress bar 
        self.cmd3_progressBar = create_progressBar(self, 280, 170, 118, 31, "cmd3_progressBar")
        #------------------------------------------------------------------------------


        #COMMAND 4 WIDGETS:
        #------------------------------------------------------------------------------
        #create and position "Command 4" Label in UI
        self.cmd4_label = create_label(self, 10, 210, 91, 16, "Command 4", "cmd4_label")

        #create plain text input box under Command 4 label
        self.cmd4_plainTextEdit = create_plain_text_edit(self, 10, 50, 261, 31, "plainTextEdit_4")

        #create and position Command 4 "Run" checkbox in UI
        self.cmd4_checkBox = create_checkBox(self, 90, 210, 81, 20, "Run", "cmd4_checkBox")

        #create and position command 4 progress bar 
        self.cmd4_progressBar = create_progressBar(self, 280, 230, 118, 31, "cmd4_progressBar")
        #------------------------------------------------------------------------------


        #PASSWORD I/O WIDGETS
        #------------------------------------------------------------------------------
        #create and position "PASSWORD" label
        self.password_label = create_label(self, 10, 280, 91, 16, "PASSWORD:", "password_label")

        #create and position password plain text input
        self.password_plainTextEdit = create_plain_text_edit(self, 10, 300, 261, 31, "password_input")

        #create and position password authentication visual (ARO)
        self.password_graphicsView = create_graphicsView(self, 420, 50, 361, 231, "password_graphicsView")

        #create and position password submit push button
        self.pass_pushButton = create_pushButton(self, 100, 340, 93, 28, "SUBMIT", "pass_pushButton")
        #------------------------------------------------------------------------------


        #position horizontal line under command password input
        self.horiz_line = create_horizLine(self, 0, 370, 401, 20, "line")


        #COMMAND HISTORY AND SERIAL OUTPUT WIDGETS
        #------------------------------------------------------------------------------
        #create and position "Command History" label for scroll area
        self.cmd_history_label = create_label(self, 10, 380, 111, 16, "Command History", "cmd_history_label")

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
        self.serial_out_label = create_label(self, 10, 460, 111, 16, "Serial Output", "serial_out_label")

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
        self.sat_selfie_label = create_label(self, 570, 30, 61, 16, "Sat Selfie", "selfie_sat_label")

        #create and position MCC "Selfie Sat" graphics view
        self.selfie_graphicsView = create_graphicsView(self, 310, 300, 31, 31, "selfie_sat_graphics")

        #create and position "Map" label (MCC)
        self.map_label = create_label(self, 590, 290, 31, 16, "Map", "map_label")

        #create and position "Map" graphics view (MCC)
        self.map_graphicsView = create_graphicsView(self, 420, 311, 361, 231, "map_graphicsView")
        #------------------------------------------------------------------------------
        
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

def create_label(self,left,top,width,height,label_name,obj_name=""):
    '''
        breif : creates label onto main window at coordinates (left, top, width, height) with specified label name
        param : 
                left - int coordinate pixels from left side of main window
                top - int coordinate pixels from top side of main window
                width - int width of label widget in pixels
                height - int height of label widget in pixels
                label_name - String label name (what shows up as label on GUI)
                obj_name - String internal object name 
        return : pyQt label object
    '''
    label = QtWidgets.QLabel(self.centralwidget)
    label.setGeometry(QtCore.QRect(left,top,width,height))
    label.setObjectName(obj_name)
    label.setText(QtCore.QCoreApplication.translate("main_window", label_name))
    return label

def create_plain_text_edit(self,left,top,width,height,obj_name=""):
    '''
        breif : creates plain text input onto main window at coordinates (left, top, width, height)
        param : 
                left - int coordinate pixels from left side of main window
                top - int coordinate pixels from top side of main window
                width - int width of widget in pixels
                height - int height of widget in pixels
                obj_name - String internal object name 
        return : pyQt plain text edit input object
    '''
    text_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
    text_edit.setGeometry(QtCore.QRect(left,top,width,height))
    text_edit.setObjectName(obj_name)
    return text_edit

def create_checkBox(self,left,top,width,height,checkBox_name,obj_name=""):
    '''
        breif : creates check box input onto main window at coordinates (left, top, width, height)
        param : 
                left - int coordinate pixels from left side of main window
                top - int coordinate pixels from top side of main window
                width - int width of widget in pixels
                height - int height of widget in pixels
                obj_name - String internal object name 
        return : pyQt check box input object
    '''
    check_box = QtWidgets.QCheckBox(self.centralwidget)
    check_box.setGeometry(QtCore.QRect(left,top,width,height))
    check_box.setObjectName(obj_name)
    check_box.setText(QtCore.QCoreApplication.translate("main_window", checkBox_name))
    return check_box

def create_progressBar(self,left,top,width,height,obj_name=""):
    '''
        breif : creates progress bar onto main window at coordinates (left, top, width, height)
        param : 
                left - int coordinate pixels from left side of main window
                top - int coordinate pixels from top side of main window
                width - int width of widget in pixels
                height - int height of widget in pixels
                obj_name - String internal object name 
        return : pyQt progress bar object
    '''
    progress_bar = QtWidgets.QProgressBar(self.centralwidget)
    progress_bar.setGeometry(QtCore.QRect(left,top,width,height))
    progress_bar.setProperty("value", 24)
    progress_bar.setObjectName(obj_name)
    return progress_bar

def create_graphicsView(self,left,top,width,height,obj_name=""):
    '''
        breif : creates graphics output onto main window at coordinates (left, top, width, height)
        param : 
                left - int coordinate pixels from left side of main window
                top - int coordinate pixels from top side of main window
                width - int width of widget in pixels
                height - int height of widget in pixels
                obj_name - String internal object name 
        return : pyQt graphics View object
    '''
    graphic = QtWidgets.QGraphicsView(self.centralwidget)
    graphic.setGeometry(QtCore.QRect(left,top,width,height))
    graphic.setObjectName(obj_name)
    return graphic

def create_pushButton(self,left,top,width,height,button_name,obj_name=""):
    '''
        breif : creates button input onto main window at coordinates (left, top, width, height)
        param : 
                left - int coordinate pixels from left side of main window
                top - int coordinate pixels from top side of main window
                width - int width of widget in pixels
                height - int height of widget in pixels
                button_name - String text presented on button
                obj_name - String internal object name 
        return : pyQt button input object
    '''
    button = QtWidgets.QPushButton(self.centralwidget)
    button.setGeometry(QtCore.QRect(left,top,width,height))
    button.setObjectName(obj_name)
    button.setText(QtCore.QCoreApplication.translate("main_window", button_name))
    return button

def create_horizLine(self,left,top,width,height,obj_name=""):
    '''
        breif : creates horizontal line onto main window at coordinates (left, top, width, height)
        param : 
                left - int coordinate pixels from left side of main window
                top - int coordinate pixels from top side of main window
                width - int width of widget in pixels
                height - int height of widget in pixels
                obj_name - String internal object name 
        return : pyQt horizontal line object
    '''
    horiz_line = QtWidgets.QFrame(self.centralwidget)
    horiz_line.setGeometry(QtCore.QRect(left,top,width,height))
    horiz_line.setFrameShape(QtWidgets.QFrame.HLine)
    horiz_line.setFrameShadow(QtWidgets.QFrame.Sunken)
    horiz_line.setObjectName(obj_name)
    return horiz_line

if __name__ == "__main__":
    ''' 
        Create main window here
    '''
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
