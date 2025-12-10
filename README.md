# Linux RSSI-Based Auto Screen Lock

This Python script automatically locks your Linux desktop when a specific Bluetooth device comes within a certain signal strength (RSSI). It works on **all major Linux distributions** and supports multiple desktop environments including GNOME, KDE, XFCE, Cinnamon, MATE, LXDE, and Budgie.

---

## Features

- Monitor a Bluetooth device by MAC address.
- Automatically lock the screen when the device is not closer to Desktop.
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
git clone https://github.com/<username>/linux-rssi-auto-lock.git
cd linux-rssi-auto-lock
