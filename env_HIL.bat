@ECHO OFF

:: Setup the environments.
@call .bootstrap\WinPython\env_winpython.bat
@call .bootstrap\MinGW\env_mingw.bat
@call .bootstrap\LLVM\env_llvm.bat

:: Setup local virtual environments
@call Scripts\activate.bat