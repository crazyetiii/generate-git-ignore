rem:generate exe
pyinstaller -F gen_git_ignore.py

rem:copy to .
copy dist\gen_git_ignore.exe . /Y
rem :delete old gen.exe
del gen.exe
ren gen_git_ignore.exe gen.exe

copy gen.exe C:\Windows\ 


rem: delete build/dist
del gen_git_ignore.spec /Q
rd /S /Q dist
rd /S /Q build