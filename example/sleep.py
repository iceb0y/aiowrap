import aiowrap
import asyncio
import time

def foo_sync(x, a, b):
    """Some existing library methods. Sleeps for x seconds and returns a + b."""
    time.sleep(x)
    return a + b

# Wraps foo_sync() into foo_async() to use in asyncio framework.
time.sleep = aiowrap.wrap_async(asyncio.sleep)
foo_async = aiowrap.wrap_sync(foo_sync)

async def main():
    print(await foo_async(1, 2, 3))

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
