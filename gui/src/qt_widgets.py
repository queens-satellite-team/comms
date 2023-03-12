from PyQt5 import QtCore, QtGui, QtWidgets



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

def create_line_edit(parent_widget,left,top,width,height,stylesheet="",obj_name="",is_password=False):
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
                is_password - boolean value, true if line edit widget is a passowrd (text is hidden)\n
        return : pyQt line text edit input object
        '''
        text_edit = QtWidgets.QLineEdit(parent_widget)
        if is_password:
                text_edit.setEchoMode(QtWidgets.QLineEdit.Password)
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