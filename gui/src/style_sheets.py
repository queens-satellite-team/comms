'''
    Python file containing UI style sheets for components
    Import into tab_edit_main.py
'''

MAIN_WINDOW = '''QWidget{background-color: rgb(26, 37, 48);}'''

TAB_GROUP = '''QTabBar::tab:selected {
                        color: rgb(255, 255, 255);
                        background-color: rgb(231, 76, 60);
                }
                QTabBar::tab:!selected {
                        color: rgb(255,255,255);
                        background-color: rgb(52, 73, 94);
                }
                QTabWidget:pane { /*replace icon text as pane ok....*/
                        font: 57 9pt \"Dubai Medium\";
                        border: 2px solid rgb(231, 76, 60);
                        border-radius: 5px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(26, 37, 48);
                }
                QTabBar::tab {
                        border: 2px solid rgb(231, 76, 60);
                        border-bottom-color:rgb(231, 76, 60);
                        height: 20px;
                        width: 70px;
                        background-color: rgb(231, 76, 60);
                }
                QTabWidget{
                        background-color: rgb(255,255,255);
                        font: 57 9pt \"Dubai Medium\";
                }
                QTabWidget::tab-bar {
                        left: 1px;
                        bottom: -1px;
                        background-color: rgb(255,255,255);
                }'''

ARO_TAB = '''QWidget{
                        background-color: rgb(26, 37, 48);
                        color: rgb(255, 255, 255);
                        border: 2px;
                    }'''

INPUT_GROUP = '''QGroupBox{
                        font: 57 8pt \"Dubai Medium\";
                        border: 2px solid rgb(26, 37, 48);
                        border-radius: 15px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(44, 62, 80);
                    }'''

PASS_SUBMIT = '''QPushButton{
                        font: 57 9pt \"Dubai Medium\";
                        border: 2px solid rgb(231, 76, 60);
                        border-radius: 12.5px;
                        padding-left: 5px;
                        padding-right: 5px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(231, 76, 60);
                    }'''

PASS_LABEL = '''font: 57 9pt \"Dubai Medium\";
                color: rgb(255, 255, 255);
                background-color: rgb(44, 62, 80);'''

PASS_INPUT = '''QLineEdit{
                        border: 2px solid rgb(26, 37, 48);
                        border-radius: 15px;
                        padding-left: 5px;
                        padding-right:5px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(26, 37, 48);
                    }'''

CALL_LABEL = '''font: 57 9pt \"Dubai Medium\";
                color: rgb(242, 242, 242);
                background-color: rgb(44, 62, 80);
                '''

CALL_INPUT = '''QLineEdit{
                        border: 2px solid rgb(26, 37, 48);
                        border-radius: 15px;
                        padding-left: 5px;
                        padding-right: 5px;
                        background-color:rgb(26, 37, 48);
                        color: rgb(255, 255, 255);
                    }'''

ARO_OUTPUT = '''QGroupBox{
                        font: 57 8pt \"Dubai Medium\";
                        border: 2px solid rgb(26, 37, 48);
                        border-radius: 15px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(44, 62, 80);
                    }'''

CMD_HISTORY_LABEL = '''font: 57 9pt \"Dubai Medium\";
                color: rgb(255, 255, 255);
                background-color: rgb(44, 62, 80);'''

CMD_HISTORY_SCROLLAREA = '''QScrollArea{
                        border: 2px solid rgb(44, 62, 80);
                        color: rgb(255, 255, 255);
                        background-color: rgb(26, 37, 48);
                        border-radius: 5px;
                    }'''

CMD_HISTORY_SCROLLBAR = "background-color: rgb(231, 76, 60);"

SERIAL_OUTPUT_LABEL = '''font: 57 9pt \"Dubai Medium\";
                color: rgb(255, 255, 255);
                background-color: rgb(44, 62, 80);'''

SERIAL_OUTPUT_SCROLLAREA = '''QScrollArea{
                        border: 2px solid rgb(44, 62, 80);
                        color: rgb(255, 255, 255);
                        background-color: rgb(26, 37, 48);
                        border-radius: 5px;
                }'''

SERIAL_OUPUT_SCROLLBAR = "background-color: rgb(231, 76, 60);"

OUTPUT_LABEL = '''color: rgb(255, 255, 255);
                background-color: rgb(44, 62, 80);
                font: 57 9pt \"Dubai Medium\";'''

SAT_SELFIE_GROUP = '''QGroupBox{
                        font: 57 8pt \"Dubai Medium\";
                        border: 2px solid rgb(26, 37, 48);
                        border-radius: 15px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(44, 62, 80);
                    }'''

SAT_SELFIE_GRAPHIC = '''QGraphicsView{
                        font: 57 8pt \"Dubai Medium\";
                        border: 2px solid rgb(26, 37, 48);
                        border-radius: 15px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(26, 37, 48);
                    }'''

TELEMETRY_GROUP = '''QGroupBox{
                        font: 57 8pt \"Dubai Medium\";
                        border: 2px solid rgb(26, 37, 48);
                        border-radius: 15px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(44, 62, 80);
                    }'''

TELEMETRY_GRAPHIC = '''QGraphicsView{
                        font: 57 8pt \"Dubai Medium\";
                        border: 2px solid rgb(26, 37, 48);
                        border-radius: 15px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(26, 37, 48);
                    }'''
                    
IMAGE_GRAPHICS_GROUP = '''QGroupBox{
                        font: 57 8pt \"Dubai Medium\";
                        border-radius: 5px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(26, 37, 48);
                        border: 2px solid rgb(231, 76, 60);
                    }'''

MAP_SAT_GROUP = '''QGroupBox{
                        font: 57 8pt \"Dubai Medium\";
                        border: 2px solid rgb(26, 37, 48);
                        border-radius: 15px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(44, 62, 80);
                    }'''

SAT_GROUP = '''QGroupBox{
                        font: 57 8pt \"Dubai Medium\";
                        border: 2px solid rgb(26, 37, 48);
                        border-radius: 15px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(44, 62, 80);
                    }'''

GRAPHICS = '''QGraphicsView{
                        border: 2px solid rgb(44, 62, 80);
                        color: rgb(255, 255, 255);
                        background-color: rgb(26, 37, 48);
                        border-radius: 15px;
                }'''

TAB_SWITCH_WINDOW = '''QWidget{
                        font: 57 8pt \"Dubai Medium\";
                        color: rgb(255, 255, 255);
                        background-color: rgb(44, 62, 80);
                }'''