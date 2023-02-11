'''
Main python file for tab_edit UI version
Run this file to execute the GUI
'''
from PyQt5 import QtCore, QtGui, QtWidgets
import style_sheets as style
import qt_widgets as qt
import ui_backend
import os

class Ui_main_window(object):
    def setupUi(self, main_window):

#MAIN WINDOW WIDGETS:
        main_window.setObjectName("main_window")
        main_window.resize(950, 754)


        self.main_widget = QtWidgets.QWidget(main_window)
        self.main_widget.setStyleSheet(
                style.MAIN_WINDOW
        )
        self.main_widget.setObjectName("main_widget")


        self.tab_group = qt.create_tab_group(self.main_widget,20,10,451,731,style.TAB_GROUP,"tab_group")


# IMAGE_OUTPUT GROUP
# ---------------------------------------------------------------------------------------------------------------------------------------------

        self.image_graphics_group = qt.create_groupBox(self.main_widget, 480, 34, 445, 707, style.IMAGE_GRAPHICS_GROUP, "image_graphics_group")

        self.ARO_image_group = qt.create_groupBox(self.image_graphics_group, 20, 32, 401, 301, style.ARO_IMAGE_GROUP, "ARO_image_group")

        self.MCC_image_group = qt.create_groupBox(self.image_graphics_group, 20, 372, 401, 301, style.MCC_IMAGE_GROUP, "MCC_image_group")

        self.ARO_map_graphics = qt.create_graphicsView(self.ARO_image_group, 20, 20, 361, 261, style.ARO_MAP_GRAPHICS, "ARO_map_graphics")

        self.MCC_map_graphics = qt.create_graphicsView(self.MCC_image_group, 20, 20, 361, 261, style.MCC_MAP_GRAPHICS, "MCC_map_graphics")

# -----------------------------------------------------------------------------------------------------------------------------------------------

#ARO TAB WIDGETS:
#-------------------------------------------------------------------------------------------------------------------------------------------------
        self.ARO_tab = QtWidgets.QWidget()
        self.ARO_tab.setStyleSheet(
                style.ARO_TAB
        )
        self.ARO_tab.setObjectName("ARO_tab")


        #ARO INPUT WIDGETS
        #------------------------------------------------------------------------------
        self.ARO_input_group = qt.create_groupBox(self.ARO_tab,10,20,421,211,style.ARO_INPUT_GROUP,"ARO_input_group")

        self.cmd_label = qt.create_label(self.ARO_input_group,170,30,91,16,style.CMD_LABEL,"COMMAND","cmd_label")

        self.cmd_input = qt.create_line_edit(self.ARO_input_group,70,50,261,31,style.CMD_INPUT,"cmd_input")

        self.pass_label = qt.create_label(self.ARO_input_group,170,100,81,16,style.PASS_LABEL,"PASSWORD","pass_label")

        self.pass_input = qt.create_line_edit(self.ARO_input_group,70,120,261,31,style.PASS_INPUT,"pass_input")

        self.pass_submit = qt.create_pushButton(self.ARO_input_group,160,160,93,28,style.PASS_SUBMIT,"SUBMIT","pass_submit")

        self.pass_submit.clicked.connect(lambda: ui_backend.submit_pressed(self.cmd_input.text(), self.pass_input.text()))
        #------------------------------------------------------------------------------


        #ARO_OUTPUT WIDGETS
        #-------------------------------------------------------------------------------
        self.ARO_output = qt.create_groupBox(self.ARO_tab,10,260,421,431,style.ARO_OUTPUT,"ARO_output")

        self.cmd_history_label = qt.create_label(self.ARO_output,20,40,141,16,style.CMD_HISTORY_LABEL,"COMMAND HISTORY","cmd_history_label")

        self.serial_ouput_label = qt.create_label(self.ARO_output,20,230,111,16,style.SERIAL_OUTPUT_LABEL,"SERIAL OUTPUT","serial_output_label")

        self.cmd_history_scrollArea = qt.create_scrollArea(self.ARO_output,20,60,381,151,style.CMD_HISTORY_SCROLLAREA,"cmd_history_scrollArea")

        self.cmd_history_content = QtWidgets.QWidget()
        self.cmd_history_content.setGeometry(QtCore.QRect(0, 0, 377, 147))
        self.cmd_history_content.setObjectName("cmd_history_content")

        self.cmd_history_scrollBar = qt.create_scrollBar(self.cmd_history_content,360,0,21,151,style.CMD_HISTORY_SCROLLBAR,"cmd_history_scrollBar")

        self.cmd_history_scrollArea.setWidget(self.cmd_history_content)

        self.serial_output_scrollArea = qt.create_scrollArea(self.ARO_output,20,250,381,161,style.SERIAL_OUTPUT_SCROLLAREA,"serial_output_scrollArea")

        self.serial_content = QtWidgets.QWidget()
        self.serial_content.setGeometry(QtCore.QRect(0, 0, 377, 157))
        self.serial_content.setObjectName("serial_content")

        self.serial_scrollBar = qt.create_scrollBar(self.serial_content,360,0,21,161,style.SERIAL_OUPUT_SCROLLBAR,"serial_scrollBar")

        self.serial_output_scrollArea.setWidget(self.serial_content)

        self.output_label = qt.create_label(self.ARO_output,180,20,61,16,style.OUTPUT_LABEL,"OUTPUT","output_label")
        #-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------

        self.tab_group.addTab(self.ARO_tab, "")

#MCC TAB WIDGETS
#-------------------------------------------------------------------------------------------------------------------------------------------
        self.MCC_tab = QtWidgets.QWidget()
        self.MCC_tab.setObjectName("MCC_tab")


        self.sat_selfie_group = qt.create_groupBox(self.MCC_tab,20,30,401,301,style.SAT_SELFIE_GROUP,"sat_selfie_group")

        self.sat_graphics_view = qt.create_graphicsView(self.sat_selfie_group,20,20,361,261,style.SAT_SELFIE_GRAPHIC,"sat_graphics_view")

        self.telemetry_group = qt.create_groupBox(self.MCC_tab,20,370,401,301,style.TELEMETRY_GROUP,"telemetry_group")

        self.telemetry_view = qt.create_graphicsView(self.telemetry_group,20,20,361,261,style.TELEMETRY_GRAPHIC,"telemetry_view")

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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())