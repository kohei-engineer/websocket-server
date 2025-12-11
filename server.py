import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.websockets import WebSocketDisconnect
import uvicorn

app = FastAPI()

connected_clients = set()
message_queue = asyncio.Queue()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    print("Client connected")

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received from client: {data}")
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print("Client disconnected")

async def broadcaster():
    """Queue に入ったメッセージを全クライアントへ送信"""
    while True:
        message = await message_queue.get()
        dead = []
        for ws in connected_clients:
            try:
                await ws.send_text(message)
            except:
                dead.append(ws)
        for ws in dead:
            connected_clients.remove(ws)

async def console_input():
    """コンソールから入力すると全クライアントへ送信"""
    loop = asyncio.get_event_loop()
    while True:
        msg = await loop.run_in_executor(None, input, ">>> ")
        await message_queue.put(msg)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(broadcaster())
    asyncio.create_task(console_input())

if __name__ == "__main__":
    uvicorn.run("server:app", reload=False)
