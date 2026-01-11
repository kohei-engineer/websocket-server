from server import WebSocketServer
from window import TkinterWindow


def main() -> None:
    """Start WebSocket server and Tkinter GUI."""
    server = WebSocketServer(host="127.0.0.1", port=8000)
    server.start()
    window = TkinterWindow()
    window.run()


if __name__ == "__main__":
    main()
