# Comms - PyQt5 GUI: Developer Workflow

### Initialization:
1. Install all python libraries in requirements.txt (including PyQt5 i.e. pip install pyqt5)
2. Generate unique API_KEY from OpenWeather website and update value in comms/gui/API_KEY.py
3. Run main.py in src/main.py to use GUI

#### To Edit:
- Edit python files in groundstation_pyqt to edit GUI program, and/or ...
- Edit .ui files with QtDesigner

### Choose ONE of A, B or C:

#### A. To MANUALLY change .ui to .py (Recommended):
1. Use pyuic5 tool (bundled with pyqt5 installation) and in command line type:
>pyuic5 FILENAME.ui FILENAME.py
2. For more information regarding .ui to .py see [.ui to .py Conversion Video](https://www.youtube.com/watch?v=1wEsP70hO0o)

#### B. (Optional) Automate UI -> PY Conversion (Windows):

1. In the /automation_scripts folder run the powershell script:
>win_ui_to_py.ps1
2. Follow prompts as required

#### C. (Optional) Automate UI -> PY Conversion (UNIX):

1. In the /automation_scripts folder run the shell script (might have to chmod 700):
>./win_ui_to_py.sh
2. Follow prompts as required

### NOTES:
- Changes in .ui files with qt designer will not be reflected in python code 
- Converting .ui files to .py files with pyuic generates new python code specific to .ui file. It is strongly recommended to edit generated python code (i.e add comments, change code layout, include useful functions) to improve readability and usability for future devs.
- .ui files are not needed for the GUI to run (only need python code). .ui files are only included for making front end edits easier/faster using QtDesigner.
- If converting .ui files using pyuic5 tool, ensure you are in the correct directory before using pyuic5 tool.

# Running the GUI
1. Ensure all python libraries are installed from 'requirments.txt'
2. Either from console or development environment, run 'main.py' to start the GUI

Now you're all set to go!