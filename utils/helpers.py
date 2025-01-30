import sys
import os

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_symbol_message(symbol):
    """Returns the message associated with a given symbol"""
    messages = {
        '-': "Customer involvement not required (Note: PPA documentation must be internally archived)",
        'I': "Customer must be informed. In accordance with IATF 16949, the customer must be granted a term of 2 weeks to provide a statement.",
        'A': "Customer agreement required, execution of PPA procedure",
        'U': "Not Applicable (See Trigger Matrix)"
    }
    return messages.get(symbol, f"Unknown symbol: {symbol}")