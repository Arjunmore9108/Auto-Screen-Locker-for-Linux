# 🔒 Linux RSSI-Based Auto Screen Lock

This Python script automatically locks your Linux desktop when a specific Bluetooth device moves out of a defined range, based on its Received Signal Strength Indicator (**RSSI**). It enhances security by automatically locking your screen when you step away.

## ✨ Features

* **Device Monitoring:** Monitors a specific Bluetooth device by its **MAC address**.
* **Auto-Locking:** Automatically locks the screen when the device's signal strength falls below the configured threshold (meaning the device is **not close** to the desktop).
* **Broad Compatibility:**
    * Works with multiple Linux distributions (Kali, Ubuntu, Fedora, Arch, Debian, Mint, etc.).
    * Supports multiple desktop environments (GNOME, KDE, XFCE, Cinnamon, MATE, LXDE, Budgie).
* **Configuration:** Configurable **RSSI threshold** and **polling interval**.
* **Debugging:** Prints real-time **RSSI values** in the terminal for monitoring.

## ⚙️ Requirements

To run this script, you need:

* A Linux machine with **Bluetooth support**.
* **Python 3.x** installed.
* **`hcitool`** (part of the `bluez` package).
* Standard Linux screen lock commands (e.g., `loginctl`, `xdg-screensaver`, `dm-tool`, `gnome-screensaver-command`, `qdbus`).

## 💾 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Arjunmore9108/Auto-Screen-Locker-for-Linux.git
    cd Auto-Screen-Locker-for-Linux
    ```

2.  **Verify Python 3 is installed:**
    ```bash
    python3 --version
    ```

3.  **Install `bluez` (which includes `hcitool`) if not already installed:**

| Distribution | Command |
| :--- | :--- |
| **Debian / Ubuntu / Kali** | `sudo apt install bluez` |
| **Fedora** | `sudo dnf install bluez` |
| *Arch, etc.* | *Use your distribution's package manager* |

## 🚀 Usage

1.  **Configure Your Device MAC Address and Threshold:**
    Open `lock_rssi.py` in a text editor and update the following variables:

    ```python
    MAC = "3C:4D:CC:1C:C6:A5"  # <-- Set your device's MAC here
    THRESHOLD = -60           # RSSI value (e.g., -60 dBm) below which the screen locks
    INTERVAL = 5              # Polling interval in seconds
    ```

2.  **Run the script:**
    The script requires **root privileges** to interact with the Bluetooth hardware via `hcitool`.
    ```bash
    sudo python3 lock_rssi.py
    ```
    The script will start monitoring and printing RSSI values. When the RSSI drops below the defined `THRESHOLD` (meaning the device is far away), the screen will automatically lock.

### 📝 Configuration Notes

* **What is RSSI?** RSSI (Received Signal Strength Indicator) is a negative number (e.g., -40, -85). A **smaller** absolute value (e.g., $-40$ is stronger than $-85$) indicates a **stronger signal** and closer proximity.
* **Recommended Threshold:** A good starting point for `THRESHOLD` is between **$-50$** and **$-70$**. You should test the script and monitor the RSSI values printed in the terminal to find the perfect value for your environment and device.

## ⚠️ Disclaimer

This script uses system commands to lock the screen and requires `sudo` privileges to run due to the use of `hcitool`. Please review the code before running it on your system. The effectiveness of the RSSI measurement can be affected by physical obstacles and interference.
