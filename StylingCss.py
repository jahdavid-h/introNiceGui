from nicegui import ui

ui.icon('thumb_up', color='#d10a0a').classes('text-7xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('DAVID JAHUEY HERNANDEZ').style('color: #0eb7e6; font-family: New Times Roman; font-size: 32px')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()