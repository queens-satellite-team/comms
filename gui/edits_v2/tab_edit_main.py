'''
Main python file for tab_edit UI version
Run this file to execute the GUI
'''
from PyQt5 import QtCore, QtGui, QtWidgets
import style_sheets as style
import ui_backend
import os


class Ui_main_window(object):
    def setupUi(self, main_window):

#MAIN WINDOW WIDGETS:
        main_window.setObjectName("main_window")
        main_window.resize(489, 780)


        self.main_widget = QtWidgets.QWidget(main_window)
        self.main_widget.setStyleSheet(
                style.MAIN_WINDOW
        )
        self.main_widget.setObjectName("main_widget")


        self.tab_group = create_tab_group(self.main_widget,20,10,451,731,style.TAB_GROUP,"tab_group")

#ARO TAB WIDGETS:
#-------------------------------------------------------------------------------------------------------------------------------------------------
        self.ARO_tab = QtWidgets.QWidget()
        self.ARO_tab.setStyleSheet(
                style.ARO_TAB
        )
        self.ARO_tab.setObjectName("ARO_tab")


        #ARO INPUT WIDGETS
        #------------------------------------------------------------------------------
        self.ARO_input_group = create_groupBox(self.ARO_tab,10,20,421,211,style.ARO_INPUT_GROUP,"ARO_input_group")

        self.cmd_label = create_label(self.ARO_input_group,170,30,91,16,style.CMD_LABEL,"COMMAND","cmd_label")

        self.cmd_input = create_line_edit(self.ARO_input_group,70,50,261,31,style.CMD_INPUT,"cmd_input")

        self.pass_label = create_label(self.ARO_input_group,170,100,91,16,style.PASS_LABEL,"PASSWORD","pass_label")

        self.pass_input = create_line_edit(self.ARO_input_group,70,120,261,31,style.PASS_INPUT,"pass_input")

        self.pass_submit = create_pushButton(self.ARO_input_group,160,160,93,28,style.PASS_SUBMIT,"SUBMIT","pass_submit")
        self.pass_submit.clicked.connect(lambda: ui_backend.submit_pressed(self.cmd_input.text(), self.pass_input.text())) # calls submit_pressed when submit button is pressed
        
        #------------------------------------------------------------------------------


        #ARO_OUTPUT WIDGETS
        #-------------------------------------------------------------------------------
        self.ARO_output = create_groupBox(self.ARO_tab,10,260,421,431,style.ARO_OUTPUT,"ARO_output")

        self.cmd_history_label = create_label(self.ARO_output,20,40,141,16,style.CMD_HISTORY_LABEL,"COMMAND HISTORY","cmd_history_label")

        self.serial_ouput_label = create_label(self.ARO_output,20,230,111,16,style.SERIAL_OUTPUT_LABEL,"SERIAL OUTPUT","serial_output_label")

        self.cmd_history_scrollArea = create_scrollArea(self.ARO_output,20,60,381,151,style.CMD_HISTORY_SCROLLAREA,"cmd_history_scrollArea")

        self.cmd_history_content = QtWidgets.QWidget()
        self.cmd_history_content.setGeometry(QtCore.QRect(0, 0, 377, 147))
        self.cmd_history_content.setObjectName("cmd_history_content")

        self.cmd_history_scrollBar = create_scrollBar(self.cmd_history_content,360,0,21,151,style.CMD_HISTORY_SCROLLBAR,"cmd_history_scrollBar")

        self.cmd_history_scrollArea.setWidget(self.cmd_history_content)

        self.serial_output_scrollArea = create_scrollArea(self.ARO_output,20,250,381,161,style.SERIAL_OUTPUT_SCROLLAREA,"serial_output_scrollArea")

        self.serial_content = QtWidgets.QWidget()
        self.serial_content.setGeometry(QtCore.QRect(0, 0, 377, 157))
        self.serial_content.setObjectName("serial_content")

        self.serial_scrollBar = create_scrollBar(self.serial_content,360,0,21,161,style.SERIAL_OUPUT_SCROLLBAR,"serial_scrollBar")

        self.serial_output_scrollArea.setWidget(self.serial_content)

        self.output_label = create_label(self.ARO_output,180,20,61,16,style.OUTPUT_LABEL,"OUTPUT","output_label")
        #-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------

        self.tab_group.addTab(self.ARO_tab, "")

#MCC TAB WIDGETS
#-------------------------------------------------------------------------------------------------------------------------------------------
        self.MCC_tab = QtWidgets.QWidget()
        self.MCC_tab.setObjectName("MCC_tab")


        self.sat_selfie_group = create_groupBox(self.MCC_tab,20,30,401,301,style.SAT_SELFIE_GROUP,"sat_selfie_group")

        self.sat_graphics_view = create_graphicsView(self.sat_selfie_group,20,20,361,261,style.SAT_SELFIE_GRAPHIC,"sat_graphics_view")

        self.telemetry_group = create_groupBox(self.MCC_tab,20,370,401,301,style.TELEMETRY_GROUP,"telemetry_group")

        self.telemetry_view = create_graphicsView(self.telemetry_group,20,20,361,261,style.TELEMETRY_GRAPHIC,"telemetry_view")

        self.tab_group.addTab(self.MCC_tab, "")
#-------------------------------------------------------------------------------------------------------------------------------------------

        main_window.setCentralWidget(self.main_widget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 26))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)

        self.retranslateUi(main_window)
        self.tab_group.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        #create main window title
        main_window.setWindowTitle(QtCore.QCoreApplication.translate("main_window", "QSET Comms"))

        #create qset program icon here
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        main_window.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'qset.jpg'))

        #show tab titles here
        self.tab_group.setTabText(self.tab_group.indexOf(self.ARO_tab), QtCore.QCoreApplication.translate("main_window", "ARO"))
        self.tab_group.setTabText(self.tab_group.indexOf(self.MCC_tab), QtCore.QCoreApplication.translate("main_window", "MCC"))



def create_tab_group(parent_widget,left,top,width,height,stylesheet="",obj_name=""):
        '''
        brief : creates tab group object onto parent widget
        param :
                parent_widget - the parent widget to the current object (where this widget is placed)\n
                left - int coordinate pixels from left side of parent window\n 
                top - int coordinate pixels from top side of parent window\n 
                width - int width of widget in pixels\n 
                height - int height of widget in pixels\n 
                str_stylesheet - str description of widget style\n 
                obj_name - String internal object name\n 
        return : pyQt tabGroup object
                 
        '''
        tab_group = QtWidgets.QTabWidget(parent_widget)
        tab_group.setGeometry(QtCore.QRect(left,top,width,height))
        tab_group.setStyleSheet(stylesheet)     
        tab_group.setObjectName(obj_name)
        return tab_group

def create_label(parent_widget,left,top,width,height,stylesheet="",label_name="",obj_name=""):
        '''
        brief : creates label object at coordinates (left, top, width, height) on specified parent_widget
        param : 
                parent_widget - the parent widget to the current object (where this widget is placed)\n 
                left - int coordinate pixels from left side of parent widget\n 
                top - int coordinate pixels from top side of parent widget\n 
                width - int width of widget in pixels\n 
                height - int height of widget in pixels\n 
                str_stylesheet - str description of widget style\n 
                label_name - String label name (what shows up as label on GUI)\n 
                obj_name - String internal object name\n 
        return : pyQt label object
        '''
        label = QtWidgets.QLabel(parent_widget)
        label.setGeometry(QtCore.QRect(left,top,width,height))
        label.setStyleSheet(stylesheet)  
        label.setText(QtCore.QCoreApplication.translate("main_window", label_name))
        label.setObjectName(obj_name)
        return label

def create_groupBox(parent_widget,left,top,width,height,stylesheet="",obj_name=""):
        '''
        brief : creates groupBox object at coordinates (left, top, width, height) with specified obj name
        param : 
                parent_widget - the parent widget to the current object (where this widget is placed)\n
                left - int coordinate pixels from left side of parent widget\n
                top - int coordinate pixels from top side of parent widget\n
                width - int width of widget in pixels\n
                height - int height of widget in pixels\n
                stylesheet - String description of widget style\n
                obj_name - String internal object name \n
        return : pyQt groupBox object
        '''
        groupBox = QtWidgets.QGroupBox(parent_widget)
        groupBox.setGeometry(QtCore.QRect(left, top, width, height))
        groupBox.setStyleSheet(stylesheet)
        groupBox.setObjectName(obj_name)
        return groupBox

def create_pushButton(parent_widget,left,top,width,height,stylesheet="",button_name="",obj_name=""):
        '''
        brief : creates button input onto specified widget at coordinates (left, top, width, height)
        param : 
                parent_widget - the parent widget to the current object (where this widget is placed)\n
                left - int coordinate pixels from left side of parent widget\n
                top - int coordinate pixels from top side of parent widget\n
                width - int width of widget in pixels\n
                height - int height of widget in pixels\n
                stylesheet - String style of widget\n
                button_name - String text presented on button\n
                obj_name - String internal object name\n 
        return : pyQt button input object
        '''
        button = QtWidgets.QPushButton(parent_widget)
        button.setGeometry(QtCore.QRect(left,top,width,height))
        button.setStyleSheet(stylesheet)
        button.setText(QtCore.QCoreApplication.translate("main_window", button_name))
        button.setObjectName(obj_name)
        return button

def create_graphicsView(parent_widget,left,top,width,height,stylesheet="",obj_name=""):
        '''
        brief : creates graphics output onto parent_widget at coordinates (left, top, width, height)
        param : 
                parent_widget - the parent widget to the current object (where this widget is placed)\n
                left - int coordinate pixels from left side of main window\n
                top - int coordinate pixels from top side of main window\n
                width - int width of widget in pixels\n
                height - int height of widget in pixels\n
                stylesheet - String style of widget\n
                obj_name - String internal object name\n 
        return : pyQt graphics View object
        '''
        graphic = QtWidgets.QGraphicsView(parent_widget)
        graphic.setGeometry(QtCore.QRect(left,top,width,height))
        graphic.setStyleSheet(stylesheet)
        graphic.setObjectName(obj_name)
        return graphic

def create_line_edit(parent_widget,left,top,width,height,stylesheet="",obj_name=""):
        '''
        brief : creates line edit text input onto parent widget at coordinates (left, top, width, height)
        param : 
                parent_widget - the parent widget to the current object (where this widget is placed)\n
                left - int coordinate pixels from left side of parent widget\n
                top - int coordinate pixels from top side of parent widget\n
                width - int width of widget in pixels\n
                height - int height of widget in pixels\n
                stylesheet - String style of widget\n
                obj_name - String internal object name\n 
        return : pyQt line text edit input object
        '''
        text_edit = QtWidgets.QLineEdit(parent_widget)
        text_edit.setGeometry(QtCore.QRect(left,top,width,height))
        text_edit.setStyleSheet(stylesheet)
        text_edit.setObjectName(obj_name)
        return text_edit

def create_scrollArea(parent_widget,left,top,width,height,stylesheet="",obj_name=""):
        '''
        brief : creates scrollArea onto parent widget at coordinates (left, top, width, height)
        param : 
                parent_widget - the parent widget to the current object (where this widget is placed)\n
                left - int coordinate pixels from left side of parent widget\n
                top - int coordinate pixels from top side of parent widget\n
                width - int width of widget in pixels\n
                height - int height of widget in pixels\n
                stylesheet - String style of widget\n
                obj_name - String internal object name\n 
        return : pyQt scrollArea object
        '''
        scrollArea = QtWidgets.QScrollArea(parent_widget)
        scrollArea.setGeometry(QtCore.QRect(left,top,width,height))
        scrollArea.setStyleSheet(stylesheet)
        scrollArea.setObjectName(obj_name)
        return scrollArea

def create_scrollBar(parent_widget,left,top,width,height,stylesheet="",obj_name=""):
        '''
        brief : creates vertical scrollBar onto parent widget at coordinates (left, top, width, height)
        param : 
                parent_widget - the parent widget to the current object (where this widget is placed)\n
                left - int coordinate pixels from left side of parent widget\n
                top - int coordinate pixels from top side of parent widget\n
                width - int width of widget in pixels\n
                height - int height of widget in pixels\n
                stylesheet - String style of widget\n
                obj_name - String internal object name\n 
        return : pyQt vertical scrollBar object
        '''
        scrollBar = QtWidgets.QScrollBar(parent_widget)
        scrollBar.setGeometry(QtCore.QRect(left,top,width,height))
        scrollBar.setStyleSheet(stylesheet)
        scrollBar.setOrientation(QtCore.Qt.Vertical)
        scrollBar.setObjectName(obj_name)
        return scrollBar

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
