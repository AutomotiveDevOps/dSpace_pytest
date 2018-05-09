git submodule init
git submodule update

call .bootstrap\WinPython\bootstrap_winpython.bat
call .bootstrap\CMake\bootstrap_cmake.bat
call .bootstrap\MinGW\bootstrap_mingw.bat
call .bootstrap\LLVM\bootstrap_llvm.bat

:: call .bootstrap\GreenHillsSoftware\bootstrap_ghs.bat
:: call .bootstrap\WindRiver\bootstrap_diab.bat
:: call .bootstrap\MATLAB\bootstrap_matlab.bat

make venv