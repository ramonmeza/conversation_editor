import dearpygui.dearpygui as dpg

from constants import SHORTCUT_METHODS
from typing import Any


# methods
def shortcut_callback(sender: int, app_data: Any, user_data: int) -> None:
    modifier_key: int = user_data
    shortcut_key: int = app_data
    if modifier_key and dpg.is_key_down(modifier_key):
        SHORTCUT_METHODS[shortcut_key]()
