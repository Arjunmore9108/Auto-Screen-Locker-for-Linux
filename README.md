# Linux RSSI-Based Auto Screen Lock

This Python script automatically locks your Linux desktop when a specific Bluetooth device comes within a certain signal strength (RSSI). It works on **all major Linux distributions** and supports multiple desktop environments including GNOME, KDE, XFCE, Cinnamon, MATE, LXDE, and Budgie.

---

## Features

- Monitor a Bluetooth device by MAC address.
- Automatically lock the screen when the device is not close to the desktop.
- Works with multiple Linux distributions (Kali, Ubuntu, Fedora, Arch, Debian, Mint, etc.).
- Supports multiple desktop environments.
- Configurable RSSI threshold and polling interval.
- Prints RSSI values in terminal for monitoring.

---

## Requirements

- Linux machine with Bluetooth support.
- Python 3.x
- `hcitool` (part of the `bluez` package)
- Standard Linux screen lock commands (`loginctl`, `xdg-screensaver`, `dm-tool`, `gnome-screensaver-command`, `qdbus`)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Arjunmore9108/Auto-Screen-Locker-for-Linux.git
cd Auto-Screen-Locker-for-Linux

2.Make sure Python 3 is installed:
```bash
python3 --version

3.Install bluez if not already installed:

Debian/Ubuntu/Kali:
```bash
sudo apt install bluez


Fedora:
```bash
sudo dnf install bluez

4.Usage
Open lock_rssi.py and set your Bluetooth device MAC address:
```python
MAC = "3C:4D:CC:1C:C6:A5"  # Set your device's MAC

5.Run the script:
```bash
sudo python3 lock_rssi.py
