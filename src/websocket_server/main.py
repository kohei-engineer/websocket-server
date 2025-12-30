import asyncio
import websockets

# Connected WebSocket clients
clients = set()

async def handler(ws: websockets.WebSocketServerProtocol):
    """Handle a single WebSocket client connection.

    Args:
        ws (websockets.WebSocketServerProtocol): Connected WebSocket client.
    """
    clients.add(ws)
    print("Client connected")
    try:
        async for msg in ws:
            print("Received:", msg)
    except websockets.ConnectionClosed:
        print("Client disconnected")
    finally:
        clients.remove(ws)

async def ws_server(host: str = "0.0.0.0", port: int = 8000):
    """Start the WebSocket server on the specified host and port.

    Args:
        host (str, optional): IP address to bind the server. Defaults to "0.0.0.0".
        port (int, optional): Port number to bind the server. Defaults to 8000.
    """
    async with websockets.serve(handler, host, port):
        print(f"WebSocket server started on {host}:{port}")
        await asyncio.Future()

def main():
    """main function to start WebSocket server"""
    asyncio.run(ws_server())
    print('WebSocket server stopped')

if __name__ == "__main__":
    main()
