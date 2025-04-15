import websockets, asyncio

async def main():
    url = "ws://localhost:8000/websocket/tasks"

    async with websockets.connect(url) as websocket:
        print("Подключено к вебсокету.")

        await websocket.send("Привет, сервер!")

        while True:
            response = await websocket.recv()
            print(response)

asyncio.run(main())