#!/bin/bash

termux-setup-storage -y


install_python() {
    echo "Installing Python..."
    pkg update -y || { echo "Failed to update packages. Exiting."; exit 1; }
    pkg install python -y || { echo "Failed to install Python. Exiting."; exit 1; }
    pkg install python-pip -y || { echo "Failed to install Python. Exiting."; exit 1; }
}

install_git() {
    echo "Installing Git..."
    pkg install git || { echo "Failed to install Git. Exiting."; exit 1; }
    pkg install python git -y || { echo "Failed to install Git Python. Exiting."; exit 1; }
}

install_wget() {
    echo "Installing wget..."
    pkg install wget || { echo "Failed to install wget. Exiting."; exit 1; }
}

install_curl() {
    echo "Installing curl..."
    pkg install curl || { echo "Failed to install curl. Exiting."; exit 1; }
}



if ! command -v python || ! command -v pip; then
    install_python
fi

if ! command -v git; then
    install_git
fi

if ! command -v wget; then
    install_wget
fi

if ! command -v curl; then
    install_curl
fi

if [ -f FixResult.py ]; then
    rm FixResult.py
    echo "Updating FixResult.py..."
fi

curl -fsSL -o FixResult.py https://raw.githubusercontent.com/arshiacomplus/Test/main/FixResult.py || { echo "Failed to download FixResult.py. Exiting."; exit 1; }

python FixResult.py
