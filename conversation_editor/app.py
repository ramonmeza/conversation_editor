import dearpygui.dearpygui as dpg


PRIMARY_WINDOW_TAG: str = 'Primary Window'


def main() -> None:
    dpg.create_context()

    dpg.create_viewport(title='Custom Title', width=800, height=600)

    with dpg.window(tag=PRIMARY_WINDOW_TAG):
        with dpg.menu_bar():
            with dpg.menu(label='File'):
                dpg.add_menu_item(label='New')
                dpg.add_separator()
                dpg.add_menu_item(label='Open')
                dpg.add_separator()
                dpg.add_menu_item(label='Save')
                dpg.add_menu_item(label='Save As')
                dpg.add_separator()
                dpg.add_menu_item(label='Exit')

        with dpg.node_editor():
            pass

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(PRIMARY_WINDOW_TAG, True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    main()
