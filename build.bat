@echo off
rem Needs: JDK 25, Python 3, Gradle (current version) on your PATH, internet.
python resolve_versions.py && gradle build && echo Jar is in build\libs\
pause
