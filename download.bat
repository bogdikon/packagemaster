@echo off
cd .\packages\
..\py\lib\wget %1 >nul 2>&1
tar -x -f %2
del %2