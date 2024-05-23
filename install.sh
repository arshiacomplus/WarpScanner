#!/bin/bash

# دانلود فایل پایتون
curl -fsSL -o FixResult.py https://raw.githubusercontent.com/arshiacomplus/Test/main/FixResult.py

command -v python3 &>/dev/null || {
    echo "wait for install python3...."

    pkg update && pkg upgrade
    pkg install python-pip 
    pkg install git python
}
# اجرای فایل پایتون
python3 FixResult.py
