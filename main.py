import os
import sys
from nicegui import ui, native, Client
from ui.app import create_app

# Add the project root directory to Python path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

if __name__ in {"__main__", "__mp_main__"}:
    # Configure UI
    ui.query('body').classes('p-0 m-0')
    ui.query('.nicegui-content').classes('w-full max-w-none p-0')
    
    # Define the main page with client handling
    @ui.page('/')
    async def main_page(client: Client):
        app = await create_app(client)
        return app
    
    # Run with minimal configuration
    ui.run(
        title="VDA Trigger Matrix",
        port=native.find_open_port(),
        show=True,
        reload=False,
        native=False,
        log_config=None  # Tell uvicorn to use its default logging config
    )
