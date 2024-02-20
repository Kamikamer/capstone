# This is the development branch for all the coding and testing, anything officially submitted will be in [production branch](https://github.com/Kamikamer/capstone/tree/main), we are in [development branch](https://github.com/Kamikamer/capstone/tree/development)

## Table of contents

- [Installation](#installation)
- [Run project](#run-the-entire-project)
- [Run files](#run-specific-files)
- [Common error](#common-error)

## Installation

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/Kamikamer/capstone/tree/main/docs/source-compilation.md)

[![Executable](https://img.shields.io/badge/Executable-3776AB?style=for-the-badge&color=000&logoColor=white)](https://github.com/Kamikamer/capstone/releases/download/v1.0.0/PostureFit.exe)

### Need help with installation? 

[Click here](https://github.com/Kamikamer/capstone/tree/main/docs)

## Run the entire project

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

Run the executable

or 

python index.py

## Run specific files

Run python file in X package

``python -m package.X``

E.g. python -m posture_fit_development.Webcam  
E.g. python -m posture_fit_algorithm.Sound

## Common error

If you installed the libraries manually and you are facing error with the sound system such as ![The driver cannot recognize the spececified command parameter.](/assets/driver_error_sp.png)

Reinstall playsound (lib) with version 1.2.2  
Windows: `pip uninstall playsound -y; pip install playsound==1.2.2`  
Linux: `pip uninstall playsound -y && pip install playsound==1.2.2`

If you face errors with icecream, you might need to install it with  
`pip install icecream` instead of `conda install icecream`

If you get issues with icecream or any other module, please make a pull request or a issue request!

