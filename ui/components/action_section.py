from nicegui import ui
from config.settings import CARD_CLASSES, TEXT_CLASSES

class ActionSection:
    def __init__(self):
        self.container = None
    
    def create(self):
        self.container = ui.card().classes('w-full h-[calc(100vh-4rem)] p-6 bg-surface shadow-sm')
        self.clear_action()
    
    def clear_action(self):
        self.container.clear()
        with self.container:
            with ui.row().classes('items-center gap-2 mb-4'):
                ui.icon('task_alt', color='primary')
                ui.label('Required Action').classes(TEXT_CLASSES['title'] + ' !mb-0')
            with ui.row().classes('items-center gap-2'):
                ui.icon('info', color='secondary')
                ui.label('Select a result to see required action').classes(TEXT_CLASSES['secondary'])
    
    def show_action(self, line, symbol, message):
        self.container.clear()
        with self.container:
            with ui.row().classes('items-center gap-2 mb-4'):
                ui.icon('task_alt', color='primary')
                ui.label('Required Action').classes(TEXT_CLASSES['title'] + ' !mb-0')
            
            with ui.card().classes(CARD_CLASSES['action'] + ' hover:shadow-md transition-all duration-200'):
                with ui.column().classes('gap-4'):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('format_list_numbered', color='primary')
                        ui.label(f'Line {line}').classes('text-h6 font-semibold text-primary')
                    
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('label', color='secondary')
                        ui.label(f'Symbol: {symbol}').classes('text-body1 text-secondary')
                    
                    with ui.row().classes('items-start gap-2'):
                        ui.icon('info', color='primary').classes('mt-1')
                        ui.label(message).classes('text-body1 text-on-surface')
