# ADB WiFi Pairing
This is a Python script to facilitate the pairing of Android devices with ADB over WiFi using QR code. It generates a random WiFi configuration, displays it as a QR code, and waits for the device to be paired through the QR code. Once paired, it connects the device over WiFi.

# Requirements
- Python 3: [Download Python](https://www.python.org/downloads/)
- ADB (Android Debug Bridge): [Download ADB](https://developer.android.com/tools/releases/platform-tools)

## Installation
- Download and install Python 3 from the provided link.
- Download and install ADB from the provided link.
- Clone or download this repository.

## Setup
- Install the required Python packages using pip by running the following command in the terminal:
```shell
pip install -r requirements.txt
```

## Usage
- Make sure your Android device is connected to the same network as your computer.
- Enable Developer options and Wireless debugging on your Android device.
- Run the ADBWiFiPairing.py script:
```shell
python ADBWiFiPairing.py
```

Please note that you need to have adb in your system's PATH for this script to work.
