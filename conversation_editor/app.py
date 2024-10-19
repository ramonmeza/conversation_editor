import dearpygui.dearpygui as dpg

from callbacks import shortcut_callback
from constants import NODE_EDITOR_TAG, NODE_SIZE, PRIMARY_WINDOW_TAG
from core.attribute_comparison_node import ComparisonOperators
from custom_types import Position, namedtuple


# methods
def main() -> None:
    dpg.create_context()
    dpg.configure_app(manual_callback_management=True)

    dpg.create_viewport(title="Custom Title", width=800, height=600)

    with dpg.window(tag=PRIMARY_WINDOW_TAG):
        with dpg.handler_registry():
            dpg.add_key_release_handler(
                dpg.mvKey_N, user_data=dpg.mvKey_LControl, callback=shortcut_callback
            )
            dpg.add_key_release_handler(
                dpg.mvKey_O, user_data=dpg.mvKey_LControl, callback=shortcut_callback
            )
            dpg.add_key_release_handler(
                dpg.mvKey_S, user_data=dpg.mvKey_LControl, callback=shortcut_callback
            )
            dpg.add_key_release_handler(
                dpg.mvKey_W, user_data=dpg.mvKey_LControl, callback=shortcut_callback
            )
            dpg.add_key_release_handler(
                dpg.mvKey_Z, user_data=dpg.mvKey_LControl, callback=shortcut_callback
            )
            dpg.add_key_release_handler(
                dpg.mvKey_Y, user_data=dpg.mvKey_LControl, callback=shortcut_callback
            )

        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="New", shortcut="Ctrl+N")
                dpg.add_separator()
                dpg.add_menu_item(label="Open", shortcut="Ctrl+O")
                dpg.add_separator()
                dpg.add_menu_item(label="Save", shortcut="Ctrl+S")
                dpg.add_separator()
                dpg.add_menu_item(label="Exit", shortcut="Ctrl+W")
            with dpg.menu(label="Edit"):
                dpg.add_menu_item(label="Undo", shortcut="Ctrl+Z")
                dpg.add_menu_item(label="Redo", shortcut="Ctrl+Y")
                dpg.add_separator()
                with dpg.menu(label="Nodes"):
                    dpg.add_menu_item(label="Add Talk Node", shortcut="Ctrl+T")
                    dpg.add_menu_item(
                        label="Add Attribute Comparison Node", shortcut="Ctrl+A"
                    )
                    dpg.add_menu_item(label="Delete Selected", shortcut="Delete")
                dpg.add_separator()
                dpg.add_menu_item(label="Preferences")

        with dpg.node_editor(
            tag=NODE_EDITOR_TAG,
            minimap=True,
            minimap_location=dpg.mvNodeMiniMap_Location_TopRight,
        ):
            # with dpg.node(label="Talk"):
            #     with dpg.node_attribute(label="Speaker"):
            #         dpg.add_text()

            # node_id = dpg.add_node(label="Talk")
            # nodeattr_id = dpg.add_node_attribute(label="Speaker", parent=node_id)
            # dpg.add_text(parent=nodeattr_id)

            add_talk_node(Position(550, 0))
            add_attribute_comparison_node(Position(500, 120))

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.set_primary_window(PRIMARY_WINDOW_TAG, True)

    while dpg.is_dearpygui_running():
        jobs = dpg.get_callback_queue()
        dpg.run_callbacks(jobs)
        dpg.render_dearpygui_frame()

    dpg.destroy_context()


def add_talk_node(pos: namedtuple = Position(0, 0)) -> None:
    node_id = dpg.add_node(label="Talk")

    # inputs
    node_attr = dpg.add_node_attribute(parent=node_id)
    dpg.add_text(parent=node_attr)

    # node attributes
    attr_id: int = dpg.add_node_attribute(
        parent=node_id, attribute_type=dpg.mvNode_Attr_Static
    )
    dpg.add_input_text(label="Speaker", parent=attr_id, width=NODE_SIZE.x)
    dpg.add_input_text(
        label="Text",
        parent=attr_id,
        multiline=True,
        width=NODE_SIZE.x,
        height=NODE_SIZE.y,
    )

    # responses
    attr_id = dpg.add_node_attribute(
        parent=node_id, attribute_type=dpg.mvNode_Attr_Output
    )
    group_id: int = dpg.add_group(parent=attr_id, horizontal=True)
    dpg.add_spacer(parent=group_id, width=NODE_SIZE.x)
    dpg.add_text("Responses", parent=group_id)


def add_attribute_comparison_node(pos: namedtuple = Position(0, 0)) -> None:
    node_id: int = dpg.add_node(label="Attribute Comparison Node", pos=pos)

    # inputs
    node_attr = dpg.add_node_attribute(parent=node_id)
    dpg.add_text(parent=node_attr)

    # node attributes
    attr_id: int = dpg.add_node_attribute(
        parent=node_id, attribute_type=dpg.mvNode_Attr_Static
    )
    group_id: int = dpg.add_group(parent=attr_id, horizontal=True)
    dpg.add_input_text(parent=group_id, width=100)
    dpg.add_combo(
        parent=group_id,
        items=ComparisonOperators,
        default_value=ComparisonOperators[0],
        width=40,
    )
    dpg.add_input_int(parent=group_id, width=100)

    # true response
    attr_id = dpg.add_node_attribute(
        parent=node_id, attribute_type=dpg.mvNode_Attr_Output
    )
    group_id = dpg.add_group(parent=attr_id, horizontal=True)
    dpg.add_spacer(parent=group_id, width=221)
    dpg.add_text("True", parent=group_id)

    # false response
    attr_id = dpg.add_node_attribute(
        parent=node_id, attribute_type=dpg.mvNode_Attr_Output
    )
    group_id = dpg.add_group(parent=attr_id, horizontal=True)
    dpg.add_spacer(parent=group_id, width=214)
    dpg.add_text("False", parent=group_id)


# app entry
if __name__ == "__main__":
    main()
