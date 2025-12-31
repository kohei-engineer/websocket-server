import tkinter
from server import WebSocketServer

def init_tkinter() -> None:
    """Initialize Tkinter GUI and return the root window."""
    root = tkinter.Tk()
    root.title('WebSocket Server')
    root.geometry('400x300')

    text_widget = tkinter.Text(root, state='disabled')
    text_widget.pack(expand=True, fill='both', padx=5, pady=5)

    root.mainloop()

def main() -> None:
    """main function to start WebSocket server and Tkinter GUI."""
    server = WebSocketServer(host="0.0.0.0", port=8000)
    server.start()
    init_tkinter()

if __name__ == "__main__":
    main()
