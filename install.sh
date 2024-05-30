#!/bin/bash

# دانلود فایل پایتون
curl -fsSL -o FixResult.py https://raw.githubusercontent.com/arshiacomplus/Test/main/FixResult.py

command -v python &>/dev/null || {
    echo "wait for install python...."

    
    pkg install python-pip
    pkg install git python
}
# اجرای فایل پایتون
python FixResult.py
