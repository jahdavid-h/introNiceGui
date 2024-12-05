from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('Quieres ver', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=20).bind_value(demo, 'number')
    ui.toggle({1: 'Programacion Orienta', 2: 'Algebra Lienal', 3: 'Calculo Integral'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()