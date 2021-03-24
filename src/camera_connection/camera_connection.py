from camera_connection.camera_converter_output import CameraConverterOutput
from time import sleep
import picamera

WIDTH = 640
HEIGHT = 480
FRAMERATE = 24
VFLIP = False
HFLIP = False


def startCamera():
    with picamera.PiCamera() as camera:
        camera.resolution = (WIDTH, HEIGHT)
        camera.framerate = FRAMERATE
        camera.vflip = VFLIP # flips image rightside up, as needed
        camera.hflip = HFLIP # flips image left-right, as needed
        sleep(1) # camera warm-up time
        output = CameraConverterOutput(camera)
        print("starting recording")
        camera.start_recording(output, 'yuv')
        return output
