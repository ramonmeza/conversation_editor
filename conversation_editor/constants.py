import dearpygui.dearpygui as dpg
import shortcuts

from custom_types import NodeSize, namedtuple

# constants
PRIMARY_WINDOW_TAG: str = "Primary Window"
NODE_EDITOR_TAG: str = "Node Editor"
NODE_SIZE: namedtuple = NodeSize(275, 250)

SHORTCUT_METHODS: dict = {
    dpg.mvKey_N: shortcuts.create_new_project,
    dpg.mvKey_O: shortcuts.open_project,
    dpg.mvKey_S: shortcuts.save_project,
    dpg.mvKey_W: shortcuts.exit_application,
    dpg.mvKey_Z: shortcuts.undo_operation,
    dpg.mvKey_Y: shortcuts.redo_operation,
}
