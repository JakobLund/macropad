"""Hotkeys for switching between desktop apps."""
from utils.byte_code_sender import ByteCodeSender

try:
    from typing import Optional
except ImportError:
    pass

from utils.bytecodes import ByteCodesEnum
from apps.chrome import ChromeApp
from apps.spotify import SpotifyApp
from utils.app_pad import AppPad
from utils.apps.key import Key, KeyApp, KeyAppSettings, MacroKey, ByteKey
from utils.commands import (
    ConsumerControlCode,
    Keycode,
    MacroCommand,
    Media,
    Press,
    PreviousAppCommand,
    Release,
    Sequence,
    SwitchAppCommand,
    Wait, ByteCode,
)
from utils.constants import (
    COLOR_GREEN,
    COLOR_RED,
    COLOR_BACK,
    COLOR_CHROME,
    COLOR_CODE,
    COLOR_FILES,
    COLOR_NOTION,
    COLOR_PYCHARM,
    COLOR_SLACK,
    COLOR_SPOTIFY,
    COLOR_SUBLIME_MERGE,
    COLOR_TERMINAL,
    OS_MAC,
    COLOR_DISCORD,
    COLOR_NAV,
    COLOR_WINMAN,
    COLOR_MEDIA,
    COLOR_PYCHARM,
    COLOR_LINUX,
)
import utils.constants


class ScriptsApp(KeyApp):
    """
    App with commands for switching between desktop apps. Some desktop apps
    also have a context-specific app for that desktop app. These will display
    when you switch to the app with the hotkey.
    """

    name = "Scripts"

    key_2 = Key(
        "Back",
        COLOR_BACK,
        PreviousAppCommand(),
        double_tap_command=PreviousAppCommand(),
    )

    key_11 = Key("Replay", COLOR_PYCHARM, Press(Keycode.CONTROL, Keycode.F6))

    encoder_button = Media(ConsumerControlCode.MUTE)

    encoder_increase = Media(ConsumerControlCode.VOLUME_INCREMENT)
    encoder_decrease = Media(ConsumerControlCode.VOLUME_DECREMENT)

    def __init__(self, app_pad: AppPad, settings: Optional[KeyAppSettings] = None):
        self.byte_code_sender = ByteCodeSender()
        self.initialize_settings_dependent_keys(app_pad, self.byte_code_sender, settings)
        super().__init__(app_pad, settings=settings)

    @classmethod
    def initialize_settings_dependent_keys(
            cls, app_pad: AppPad, byte_code_sender: ByteCodeSender, settings: Optional[KeyAppSettings] = None
    ):
        chrome_app = ChromeApp(app_pad, settings)
        spotify_app = SpotifyApp(app_pad, settings)

        cls.key_3 = ByteKey(
            "PS On",
            COLOR_GREEN,
            ByteCode(byte_code_sender, ByteCodesEnum.CODE_PS5_ON),

        )
        cls.key_6 = ByteKey(
            "PS Off",
            COLOR_RED,
            ByteCode(byte_code_sender, ByteCodesEnum.CODE_PS5_OFF),
        )

        cls.key_4 = ByteKey(
            "Speakers",
            COLOR_WINMAN,
            ByteCode(byte_code_sender, ByteCodesEnum.CODE_CHANGE_TO_SPEAKERS),
        )

        cls.key_7 = ByteKey(
            "Headset",
            COLOR_NAV,
            ByteCode(byte_code_sender, ByteCodesEnum.CODE_CHANGE_TO_HEADSET),
        )

        cls.key_5 = ByteKey(
            "BD Fix",
            COLOR_DISCORD,
            ByteCode(byte_code_sender, ByteCodesEnum.CODE_INSTALL_BETTER_DISCORD),
        )

        cls.key_8 = ByteKey(
            "Stream",
            COLOR_MEDIA,
            ByteCode(byte_code_sender, ByteCodesEnum.CODE_RESTART_DISCORD_STREAM),
        )

        cls.key_9 = ByteKey(
            "RTX",
            COLOR_LINUX,
            ByteCode(byte_code_sender, ByteCodesEnum.CODE_CHANGE_TO_RTX),
        )

        cls.key_10 = ByteKey(
            "VR",
            COLOR_MEDIA,
            ByteCode(byte_code_sender, ByteCodesEnum.CODE_CHANGE_TO_VR),
        )

        cls.key_11 = ByteKey(
            "Replay",
            COLOR_PYCHARM,
            ByteCode(byte_code_sender, ByteCodesEnum.CODE_SAVE_REPLAY),
        )
