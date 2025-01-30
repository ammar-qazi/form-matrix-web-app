import os
import asyncio
from nicegui import Client

class ConnectionManager:
    def __init__(self):
        self._shutdown_initiated = False
    
    async def _perform_shutdown(self):
        """Handle the shutdown procedure"""
        if self._shutdown_initiated:
            return
            
        self._shutdown_initiated = True
        try:
            await asyncio.sleep(1)  # Give time for cleanup
            os._exit(0)
        except Exception:
            os._exit(1)

    async def monitor_connection(self, client: Client):
        """Monitor a client's connection status"""
        try:
            await client.disconnected()
            await self._perform_shutdown()
        except Exception:
            await self._perform_shutdown()
