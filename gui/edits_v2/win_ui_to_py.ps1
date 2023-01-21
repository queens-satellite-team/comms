#PowerShell script automating the conversion of .ui files to .py file using pyuic5
#new files are created in the same directory
#by Joseph Moraru

Write-Host "Generates python files from .UI files using pyuic5"
$pyuic5_path = Read-Host "Enter absolute path to pyuic5.exe here" -Prompt
$ui_path = Read-Host "Enter absolute path to .ui file here" -Prompt
$py_path = Read-Host "Enter absolute path to .py file here" -Prompt

#execute ui to py conversion here
Start-Process $pyuic5_path -ArgumentList "-x", "$ui_path", "-o", "$py_path"

Write-Host "New .py file stored at $py_path"
Write-Host "Job completed."