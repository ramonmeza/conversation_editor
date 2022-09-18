import dearpygui.dearpygui as dpg


PRIMARY_WINDOW_TAG: str = 'Primary Window'


def main() -> None:
    dpg.create_context()

    with dpg.window(tag=PRIMARY_WINDOW_TAG):
        dpg.add_text('Hello, world!')

    dpg.setup_dearpygui()
    dpg.create_viewport(title='Conversation Editor', width=800, height=600)
    dpg.set_primary_window(PRIMARY_WINDOW_TAG, True)
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    main()
