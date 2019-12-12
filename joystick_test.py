#!/usr/bin/python
import usb

dev = usb.core.find(idVendor=0x0416, idProduct=0xb001)

if dev is None:
  raise ValueError("Joystick not found")

interface = 0
endpoint = dev[0][(0,0)][0]
# if the OS kernel already claimed the device, which is most likely true
# thanks to http://stackoverflow.com/questions/8218683/pyusb-cannot-set-configuration
if dev.is_kernel_driver_active(interface) is True:
  # tell the kernel to detach
  dev.detach_kernel_driver(interface)
  # claim the device
  usb.util.claim_interface(dev, interface)

dev.set_configuration()

try:
  while True:
    print(dev.read(endpoint=0x81, size_or_buffer=6))
except KeyboardInterrupt:
  print("Exiting due to Keyboard Interrupt")
usb.util.release_interface(dev, interface)
dev.attach_kernel_driver(interface)