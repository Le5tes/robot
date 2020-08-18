import asyncio
from camera_connection.camera_connection import startCamera

def getControlConnection(controller): 
    async def controlConnection(websocket, path):
        startCamera(websocket)
        escape = False
        while not escape:
            command = await websocket.recv()
            if command == "END":
                escape = True
            else:
                print("command")
                websocket.send(controller.giveCommand(command))
    return controlConnection

