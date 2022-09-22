import dearpygui.dearpygui as dpg


# methods
def create_new_project() -> None:
    raise NotImplementedError('create_new_project')

def open_project() -> None:
    raise NotImplementedError('open_project')

def save_project() -> None:
    raise NotImplementedError('save_project')

def exit_application() -> None:
    raise NotImplementedError('exit_application')

def undo_operation() -> None:
    raise NotImplementedError('undo_operation')

def redo_operation() -> None:
    raise NotImplementedError('redo_operation')
