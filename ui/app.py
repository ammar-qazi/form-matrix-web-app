from nicegui import ui, Client
from core.connection_manager import ConnectionManager
import asyncio
from data.default_data import get_default_data
from ui.components.question_section import QuestionSection
from ui.components.results_section import ResultsSection
from ui.components.action_section import ActionSection
from config.settings import LIGHT_THEME, DARK_THEME, BUTTON_CLASSES, TEXT_CLASSES

class VDATriggerMatrix:
    def __init__(self):
        self.dark_mode = False
        self.base_questions = [
            "1) Is it a change?",
            "2) Does it apply to Special Characteristics towards the customer?",
            "3) Does it apply to the technical interface to the customer?",
            "4) Change type?",
            "5) Does it apply to contract documents?",
            "6) Does it apply to fit, form, function, performance, reliability?"
        ]
        self.section_question = "Section:"
        self.trigger_matrix = self.initialize_data()
        self.filtered_data = self.trigger_matrix.copy()
        self.selected_answers = [None] * (len(self.base_questions) + 1)
        
        # Create UI Components
        self.action_section = ActionSection()
        self.results_section = ResultsSection()
        self.question_section = None
        
        # Set up component relationships
        self.results_section.set_action_section(self.action_section)
        
        # Connection manager
        self.connection_manager = ConnectionManager()

    def initialize_data(self):
        """Initialize and preprocess the trigger matrix data"""
        try:
            matrix = get_default_data()
            # Replace N/A with None
            for column in matrix.columns:
                matrix.data[column] = [None if x == 'N/A' else x for x in matrix.data[column]]
            return matrix
        except Exception as e:
            raise

    def _update_filtered_data(self):
        """Update filtered data based on selected answers"""
        # Create a dictionary of column-value pairs for non-None answers
        conditions = {}
        for idx, answer in enumerate(self.selected_answers):
            if answer is not None:
                column = self.trigger_matrix.columns[idx]
                conditions[column] = answer
        
        # Apply all filters at once
        self.filtered_data = self.trigger_matrix.filter_multiple(conditions)
        

    def toggle_theme(self):
        """Toggle between light and dark themes"""
        self.dark_mode = not self.dark_mode
        # Update UI colors based on theme
        ui.colors(**(DARK_THEME if self.dark_mode else LIGHT_THEME))
        # Update theme toggle button icon
        self.theme_button.props(f'icon={("light_mode" if self.dark_mode else "dark_mode")}')

    def handle_answer(self, question_index, answer):
        self.selected_answers[question_index] = answer
        self._update_filtered_data()
        self.question_section.update_button_styles(question_index, answer)
        
        # Check if we should show section question after each answer
        show_section = self.question_section.should_show_section(self.selected_answers)
        if self.question_section.section_container:
            self.question_section.section_container.visible = show_section
        
        # If we're hiding section, clear its answer
        if not show_section and question_index < 6:
            self.selected_answers[6] = None
            for button, _ in self.question_section.section_buttons:
                button.classes(remove=BUTTON_CLASSES['selected'])
                button.classes(add=BUTTON_CLASSES['unselected'])
        
        self.results_section.update_results(self.filtered_data, self.selected_answers)
    
    def reset(self):
        """Reset the application to its initial state"""
        # Reset answers and data
        self.selected_answers = [None] * (len(self.base_questions) + 1)
        self.filtered_data = self.trigger_matrix.copy()
        
        # Reset UI components
        self.question_section.reset_buttons()
        self.results_section.update_results(self.filtered_data, self.selected_answers)
        self.action_section.clear_action()

    def create_ui(self):
        # Apply material theme
        ui.colors(**(DARK_THEME if self.dark_mode else LIGHT_THEME))

        with ui.column().classes('w-full min-h-screen bg-background'):
            # Header
            with ui.row().classes('w-full items-center p-4 justify-between bg-surface'):
                with ui.row().classes('gap-4 items-center'):
                    ui.button(
                        'Start Over',
                        on_click=self.reset,
                        icon='refresh'
                    ).classes('bg-error text-on-error hover:bg-opacity-90 rounded shadow-sm')
                    ui.label('VDA Trigger Matrix Questions').classes(TEXT_CLASSES['title'] + ' !mb-0')
                self.theme_button = ui.button(
                    icon='dark_mode',
                    on_click=self.toggle_theme
                ).classes('bg-surface-variant text-on-surface hover:bg-opacity-90 rounded')
            
            with ui.splitter(horizontal=False, reverse=False, value=35).classes('w-full bg-background !border-0') as h_splitter:
                with h_splitter.before:
                    with ui.scroll_area().classes('w-full h-[calc(100vh-4rem)] p-4 bg-background'):
                        self.question_section = QuestionSection(
                            self.base_questions,
                            self.trigger_matrix,
                            self.handle_answer
                        )
                        self.question_section.create()

                with h_splitter.after:
                    with ui.column().classes('w-full h-[calc(100vh-4rem)]'):
                        with ui.splitter(horizontal=False, reverse=False, value=60).classes('w-full bg-background !border-0') as h_splitter_2:
                            with h_splitter_2.before:
                                self.results_section.create()
                            
                            with h_splitter_2.after:
                                self.action_section.create()

@ui.page('/')
async def create_app(client: Client):
    app = VDATriggerMatrix()
    
    # Start monitoring this client's connection
    asyncio.create_task(app.connection_manager.monitor_connection(client))
    
    # Create the UI
    app.create_ui()
    return app
