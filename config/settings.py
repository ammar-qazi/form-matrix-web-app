# UI Theme configuration
LIGHT_THEME = {
    'primary': '#1976D2',
    'secondary': '#424242',
    'error': '#B00020',
    'background': '#FFFFFF',
    'surface': '#F5F5F5',
    'surface-variant': '#E0E0E0',
    'on-surface': '#000000',
    'on-primary': '#FFFFFF',
    'on-secondary': '#FFFFFF',
    'on-error': '#FFFFFF'
}

DARK_THEME = {
    'primary': '#64B5F6',  # More vibrant blue
    'secondary': '#78909C',  # Slightly darker for better contrast
    'error': '#FF5252',  # Brighter error color
    'background': '#121212',  # Darker background
    'surface': '#1E1E1E',  # Darker surface
    'surface-variant': '#2A2A2A',  # Better contrast with surface
    'on-surface': '#E0E0E0',  # Softer white for better eye comfort
    'on-primary': '#000000',
    'on-secondary': '#000000',
    'on-error': '#000000'
}

# Default to light theme
UI_COLORS = LIGHT_THEME

# Connection timeout settings
CONNECTION_TIMEOUT_SECONDS = 3

# Button style classes
BUTTON_CLASSES = {
    'default': 'bg-surface text-on-surface hover:bg-surface-variant transition-all duration-200 px-4 py-2 rounded',
    'selected': 'bg-primary text-on-primary font-bold shadow-lg transform scale-105 border-2 border-primary transition-all duration-200 px-4 py-2 rounded',
    'unselected': 'bg-surface text-on-surface hover:bg-surface-variant transition-all duration-200 px-4 py-2 rounded',
    'action': 'mt-2 bg-secondary text-on-secondary hover:bg-opacity-90 transition-all duration-200 px-4 py-2 rounded shadow-sm'
}

# Card style classes
CARD_CLASSES = {
    'question': 'w-full mb-1 p-3 bg-surface-variant border-l-4 border-primary rounded-r shadow-sm',
    'results': 'w-full mb-2 p-4 bg-surface hover:bg-surface-variant transition-colors rounded shadow-sm',
    'action': 'w-full p-6 bg-surface-variant rounded shadow-sm'
}

# Layout classes
LAYOUT_CLASSES = {
    'container': 'w-full h-[100vh] bg-background',
    'header': 'w-full items-center p-4 bg-surface shadow-sm',
    'content': 'w-full h-[calc(100vh-4rem)] overflow-auto px-4 py-2'
}

# Text style classes
TEXT_CLASSES = {
    'title': 'text-h6 mb-2 text-on-surface font-semibold',
    'subtitle': 'text-h5 ml-2 text-primary font-medium',
    'body': 'text-body1 text-on-surface',
    'secondary': 'text-body1 text-secondary',
    'error': 'text-error font-medium'
}
