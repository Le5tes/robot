import asyncio
import concurrent.futures

def getOutput(converter):
    print("in get output")
    return converter.stdout.read1(32768)

async def broadcastOut(converter, websocket):
    print("in broadcastOut")
    loop = asyncio.get_running_loop()
    
    try:
        while True:
            with concurrent.futures.ThreadPoolExecutor() as pool:
                print("await output in broadcastOut")
                buf = await loop.run_in_executor(pool, getOutput, converter)
                if buf:
                    print("got output, sending")
                    websocket.send(buf)
                elif converter.poll() is not None:
                    break
    finally:
        converter.stdout.close()