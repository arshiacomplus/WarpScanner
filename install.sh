#!/bin/bash

curl -fsSL -o FixResult.py https://raw.githubusercontent.com/arshiacomplus/Test/main/FixResult.py

command -v python &>/dev/null || {
    echo "wait for install python...."

    pkg update
    pkg install python-pip
    pkg install git python
}

command -v wget &>/dev/null || {
    echo "wget is not installed. Installing..."
    pkg install wget -y
}
command -v curl &>/dev/null || {
    echo "curl is not installed. Installing..."
    pkg install curl -y
}


python FixResult.py
