import asyncio
import ssl
import websockets

from robot_connection.websocket_connection import getControlConnection
from robot_control.robot_control import RobotController

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
controller = RobotController()

start_server = websockets.serve(
    getControlConnection(controller), "0.0.0.0", 8765
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()