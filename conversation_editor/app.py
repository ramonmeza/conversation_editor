import dearpygui.dearpygui as dpg

from collections import namedtuple

from core.attribute_comparison_node import ComparisonOperators


# types
NodeSize: namedtuple = namedtuple('NodeSize', ['x', 'y'])
Position: namedtuple = NodeSize

# constants
PRIMARY_WINDOW_TAG: str = 'Primary Window'
NODE_EDITOR_TAG: str = 'Node Editor'

NODE_SIZE: NodeSize = NodeSize(275, 250)


# methods
def main() -> None:
    dpg.create_context()

    dpg.create_viewport(title='Custom Title', width=800, height=600)

    with dpg.window(tag=PRIMARY_WINDOW_TAG):
        with dpg.menu_bar():
            with dpg.menu(label='File'):
                dpg.add_menu_item(label='New', shortcut='Ctrl+N')
                dpg.add_separator()
                dpg.add_menu_item(label='Open', shortcut='Ctrl+O')
                dpg.add_separator()
                dpg.add_menu_item(label='Save', shortcut='Ctrl+S')
                dpg.add_menu_item(label='Save As', shortcut='Ctrl+Shift+S')
                dpg.add_separator()
                dpg.add_menu_item(label='Exit')
            with dpg.menu(label='Edit'):
                dpg.add_menu_item(label='Undo', shortcut='Ctrl+Z')
                dpg.add_menu_item(label='Redo', shortcut='Ctrl+Y')
                dpg.add_separator()
                with dpg.menu(label='Nodes'):
                    dpg.add_menu_item(label='Add Talk Node', shortcut='Ctrl+T')
                    dpg.add_menu_item(label='Add Attribute Comparison Node', shortcut='Ctrl+A')
                    dpg.add_menu_item(label='Delete Selected', shortcut='Delete')
                dpg.add_separator()
                dpg.add_menu_item(label='Preferences')

        with dpg.node_editor(tag=NODE_EDITOR_TAG, minimap=True, minimap_location=dpg.mvNodeMiniMap_Location_TopRight):
            add_talk_node(Position(0, 0))
            add_attribute_comparison_node(Position(500, 120))

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.set_primary_window(PRIMARY_WINDOW_TAG, True)
    dpg.start_dearpygui()
    dpg.destroy_context()

def add_talk_node(pos: Position = Position(0, 0)) -> None:
    node_id: int = dpg.add_node(parent=NODE_EDITOR_TAG, label='Talk Node', pos=pos)

    # inputs
    dpg.add_node_attribute(parent=node_id)

    # node attributes
    attr_id: int = dpg.add_node_attribute(parent=node_id, attribute_type=dpg.mvNode_Attr_Static)
    dpg.add_input_text(label='Speaker', parent=attr_id, width=NODE_SIZE.x)
    dpg.add_input_text(label='Text', parent=attr_id, multiline=True, width=NODE_SIZE.x, height=NODE_SIZE.y)

    # responses
    attr_id = dpg.add_node_attribute(parent=node_id, attribute_type=dpg.mvNode_Attr_Output)
    group_id: int = dpg.add_group(parent=attr_id, horizontal=True)
    dpg.add_spacer(parent=group_id, width=NODE_SIZE.x)
    dpg.add_text('Responses', parent=group_id)

def add_attribute_comparison_node(pos: Position = Position(0, 0)) -> None:
    node_id: int = dpg.add_node(parent=NODE_EDITOR_TAG, label='Attribute Comparison Node', pos=pos)

    # inputs
    dpg.add_node_attribute(parent=node_id)

    # node attributes
    attr_id: int = dpg.add_node_attribute(parent=node_id, attribute_type=dpg.mvNode_Attr_Static)
    group_id: int = dpg.add_group(parent=attr_id, horizontal=True)
    dpg.add_input_text(parent=group_id, width=100)
    dpg.add_combo(parent=group_id, items=ComparisonOperators, default_value=ComparisonOperators[0], width=40)
    dpg.add_input_int(parent=group_id, width=100)

    # true response
    attr_id = dpg.add_node_attribute(parent=node_id, attribute_type=dpg.mvNode_Attr_Output)
    group_id = dpg.add_group(parent=attr_id, horizontal=True)
    dpg.add_spacer(parent=group_id, width=221)
    dpg.add_text('True', parent=group_id)

    # false response
    attr_id = dpg.add_node_attribute(parent=node_id, attribute_type=dpg.mvNode_Attr_Output)
    group_id = dpg.add_group(parent=attr_id, horizontal=True)
    dpg.add_spacer(parent=group_id, width=214)
    dpg.add_text('False', parent=group_id)


# app entry
if __name__ == '__main__':
    main()
