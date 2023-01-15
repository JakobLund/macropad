from adafruit_hid.keycode import Keycode



try:
    from typing import Optional
except ImportError:
    pass
from utils.app_pad import AppPad
from utils.apps.key import (
    Key,
    KeyApp,
    KeyAppSettings,
    SettingsSelectKey,
    SettingsValueKey, HwInfoKey,
)
from utils.commands import (
    ConsumerControlCode,
    Media,
    PreviousAppCommand,
    SwitchAppCommand, Press, HwInfoRefreshException, Text,
)
from utils.constants import (
    COLOR_APPS,
    COLOR_FUNC,
    COLOR_LINUX,
    COLOR_MAC,
    COLOR_MEDIA,
    COLOR_NAV,
    COLOR_NUMPAD,
    COLOR_WINDOWS,
    COLOR_WINMAN,
    COLOR_RED,
    COLOR_GREEN,
    OS_LINUX,
    OS_MAC,
    OS_SETTING,
    OS_WINDOWS,
    HW_INFO_LOW,
    HW_INFO_MEDIUM_LOW,
    HW_INFO_MEDIUM,
    HW_INFO_MEDIUM_HIGH,
    HW_INFO_HIGH,
)


class HwInfoApp(KeyApp):
    name = "Hardware Info"
    key_0 = HwInfoKey(
        "CPU",
        COLOR_APPS,
        command=PreviousAppCommand(),
        double_tap_command=PreviousAppCommand()
    )
    key_1 = HwInfoKey(
        "0",
        COLOR_APPS,
        command=PreviousAppCommand(),
        text_template="{value}%",
        double_tap_command=PreviousAppCommand()
    )
    key_2 = HwInfoKey(
        "0",
        COLOR_APPS,
        command=PreviousAppCommand(),
        text_template="{value} C",
        double_tap_command=PreviousAppCommand()
    )
    key_3 = Key("7", COLOR_NUMPAD, Text("7"), double_tap_command=Text("/"))

    def __init__(self, app_pad: AppPad, settings: Optional[KeyAppSettings] = None):
        super().__init__(app_pad, settings=settings)
        #self.app_pad.listen_to_usb(self)


