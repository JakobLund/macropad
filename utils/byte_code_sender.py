import usb_cdc

from utils.bytecodes import ByteCodesEnum

try:
    from typing import Optional, Union, List, get_args
except ImportError:
    pass


from utils.app_pad import DoubleTapBuffer


class ByteCodeSender:
    """
    Helper class to send bytes over USB to host.
    Used to send codes to a listener application running on the host.

    """

    # TODO: Input link to host app above

    def __init__(self):
        self.serial = usb_cdc.data

        self._timers = dict()

        self._double_tap_buffer: Optional[DoubleTapBuffer] = None

    def get_serial(self):
        return self.serial

    def send_byte_code(self, code: ByteCodesEnum):
        if self.serial.connected and self.serial.out_waiting == 0:
            self.serial.write(code)

    def send_sequence(self, list_of_codes: List[ByteCodesEnum]):
        for code in list_of_codes:
            self.send_byte_code(code)

    def receive_byte_code(self):
        if self.serial.connected:
            self.serial.read()
