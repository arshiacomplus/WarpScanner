#!/bin/bash

termux-setup-storage

update_packages() {
    echo "Updating packages..."
    pkg update -y || { echo "Failed to update packages. Exiting."; exit 1; }
}

install_python() {
    echo "Installing Python..."
    pkg install python -y || { echo "Failed to install Python. Exiting."; exit 1; }
    pkg install python-pip -y || { echo "Failed to install Python. Exiting."; exit 1; }
}

install_git() {
    echo "Installing Git..."
    pkg install git || { echo "Failed to install Git. Exiting."; exit 1; }
    pkg install git python -y || { echo "Failed Failed to install git python. Exiting."; exit 1; }

}

install_wget() {
    echo "Installing wget..."
    pkg install wget || { echo "Failed to install wget. Exiting."; exit 1; }
}

install_curl() {
    echo "Installing curl..."
    pkg install curl || { echo "Failed to install curl. Exiting."; exit 1; }
}

update_packages

if ! command -v python &>/dev/null; then
    install_python
fi

if ! command -v git &>/dev/null; then
    install_git
fi

if ! command -v wget &>/dev/null; then
    install_wget
fi

if ! command -v curl &>/dev/null; then
    install_curl
fi

curl -fsSL -o FixResult.py https://raw.githubusercontent.com/arshiacomplus/Test/main/FixResult.py || { echo "Failed to download FixResult.py. Exiting."; exit 1; }

python FixResult.py
