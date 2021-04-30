# Handwritten Digit Recognition
This is a program which lets the user input a handwritten digit and the AI model will predict what the digit is depending on the accuracy of the chosen model.

## Description
<!-- What your application does,
Why you used the technologies you used,
Some of the challenges you faced and features you hope to implement in the future. -->

## Prerequisites

torch:          PyTorch is an open source machine learning library based on the Torch library, 
                used for applications such as computer vision and natural language processing,       
                primarily developed by Facebook's AI Research lab (FAIR).

torchvision:    This library is part of the PyTorch project. PyTorch is an open source machine learning framework.
                The torchvision package consists of popular datasets, model architectures, and common image transformations for computer vision.
                
TensorFlow:     TensorFlow is an end-to-end open source platform for machine learning. 
                It has a comprehensive, flexible ecosystem of tools, libraries and community resources
                that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.

NumPy:          NumPy is a Python library used for working with arrays.

Pillow:         Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

PyQt5:          PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in.

requests:       The requests module allows you to send HTTP requests using Python. 
                The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

## Installation

In order to run the program a python development environment is needed. These are the steps in order to install the recommended setup:

Step 1
[Miniconda Docs](https://docs.conda.io/en/latest/miniconda.html)
Download Python Version 3.8 and follow the on screen prompts to install miniconda
In order to create the development environment launch "Anaconda Prompy (miniconda3)" and type in the following:
```sh
conda create –n py38 python=3.8
```
```sh
y
```
```sh
conda activate py38
```

We need to install the above mentioned libraries in order to run our program:
```sh
pip install PyQt5 torch torchvision tensorflow
```

Check if the above programs have been installed:
```sh
pip list
```

Step 2
[Visual Studio Code](https://code.visualstudio.com/)
The recommended IDE to be used would be Visual Studio but other IDEs can be used to the users preference.
Download Visual Studio Code and follow the on screen prompts to install VS Code.
Install the Python extension by navigation to the Extension tab on the left side.
Open the project folder with the scripts on the workspace and select 'py38' as your Python Interpreter.

## Usage
Running the program is easy, navigate to the "main_window.py" file and Run without Debugging.

1. To recognize digits on the program follow these steps:

Step 1
Train a Model by navigating to >> File >> Train Model, or use Ctrl+T.
Pick a Model of your preference and wait for the model to finish training and the accuracy of your model will be displayed.

Step 2
Draw Digits by navigating to >> View >> Open Analyser.
Draw your digit on the canvas.
Clear Button can be used to clear the canvas.
Recognize Button can be used to analyse and get the probabilities of what digit it is.
The Predictions chart will display the probabilities of the analysed digit.

2. To view Images from the dataset follow these steps:

Navigate to >> View >> View Testing Images, and the images will be displayed.

## Credits


## Versions
Version 65 - probabilities added <br />
Version 64 - . <br />
Version 63 - added placeholder images
Version 62 - Merge branch 'master' of https://github.com/COMPSYS-302-2021/project-… …
Version 61 - .
Version 60 - logo!
Version 59 - .
Version 58 - Merge branch 'master' of https://github.com/COMPSYS-302-2021/project-… …
Version 57 - added preprocessing
Version 56 - Added save image functions
Version 55 - added preprocessing into master file
Version 54 - Merge branch 'master' of https://github.com/COMPSYS-302-2021/project-… …
Version 53 - .
Version 52 - commented
Version 51 - removed camelCase completely
Version 50 - camelCase removed from mainWindow
Version 49 - getting rid of camel case
Version 48 - added a few models
Version 47 - Merge branch 'master' of https://github.com/COMPSYS-302-2021/project-… …
Version 46 - Fixed prediction method. …
Version 45 - Used a new model. …
Version 44 - Attempt at making recognise work …
Version 43 - Revert back to working version.
Version 42 - .
Version 41 - restored main_window.py
Version 40 - Changed all variable names to a better naming system
Version 39 - added an icon …
Version 38 - Progress Bar works for training
Version 37 - Merge branch 'Canvas'
Version 36 - Added a working canvas …
Version 35 - Changed 'view test image' …
Version 34 - Added slider and label …
Version 33 - .
Version 32 - progress bar works but doesnt update
Version 31 - Progress Bar …
Version 30 - .
Version 29 - Merge pull request #5 from COMPSYS-302-2021/GUI-Changes-Lenny …
Version 28 - Merge branch 'master' into GUI-Changes-Lenny
Version 27 - Train_gui …
Version 26 - Train_gui …
Version 25 - Added the drawing canvas …
Version 24 - Merge pull request #4 from COMPSYS-302-2021/QPainter …
Version 23 - added a drawing file …
Version 22 - Merge pull request #3 from COMPSYS-302-2021/QPainter …
Version 21 - added a drawing file …
Version 20 - Tried to fix the layout of ModelUI() …
Version 19 - Fixed Centering
Version 18 - Attempted to add PixMap
Version 17 - Working ModelUI() …
Version 16 - Imported test_gui to train_gui
Version 15 - Changed QMainWindows -> QWidget …
Version 14 - fixed indentation …
Version 13 - Merge branch 'master' of https://github.com/COMPSYS-302-2021/project-… …
Version 12 - UI update. …
Version 11 - Merge pull request #2 from COMPSYS-302-2021/GUI-Changes-Lenny …
Version 10 - AI Model …
Version 9 - pbar in train_gui …
Version 8 - update train_gui …
Version 7 - Merge pull request #1 from COMPSYS-302-2021/GUI-Changes-Lenny …
Version 6 - Centering GUI …
Version 5 - test_gui_05 …
Version 4 - test_gui_04 …
Version 3 - test_gui_03 …
Version 2 - test_gui_02 …
Version 1 - test_gui_01 …

