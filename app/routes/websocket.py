from fastapi import APIRouter, WebSocket
from typing import List
from pydantic import BaseModel

router = APIRouter()

# Store connected WebSocket clients
active_connections: List[WebSocket] = []

class OrderStatusUpdate(BaseModel):
    id: int
    symbol: str
    price: float
    quantity: int
    order_type: str

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Accept the WebSocket connection
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Handle incoming messages if needed
            for connection in active_connections:
                if connection != websocket:
                    await connection.send_text(f"New message: {data}")
    except Exception as e:
        active_connections.remove(websocket)
        await websocket.close()
