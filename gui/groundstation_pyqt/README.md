# Comms - PyQt5 GUI

#### Initialization:
1. Install all python libraries in requirements.txt (including PyQt5 i.e. pip install pyqt5)
2. Generate unique API_KEY from OpenWeather website and update value in comms/gui/API_KEY.py
3. Run main.py in groundstattion_pyqt/main.py
4. (Optional) use QtDesigner application (inluded with pyqt5 installation) to edit/view .ui files

#### To Edit:
- Edit python files in groundstation_pyqt to edit GUI program.

#### NOTES:
- Changes in .ui files with qt designer will not be reflected in python code

#### To change .ui to .py:
1. Use pyuic5 tool (bundled with pyqt5 installation) and in command line type:
> pyuic5 [FILENAME].ui [FILENAME].py