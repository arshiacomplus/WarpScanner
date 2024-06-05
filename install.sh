#!/bin/bash

install_python() {
    echo "Installing Python..."
    pkg update
    pkg install python-pip
    pkg install git python
}

install_wget() {
    echo "Installing wget..."
    pkg install wget -y
}

install_curl() {
    echo "Installing curl..."
    pkg install curl -y
}

if ! command -v python &>/dev/null; then
    install_python
fi

if ! command -v wget &>/dev/null; then
    install_wget
fi

if ! command -v curl &>/dev/null; then
    install_curl
fi

curl -fsSL -o FixResult.py https://raw.githubusercontent.com/arshiacomplus/Test/main/FixResult.py

python FixResult.py
