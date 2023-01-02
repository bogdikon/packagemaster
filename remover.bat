@echo off
cd .\packages\
if exist .\%1 goto exist
goto notexist





:exist
rd /s /q %1
exit 0

:notexist
exit 1