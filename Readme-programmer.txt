DEPENDENCIES FOR BUILDING:
    - Python (written in 2.7, any recent version should work)
    - PyQt4
    - setuptools
    - py2exe

INSTRUCTIONS FOR BUILDING:
    - "python setup.py py2exe" will generate the build and dist folders. The dist folder contains the executable and all
       files necessary for running.


NOTE: The convert_ui.bat script allows for easy conversion from .ui to .py. It takes one parameter,
      the filename without its extension. It outputs the .py file into the main UXO directory. 
      Eg: "convert_ui.bat main_window" would generate a ../main_window.py file from the main_window.ui file.