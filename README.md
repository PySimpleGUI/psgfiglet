
<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Logo%20with%20text%20for%20GitHub%20Top.png" alt="Python GUIs for Humans">
  <h2 align="center">Figlet Creation</h2>
</p>

Create Figlets easily using this application created using PySimpleGUI.

## Installation

### Old-school Straight Pip

pip install psgfiglet

### pip via `python -m pip` the python recommended way

#### If `python` is your command

python -m pip install psgfiglet

#### If `python3` is your command

python3 -m pip install psgfiglet

## Usage

To run the program and create your own Figlets type from your command prompt:

psgfiglet




## About - What is a Figlet?

A Figlet is a text based way to add large block text to your code or chats.  There are a variety of "Fonts" available that you'll find listed along the left side of the screen.

![image](https://user-images.githubusercontent.com/46163555/136379651-58f474d7-fbfa-423f-a5da-162d6936d104.png)

## To use in your code

The easiest way to is make a multiline string in your code using triple quotes:

```python

'''
This is a multiline string
Line 2
'''
```


You can simply paste your Figlet into one of these multiline comments.  They work well at breaking up your code into chunks

```python

'''
                    oo          
                                
88d8b.d8b. .d8888b. dP 88d888b. 
88'`88'`88 88'  `88 88 88'  `88 
88  88  88 88.  .88 88 88    88 
dP  dP  dP `88888P8 dP dP    dP
'''

def main():
    x = 20

```

## License

Licensed under an LGPL3 License

## Origins and Underlying Package

### Origination of GUI

The code has roots in a program developed by @nycynik that you'll find in the repo:

https://github.com/nycynik/ascii-font-processor

@nycynik has kindly licensed his code using an MIT license.


### Underlying Package Required

Without pyfiglet none of this would be possible.  It's at the core of the program since it's what actually makes the figlet.  The PySimpleGUI portion is a front-end integration.  Information is collected from the user, the pyfiglet package is called to convert the input string and then the results are displayed in the GUI.

They were kind enough to license this code using an MIT license.

pyfiglet - https://github.com/pwaller/pyfiglet

If you pip install `psgfiglet` it will also install pyfiglet for you.

Of course you'll need PySimpleGUI as well.

## Contributing

Like the PySimpleGUI project, this project is currently licensed under an open-source license, the project itself is structured like a proprietary product. Pull Requests are not accepted.

## Release Notes
1.21.0   2-Jan-2022
* Updated readme with credit for initial code and package used added
* Changed the .py file to be psgfiglet.py in keeping with the new naming convention for projects released to PyPI with the `psg` prefix. Previously used gui.py generically.


## Copyright

Copyright 2021, 2022 PySimpleGUI
