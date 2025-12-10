import subprocess
import time
import os

MAC = "3C:4D:CC:1C:C6:A5"

def get_rssi(mac):
    try:
        output = subprocess.check_output(
            ["hcitool", "rssi", mac],
            stderr=subprocess.STDOUT,
            text=True
        )
        if "RSSI return value:" in output:
            return int(output.split(":")[1].strip())
    except Exception:
        return None


def lock_screen():
    # Works on GNOME, KDE Plasma, XFCE, LXDE, MATE, Cinnamon, Budgie
    commands = [
        "loginctl lock-session",
        "loginctl lock-session $(loginctl | grep seat0 | awk '{print $1}')",
        "xdg-screensaver lock",
        "dm-tool lock",
        "gnome-screensaver-command -l",
        "qdbus org.freedesktop.ScreenSaver /ScreenSaver Lock"
    ]

    for cmd in commands:
        os.system(cmd)


while True:
    rssi = get_rssi(MAC)

    if rssi is not None:
        print("RSSI:", rssi, "dBm")

        if rssi >= -60:
            lock_screen()

    else:
        print("device might be disconnected")

    time.sleep(1)
