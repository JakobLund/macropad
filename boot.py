import storage
import usb_cdc

storage.remount("/", False)
usb_cdc.enable(console=True, data=True)
