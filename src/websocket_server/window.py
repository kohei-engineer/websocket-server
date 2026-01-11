import tkinter as tk
from tkinter import ttk


class TkinterWindow(tk.Tk):
    """Class to create and manage the main Tkinter window."""

    def __init__(self) -> None:
        """Initialize the main Tkinter window and its frames."""
        super().__init__()
        self.title("WebSocket Server")
        self.geometry("800x500")

        self._setup_layout()
        self._setup_frames()

    def _setup_layout(self) -> None:
        """Set up the grid layout for the main window."""
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=8)
        self.columnconfigure(0, weight=1, uniform="x")
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1, uniform="x")

    def _setup_frames(self) -> None:
        """Set up the individual frames within the main window."""
        self.connection_settings_frame = ConnectionSettingsFrame(self)
        self.connection_settings_frame.grid(
            row=0, column=0, columnspan=3, sticky="nsew", padx=5, pady=5
        )

        self.send_message_frame = SendMessageFrame(self)
        self.send_message_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

        self.received_messages_frame = ReceivedMessagesFrame(self)
        self.received_messages_frame.grid(
            row=2, column=2, sticky="nsew", padx=5, pady=5
        )

        horizontal_separator = ttk.Separator(self, orient="horizontal")
        horizontal_separator.grid(row=1, column=0, columnspan=3, sticky="ew")
        vertical_separator = ttk.Separator(self, orient="vertical")
        vertical_separator.grid(row=1, column=1, rowspan=2, sticky="ns")

    def run(self) -> None:
        """Start the Tkinter main loop."""
        self.mainloop()


class ConnectionSettingsFrame(tk.Frame):
    """Class to create and manage the connection settings frame."""

    def __init__(self, master: tk.Tk) -> None:
        """Initialize the connection settings frame."""
        super().__init__(master)
        self.server_running = False

        for i in range(8):
            self.columnconfigure(i, weight=1)

        tk.Label(self, text="Connection Settings").grid(row=0, column=0, sticky="w")

        tk.Label(self, text="Host").grid(row=0, column=1, sticky="ew")
        self.host_entry = tk.Entry(self, state=tk.DISABLED)
        self.host_entry.grid(row=0, column=2, sticky="ew")

        tk.Label(self, text="Port").grid(row=0, column=4, sticky="ew")
        self.port_entry = tk.Entry(self, state=tk.DISABLED)
        self.port_entry.grid(row=0, column=5, sticky="ew")

        self.start_button = tk.Button(
            self, text="Start Server", command=self.start_server, state=tk.DISABLED
        )
        self.start_button.grid(row=0, column=7, pady=5)

    def start_server(self):
        """Handle the start server button click event."""
        host = self.host_entry.get()
        port = self.port_entry.get()
        print(f"Start server on {host}:{port}")
        # Disable the start button so it can only be pressed once
        if not self.server_running:
            self.server_running = True
            self.start_button.config(state=tk.DISABLED)


class SendMessageFrame(tk.Frame):
    """Class to create and manage the send message frame."""

    def __init__(self, master: tk.Tk) -> None:
        """Initialize the send message frame."""
        super().__init__(master)

        tk.Label(self, text="Send Message").pack(anchor="w")

        self.entry = tk.Text(self, height=5)
        self.entry.pack(pady=5)

        self.send_button = tk.Button(
            self, text="Send", command=self.send, state=tk.DISABLED
        )
        self.send_button.pack(anchor="e")

    def send(self):
        print("Send:", self.entry.get())


class ReceivedMessagesFrame(tk.Frame):
    """Class to create and manage the received messages frame."""

    def __init__(self, master: tk.Tk) -> None:
        """Initialize the received messages frame."""
        super().__init__(master)

        tk.Label(self, text="Received Messages").pack(anchor="w")

        self.text = tk.Text(self, state=tk.DISABLED)
        self.text.pack(fill=tk.BOTH, expand=True, pady=5)

    def add_message(self, message):
        self.text.insert(tk.END, message + "\n")
