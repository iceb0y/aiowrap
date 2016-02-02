# aiowrap

## Simple example

Assume that you have some existing libraries with blocking methods.

```python
def foo_sync(x, a, b):
    """Some existing library methods. Sleeps for x seconds and returns a + b."""
    time.sleep(x)
    return a + b
```

And you are writing a program in Python3's `asyncio` framework. To use the
blocking library, one way is to use a thread pool. This library provides
another option:

```python
# Wraps foo_sync() into foo_async() to use in asyncio framework.
time.sleep = aiowrap.wrap_async(asyncio.sleep)
foo_async = aiowrap.wrap_sync(foo_sync)
```

Now you have an asynchronous, non-blocking version of the method, you can call
it inside your favourite coroutine:

```python
async def main():
    print(await foo_async(1, 2, 3))
```

The source code of this example can be found at `example/sleep.py`.
