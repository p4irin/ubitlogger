![PyPI - Version](https://img.shields.io/pypi/v/ubitlogger)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ubitlogger)
![PyPI - License](https://img.shields.io/pypi/l/ubitlogger)
[![Static Badge](https://img.shields.io/badge/microbit-v1.3x-blue?logo=microbit&link=https%3A%2F%2Ftech.microbit.org%2Fhardware%2F1-3-revision%2F)](https://tech.microbit.org/hardware/1-3-revision/)
[![Static Badge](https://img.shields.io/badge/Ubuntu-22.04_LTS_jammy-orange?logo=ubuntu)](https://ubuntu.com/download/server)
[![Static Badge](https://img.shields.io/badge/Raspberry_Pi-4B_8GB-red?logo=raspberrypi&logoColor=red)](https://www.raspberrypi.com/products/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
# ubitlogger

A micro:bit serial port logger

## Using ubitlogger from a linux distro on WSL 2

Connect a USB device to your linux distro on WSL 2 using [usbipd-win](https://github.com/dorssel/usbipd-win)

List USB devices

```powershell
PS C:\Users\p4irin> usbipd list --usbids

Connected:
BUSID  VID:PID  DEVICE                          STATE
1-1    046d:c534  Logitech, Inc., NanoReceiver  Not shared
1-3    0d28:0204  NXP, ARM  mbed                Not Shared
...
```

Register/bind a USB device for sharing. Device "NXP, ARM mbed" with busid _1-3_ identifies our micro:bit:

```powershell
PS C:\Users\p4irin> usbipd bind --busid 1-3
```

If you list USB devices again, the microbit wil show up as _Shared_:

```powershell
PS C:\Users\p4irin> usbipd list --usbids

Connected:
BUSID  VID:PID  DEVICE                          STATE
1-1    046d:c534  Logitech, Inc., NanoReceiver  Not shared
1-3    0d28:0204  NXP, ARM  mbed                Shared
...
PS C:\Users\p4irin>
```

Attach the USB device to WSL:

```powershell
PS C:\Users\p4irin> usbipd attach --wsl --busid 1-3

usbipd: info: Using WSL distribution 'Ubuntu-22.04' to attach; the device will be available in all WSL 2 distributions.
usbipd: info: Using IP address 172.21.144.1 to reach the host.

PS C:\Users\p4irin>
```

In your WSL distro's terminal, check if the micro:bit is listed:

```bash
$ lsusb
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 004: ID 0d28:0204 NXP ARM mbed
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
$
```

Now run _ubitlogger_ in your Python virtualenv:

```bash
(venv) $ ubitlogger start -d -t 3

Found a micro:bit on: /dev/ttyACM0
Listening on port /dev/ttyACM0
Baudrate: 115200
Data bits: 8
Stop bits: 1
Parity: N
timeout: 3.0
18 17
18 6
^C
Exited by CTRL-C
Cleaning up thread
--> Waiting for thread to finish.

(venv) $
```

Listing USB devices will show the micro:bit attached:

```powershell
PS C:\Users\p4irin> usbipd list --usbids

Connected:
BUSID  VID:PID  DEVICE                          STATE
1-1    046d:c534  Logitech, Inc., NanoReceiver  Not shared
1-3    0d28:0204  NXP, ARM  mbed                Attached
...
PS C:\Users\p4irin>
```


To detach the device from WSL:

```powershell
PS C:\Users\p4irin> usbipd detach --busid 1-3
```