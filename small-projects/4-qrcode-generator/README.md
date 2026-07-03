# QR Code Generator
Program to generate a QR Code image with a link, created with Python and using a QR Code library.

## Table of Content 
## Table of Content 
- [Overview](#overview)
- [View](#view)
- [Process Breakdown](#process-breakdown)
    - [How to Run](#how-to-run)
- [Links](#links)
- [Author](#author)

## Overview

The user is asked to add a URL for any website and a name for the file with the preferrable extension. Then choose the color of the code and background. If the user doesn't add a color to either option, the QR Code will generated in a standard black with a white background.
Once generated, the iamge is automatically saved in the same folder where the program is.

## View

<div align="center">
  <img width="550" height="300" alt="" src="./qrcode-generator.gif" />
</div>

## Process Breakdown

For this code, a library needs to be downloaded to be able to generate the QR Code correctly. The `qrcode 8.2` is the libray used downloaded, with the pillow dependency to generate the QR Code image.

```
pip install "qrcode[pil]"
```

Starting by importing the library, then two variable have an user input. One to add the URL the user wants the code to open, and the second one to add the name of the file (the user need to add the image extension when adding the name of the file or the image will not create correctly). 


#### How to Run

Python Version: 3.13.7
QR Code Library Version: 8.2

```
# Download the code onto a preferred folder.
```
```
# Open the terminal console and navigate to the folder where the file was downloaded.
```
``` 
# Create the Virtual Environment .venv inside the folder where the code is.
python3 -m venv .venv
```
```
# Activate the .venv environment.
source .venv/bin/activate
```
```
# Download the Library used to generate the QR Code. The should be installed with the `pil` dependency for you to be able to generate the QR Code Image.
pip install "qrcode[pil]"
```
```
# (OPTIONAL) Once the virtual environment is activated and the library is installed, you can look for the exact location of the file inside the folder
find . -name 4-qrcode-generator.py
```
```
# Run the Code
python3 4-qrcode-generator.py
```

## Links

- [QR Code Library](https://pypi.org/project/qrcode/) - Library used for the QR Code Generator Project
- [Python for Beginners - Master Problem Solving](https://youtu.be/yVl_G-F7m8c?si=Q8ebGLM_njwdJAww) - Python Tutorial 

## Authorde 

- Developed by Nathalia Santos 🐉<br><br>
[![LinkedIn Badge](https://img.shields.io/badge/-Nathalia_Santos-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/naathcs/)](https://www.linkedin.com/in/naathcs/)