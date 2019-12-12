# Maverick Joystick
This library is for the ChenGong joystick. Below are the details for this device:

```
idVendor=0x0416
idProduct=0xb001
```
## How to Run
1. Using pip, install `pyusb`
```
pip install pyusb
```
2. Copy and paste the `*udev.rules file ` into `/etc/udev/rules.d`
```
sudo cp 50-chengong-joystick-udev.rules /etc/udev/rules.d/
```
3. Run the python file
```
python joystick_test.py
```