from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz Click', on_click=lambda: ui.notify('Clic'))
with ui.row():
    ui.checkbox('Pepsi', on_change=show)
    ui.switch('Activo', on_change=show)
ui.radio(['Pizza', 'Tacos', 'Piña'], value='Pizza', on_change=show).props('inline')
with ui.row():
    ui.input('Ingresa su Nombre', on_change=show)
    ui.select(['2005', '2001'], value='2001', on_change=show)
ui.link('And many more...', '/documentation').classes('mt-8')

ui.run()