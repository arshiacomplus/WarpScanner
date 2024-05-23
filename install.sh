#!/bin/bash

# دانلود فایل پایتون
curl -fsSL -o FixResult.py https://raw.githubusercontent.com/arshiacomplus/Test/main/FixResult.py

command -v python3 &>/dev/null || {
    echo "Python 3 نصب نیست. در حال نصب..."

    pkg install python-pip 
    pkg install git python
}
# اجرای فایل پایتون
python3 FixResult.py
