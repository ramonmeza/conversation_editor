import dearpygui.dearpygui as dpg

from collections import namedtuple

from core.attribute_comparison_node import ComparisonOperators


# types
NodeSize: namedtuple = namedtuple('NodeSize', ['x', 'y'])

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
                    dpg.add_menu_item(label='Add Node', shortcut='Ctrl+A')
                    dpg.add_menu_item(label='Delete Selected', shortcut='Delete')
                dpg.add_separator()
                dpg.add_menu_item(label='Preferences')

        with dpg.node_editor(tag=NODE_EDITOR_TAG, minimap=True, minimap_location=dpg.mvNodeMiniMap_Location_TopRight):
            with dpg.node(label='Talk Node'):
                # inputs
                with dpg.node_attribute():
                    pass

                # talk node attributes
                with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                    dpg.add_input_text(label='Speaker', width=NODE_SIZE.x)
                    dpg.add_input_text(label='Text', multiline=True, width=NODE_SIZE.x, height=NODE_SIZE.y)

                # responses output
                with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                    with dpg.group(horizontal=True):
                        dpg.add_spacer(width=NODE_SIZE.x)
                        dpg.add_text('Responses')

            with dpg.node(label='Attribute Comparison Node'):
                # inputs
                with dpg.node_attribute():
                    pass

                # attribute comparison node attributes
                with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                    with dpg.group(horizontal=True):
                        dpg.add_input_text(width=100)
                        dpg.add_combo(items=ComparisonOperators, default_value=ComparisonOperators[0], width=40)
                        dpg.add_input_int(width=100)

                # true response
                with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                    with dpg.group(horizontal=True):
                        dpg.add_spacer(width=221)
                        dpg.add_text('True')

                # false response
                with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                    with dpg.group(horizontal=True):
                        dpg.add_spacer(width=214)
                        dpg.add_text('False')

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.set_primary_window(PRIMARY_WINDOW_TAG, True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    main()
