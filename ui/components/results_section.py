from nicegui import ui
from config.settings import CARD_CLASSES, TEXT_CLASSES, BUTTON_CLASSES
from utils.helpers import get_symbol_message

class ResultsSection:
    def __init__(self, action_section=None):
        self.container = None
        self.action_section = action_section
    
    def set_action_section(self, action_section):
        self.action_section = action_section
    
    def create(self):
        self.container = ui.card().classes('w-full h-[calc(100vh-4rem)] p-6 bg-surface mb-1 shadow-sm')
        with self.container:
            with ui.row().classes('items-center gap-2 mb-4'):
                ui.icon('filter_list', color='primary')
                ui.label('Filtered Results').classes(TEXT_CLASSES['title'] + ' !mb-0')
            ui.label('Select filters to see results').classes(TEXT_CLASSES['secondary'])
    
    def show_action(self, row):
        if self.action_section:
            self.action_section.show_action(
                line=row['Line'],
                symbol=row['Symbol'],
                message=get_symbol_message(row['Symbol'])
            )
    
    def update_results(self, filtered_data, selected_answers=None):
        """Update the results section based on filtered data and selected answers"""
        self.container.clear()
        with self.container:
            with ui.row().classes('items-center gap-2 mb-4'):
                ui.icon('filter_list', color='primary')
                ui.label('Filtered Results').classes(TEXT_CLASSES['title'] + ' !mb-0')
            
            # Show initial state if no answers are selected
            if selected_answers is None or all(answer is None for answer in selected_answers):
                ui.label('Select filters to see results').classes(TEXT_CLASSES['secondary'])
            elif not filtered_data.empty:
                with ui.scroll_area().classes('h-[calc(100vh-12rem)] pr-2'):
                    rows = filtered_data.get_rows()
                    with ui.row().classes('items-center gap-2 mb-4 text-secondary'):
                        ui.icon('info')
                        ui.label(f'Found {len(rows)} results').classes('text-sm')
                    
                    for row in rows:
                        with ui.card().classes(CARD_CLASSES['results'] + ' hover:shadow-md transition-all duration-200'):
                            with ui.column().classes('w-full gap-3'):
                                with ui.row().classes('items-center gap-2'):
                                    ui.label(f"Line {row['Line']}").classes('text-sm font-bold text-primary')
                                ui.label(row['Result']).classes('text-sm text-on-surface')
                                ui.button(
                                    'View Action',
                                    on_click=lambda r=row: self.show_action(r),
                                    icon='arrow_forward'
                                ).classes(BUTTON_CLASSES['action'])
            else:
                with ui.row().classes('items-center gap-2 mt-4'):
                    ui.icon('warning', color='error')
                    ui.label('No results found').classes(TEXT_CLASSES['error'])
