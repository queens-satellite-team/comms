#!/bin/bash
#UNIX Shell script automating the conversion of .ui files to .py file using pyuic5
#new files are created in the same directory
#reads exactly 3 args from std input
#PLEASE have pyuic5 installed before running this script, thanku
#by Joseph Moraru

echo "---UNIX Script for converting UI file to .py---"
if [[ $# -ne 3 ]]; then
    echo "You must provide exactly 3 arguments: (1) pyuic5 abs path, (2) ui file abs path, (3) output py abs path"
    exit 1
else
    pyuic5_path=$1
    ui_path=$2
    py_path=$3
    #execute pyuic here and convert ui -> py
    $pyuic5_path $ui_path $py_path
    echo "Conversion compete."
    exit 0
fi