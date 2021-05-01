# Handwritten Digit Recognition
This is a program which lets the user input a handwritten digit and the AI model will predict what the digit is depending on the accuracy of the chosen model.

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#description">Description</a>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#how-to">How To</a></li>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#version">Version</a></li>
  </ol>
</details>

## Description
<!-- What your application does, Why you used the technologies you used, Some of the challenges you faced and features you hope to implement in the future. -->

## Prerequisites

1. [torch](https://pytorch.org/)          
PyTorch is an open source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing, primarily developed by Facebook's AI Research lab (FAIR).

2. [torchvision](https://pytorch.org/vision/stable/index.html)
This library is part of the PyTorch project. PyTorch is an open source machine learning framework. The torchvision package consists of popular datasets, model architectures, and common image transformations for computer vision.

3. [NumPy](https://numpy.org/)
NumPy is a Python library used for working with arrays.

4. [Pillow](https://pillow.readthedocs.io/en/stable/)
Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

5. [PyQt5](https://pypi.org/project/PyQt5/)
PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in.

6. [requests](https://pypi.org/project/requests/)
The requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

## Installation

In order to run the program a python development environment is needed. These are the steps in order to install the recommended setup:

#### Step 1 <br />
[Miniconda Docs](https://docs.conda.io/en/latest/miniconda.html) <br />
Download **Python Version 3.8** and follow the on screen prompts to install miniconda <br />
In order to create the development environment launch `Anaconda Prompt (miniconda3)` and type in the following:
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
pip install PyQt5 torch torchvision
```

Check if the above programs have been installed:
```sh
pip list
```

#### Step 2 <br />
[Visual Studio Code](https://code.visualstudio.com/) <br />
The recommended IDE to be used would be Visual Studio but other IDEs can be used to the users preference. <br />
Download Visual Studio Code and follow the on screen prompts to install VS Code. <br />
Install the *Python Extension* by navigation to the *Extension tab* on the left side. <br />
Open the project folder with the scripts on the workspace and select `py38` as your Python Interpreter. 

## How To
Running the program is easy, navigate to the `main_window.py` file and ***Run without Debugging***.

1. To recognize digits on the program follow these steps:

##### Step 1 <br />
Train a Model by navigating to >> `File` >> `Train Model`, or use `Ctrl+T`. <br />
Pick a Model of your preference and wait for the model to finish training and the accuracy of your model will be displayed. 

##### Step 2 <br />
Draw Digits by navigating to >> `View` >> `Open Analyser`. <br />
Draw your digit on the canvas. <br />
`Clear` Button can be used to clear the canvas. <br />
`Recognize` Button can be used to analyse and get the probabilities of what digit it is. <br />
The `Predictions` chart will display the probabilities of the analysed digit. <br />

2. To view Images from the dataset follow these steps:

Navigate to >> `View` >> `View Testing Images`, and the images will be displayed.

## Credits
Cynthia Kwok - Made the GUI and Interface <br />
Pulasthi Lenaduwa - Integrated the AI Models into the GUI

## Acknowledgments
<!-- add all the supporting sites we used -->

## Versions
Version 75 - . <br />
Version 74 - stylised readme <br />
Version 73 - . <br />
Version 72 - readme formatting 
Version 71 - added usage instructions <br />
Version 70 - added an accuracy label to training <br />
Version 69 - Cleaning up the project files … <br />
Version 68 - . <br />
Version 67 - Update README.md … <br />
Version 66 - making readme file <br />
Version 65 - probabilities added <br />
Version 64 - . <br />
Version 63 - added placeholder images <br />
Version 62 - Merge branch 'master' of https://github.com/COMPSYS-302-2021/project-… … <br />
Version 61 - . <br />
Version 60 - logo! <br />
Version 59 - . <br />
Version 58 - Merge branch 'master' of https://github.com/COMPSYS-302-2021/project-… … <br />
Version 57 - added preprocessing <br />
Version 56 - Added save image functions <br />
Version 55 - added preprocessing into master file <br />
Version 54 - Merge branch 'master' of https://github.com/COMPSYS-302-2021/project-… … <br />
Version 53 - . <br />
Version 52 - commented <br />
Version 51 - removed camelCase completely <br />
Version 50 - camelCase removed from mainWindow <br />
Version 49 - getting rid of camel case <br />
Version 48 - added a few models <br />
Version 47 - Merge branch 'master' of https://github.com/COMPSYS-302-2021/project-… … <br />
Version 46 - Fixed prediction method. … <br />
Version 45 - Used a new model. … <br />
Version 44 - Attempt at making recognise work … <br />
Version 43 - Revert back to working version. <br />
Version 42 - . <br />
Version 41 - restored main_window.py <br />
Version 40 - Changed all variable names to a better naming system <br />
Version 39 - added an icon … <br />
Version 38 - Progress Bar works for training <br />
Version 37 - Merge branch 'Canvas' <br />
Version 36 - Added a working canvas … <br />
Version 35 - Changed 'view test image' … <br />
Version 34 - Added slider and label … <br />
Version 33 - . <br />
Version 32 - progress bar works but doesnt update <br />
Version 31 - Progress Bar … <br />
Version 30 - . <br />
Version 29 - Merge pull request #5 from COMPSYS-302-2021/GUI-Changes-Lenny … <br />
Version 28 - Merge branch 'master' into GUI-Changes-Lenny <br />
Version 27 - Train_gui … <br />
Version 26 - Train_gui … <br />
Version 25 - Added the drawing canvas … <br />
Version 24 - Merge pull request #4 from COMPSYS-302-2021/QPainter … <br />
Version 23 - added a drawing file … <br />
Version 22 - Merge pull request #3 from COMPSYS-302-2021/QPainter … <br />
Version 21 - added a drawing file … <br />
Version 20 - Tried to fix the layout of ModelUI() … <br />
Version 19 - Fixed Centering <br />
Version 18 - Attempted to add PixMap <br />
Version 17 - Working ModelUI() … <br />
Version 16 - Imported test_gui to train_gui <br />
Version 15 - Changed QMainWindows -> QWidget … <br />
Version 14 - fixed indentation … <br />
Version 13 - Merge branch 'master' of https://github.com/COMPSYS-302-2021/project-… … <br />
Version 12 - UI update. … <br />
Version 11 - Merge pull request #2 from COMPSYS-302-2021/GUI-Changes-Lenny … <br />
Version 10 - AI Model … <br />
Version 9 - pbar in train_gui … <br />
Version 8 - update train_gui … <br />
Version 7 - Merge pull request #1 from COMPSYS-302-2021/GUI-Changes-Lenny … <br />
Version 6 - Centering GUI … <br />
Version 5 - test_gui_05 … <br />
Version 4 - test_gui_04 … <br />
Version 3 - test_gui_03 … <br />
Version 2 - test_gui_02 … <br />
Version 1 - test_gui_01 … <br />

