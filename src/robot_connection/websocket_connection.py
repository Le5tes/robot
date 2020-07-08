import asyncio

def getControlConnection(controller): 
    async def controlConnection(websocket, path):
        escape = False
        while not escape:
            command = await websocket.recv()
            if command == "END":
                escape = True
            else:
                websocket.send(controller.giveCommand(command))
    return controlConnection

