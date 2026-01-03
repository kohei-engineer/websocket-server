import asyncio
import threading
import websockets

class WebSocketServer:
    """WebSocketServer class to handle WebSocket connections.

    Args:
        host (str, optional): IP address to bind the server. Defaults to "0.0.0.0".
        port (int, optional): Port number to bind the server. Defaults to 8000.
    """

    def __init__(self, host: str = "0.0.0.0", port: int = 8000) -> None:
        self.host = host
        self.port = port
        self._clients = set()
        self._running = False

    @property
    def running(self) -> bool:
        """Return whether the server has been started."""
        return self._running

    async def handler(self, ws: websockets.WebSocketServerProtocol) -> None:
        """Handle a single WebSocket client connection.

        Args:
            ws (websockets.WebSocketServerProtocol): Connected WebSocket client.
        """
        self._clients.add(ws)
        print("Client connected")
        try:
            async for msg in ws:
                print("Received:", msg)
        except websockets.ConnectionClosed:
            print("Client disconnected")
        finally:
            self._clients.remove(ws)

    async def run_server(self) -> None:
        """Start the WebSocket server on the specified host and port."""
        async with websockets.serve(self.handler, self.host, self.port):
            print(f"WebSocket server started on {self.host}:{self.port}")
            self._running = True
            await asyncio.Future()

    def start(self) -> None:
        """Start the WebSocket server in a daemon thread."""
        if self._running:
            return
        threading.Thread(target=lambda: asyncio.run(self.run_server()), daemon=True).start()
