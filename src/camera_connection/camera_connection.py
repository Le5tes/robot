from camera_connection.camera_converter_output import CameraConverterOutput
from time import sleep
import picamera
import asyncio

WIDTH = 640
HEIGHT = 480
FRAMERATE = 24
VFLIP = False
HFLIP = False

async def broadcastOut(converter, websocket):
    try:
        while True:
            buf = await converter.stdout.read1(32768)
            if buf:
                await websocket.send(buf)
            elif converter.poll() is not None:
                break
    finally:
        converter.stdout.close()

def startCamera(websocket):
    with picamera.PiCamera() as camera:
        camera.resolution = (WIDTH, HEIGHT)
        camera.framerate = FRAMERATE
        camera.vflip = VFLIP # flips image rightside up, as needed
        camera.hflip = HFLIP # flips image left-right, as needed
        sleep(1) # camera warm-up time
        output = CameraConverterOutput(camera)
        asyncio.create_task(broadcastOut(output.converter, websocket))
        camera.start_recording(output, 'yuv')
