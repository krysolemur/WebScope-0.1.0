# main.py

import sys
import traceback
import signal

from Application.Logger.Logger import Logger
from Application.Application import Application

logger = Logger()

def main() -> None:
    # Allow Ctrl+C to work properly with Qt
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    try:
        # Create app, run end exec
        app = Application()
        app.run() 
        sys.exit(app.exec())
        
    except KeyboardInterrupt:
        # Clean exit on Ctrl+C
        print("\nApplication stopped.")
        sys.exit(0)
        
    except Exception:
        # Log unexpected errors
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()