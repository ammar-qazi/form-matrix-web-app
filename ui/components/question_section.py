from nicegui import ui
from config.settings import BUTTON_CLASSES, CARD_CLASSES, TEXT_CLASSES

class QuestionSection:
    def __init__(self, questions, trigger_matrix, on_answer):
        self.questions = questions
        self.trigger_matrix = trigger_matrix
        self.on_answer = on_answer
        self.answer_buttons = []
        self.section_buttons = []
        self.section_container = None
        self.selected_answers = [None] * (len(questions) + 1)  # Track selected answers
        
        # Expected answers definitions
        self.optional_answers = {
            0: 'Y',  # Is it a change?
            1: 'N',  # Special Characteristics
            2: 'N'   # Technical interface
        }
        self.mandatory_answers = {
            3: 'Process',  # Change type
            4: 'N',        # Contract documents
            5: 'N'         # Fit, form, function
        }

    def should_show_section(self, selected_answers):
        """
        Determine if section question should be shown based on answers.
        
        Rules:
        1. Mandatory answers (index 3-5) must match expected values
        2. Optional answers (index 0-2) if provided must match expected values
        3. Show section if mandatory answers match and optional answers either match or aren't provided
        """
        # Check if we have enough answers
        if len(selected_answers) < 6:
            return False
            
        # Check mandatory answers first (must all be present and match)
        for idx, expected in self.mandatory_answers.items():
            if selected_answers[idx] != expected:
                return False
        
        # Check optional answers only if they're provided
        for idx, expected in self.optional_answers.items():
            if selected_answers[idx] is not None and selected_answers[idx] != expected:
                return False
        
        # If we get here, all conditions are met
        return True

    def create(self):
        with ui.column().classes('w-full'):
            # Create base questions
            for idx, question in enumerate(self.questions):
                with ui.card().classes(CARD_CLASSES['question'] + ' hover:shadow-md transition-shadow duration-200 !border-l-[6px]'):
                    with ui.row().classes('w-full items-center justify-between'):
                        if idx in self.mandatory_answers:
                            with ui.row().classes('items-center gap-2'):
                                ui.label(question).classes(TEXT_CLASSES['body'])
                                ui.label('*').classes('text-error font-bold')
                        else:
                            ui.label(question).classes(TEXT_CLASSES['body'])
                    
                    current_column = self.trigger_matrix.columns[idx]
                    valid_answers = [x for x in self.trigger_matrix.unique(current_column) if x is not None]
                    valid_answers.sort(reverse=True)
                    
                    question_buttons = []
                    with ui.row().classes('gap-2 flex-wrap mt-2'):
                        for option in valid_answers:
                            btn = ui.button(
                                str(option),
                                on_click=lambda i=idx, o=option: self.handle_button_click(i, o)
                            ).classes(BUTTON_CLASSES['unselected'])
                            question_buttons.append((btn, option))
                    self.answer_buttons.append(question_buttons)
            
            # Add note about mandatory questions
            with ui.card().classes('w-full mb-4 mt-2 p-3 bg-surface-variant rounded shadow-sm'):
                with ui.row().classes('items-center gap-2'):
                    ui.icon('info', color='secondary')
                    ui.label('* Mandatory questions for section selection').classes('text-secondary text-sm')
            
            # Create section question
            self.section_container = ui.card().classes(CARD_CLASSES['question'] + ' hover:shadow-md transition-shadow duration-200 !border-l-[6px]')
            with self.section_container:
                with ui.row().classes('w-full items-center mb-2'):
                    ui.label("Section:").classes(TEXT_CLASSES['body'] + ' font-medium')
                current_column = self.trigger_matrix.columns[6]  # Section column
                valid_answers = [x for x in self.trigger_matrix.unique(current_column) if x is not None]
                valid_answers.sort()
                
                with ui.row().classes('gap-2 flex-wrap mt-2'):
                    for option in valid_answers:
                        btn = ui.button(
                            str(option),
                            on_click=lambda o=option: self.handle_button_click(6, o)
                        ).classes(BUTTON_CLASSES['unselected'])
                        self.section_buttons.append((btn, option))
            
            # Initially hide section container
            self.section_container.visible = False

    def handle_button_click(self, question_index, clicked_answer):
        """Handle button clicks with toggle functionality"""
        # If clicking the same answer that's currently selected, unselect it
        if self.selected_answers[question_index] == clicked_answer:
            self.selected_answers[question_index] = None
            self.on_answer(question_index, None)
        else:
            # Otherwise, select the new answer
            self.selected_answers[question_index] = clicked_answer
            self.on_answer(question_index, clicked_answer)
        
        # Update button styles
        self.update_button_styles(question_index, self.selected_answers[question_index])

    def update_button_styles(self, question_index, selected_answer):
        # Update base question buttons
        if question_index < len(self.answer_buttons):
            for button, btn_answer in self.answer_buttons[question_index]:
                if btn_answer == selected_answer:
                    button.classes(remove=BUTTON_CLASSES['unselected'])
                    button.classes(add=BUTTON_CLASSES['selected'])
                else:
                    button.classes(remove=BUTTON_CLASSES['selected'])
                    button.classes(add=BUTTON_CLASSES['unselected'])
        
        # Update section buttons if it's the section question
        if question_index == 6:
            for button, btn_answer in self.section_buttons:
                if btn_answer == selected_answer:
                    button.classes(remove=BUTTON_CLASSES['unselected'])
                    button.classes(add=BUTTON_CLASSES['selected'])
                else:
                    button.classes(remove=BUTTON_CLASSES['selected'])
                    button.classes(add=BUTTON_CLASSES['unselected'])

    def reset_buttons(self):
        # Reset selected answers
        self.selected_answers = [None] * len(self.selected_answers)
        
        # Reset base question buttons
        for buttons in self.answer_buttons:
            for button, _ in buttons:
                button.classes(remove=BUTTON_CLASSES['selected'])
                button.classes(add=BUTTON_CLASSES['unselected'])
        
        # Reset section buttons
        for button, _ in self.section_buttons:
            button.classes(remove=BUTTON_CLASSES['selected'])
            button.classes(add=BUTTON_CLASSES['unselected'])
        
        # Hide section question
        self.section_container.visible = False
