import asyncio as aio

async def main():
    print('...Hello')
    await aio.sleep(2)
    print('World...!')

aio.run(main())