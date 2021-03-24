import asyncio
from camera_connection.camera_broadcaster import broadcastOut
from camera_connection.camera_connection import startCamera

cameraRunning = False
output = None

def getControlConnection(controller): 
    async def controlConnection(websocket, path):
        print("in controlConnection, strting camera")
        print("in controlConnection, camera started")
        if websocket.subprotocol == "control":
            escape = False
            while not escape:
                command = await websocket.recv()
                if command == "END":
                    escape = True
                else:
                    print("command")
                    websocket.send(controller.giveCommand(command))
        elif websocket.subprotocol == "video_feed":
            if not cameraRunning:
                output = startCamera()
            asyncio.create_task(broadcastOut(output.converter, websocket))
    return controlConnection

