#!/bin/sh
# Needs: JDK 25, Python 3, Gradle (current version) on your PATH, internet.
python3 resolve_versions.py && gradle build && echo "Jar is in build/libs/"
