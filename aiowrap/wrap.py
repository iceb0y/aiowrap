import asyncio
import functools
import greenlet

def wrap_async(func):
    """Wraps an asynchronous function into a synchronous function."""
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        fut = asyncio.ensure_future(func(*args, **kwargs))
        cur = greenlet.getcurrent()
        def callback(fut):
            try:
                cur.switch(fut.result())
            except Exception as e:
                cur.throw(e)
        fut.add_done_callback(callback)
        return cur.parent.switch()
    return wrapped

def wrap_sync(func):
    """Wraps a synchronous function into an asynchronous function."""
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        fut = asyncio.Future()
        def green():
            try:
                fut.set_result(func(*args, **kwargs))
            except Exception as e:
                fut.set_exception(e)
        greenlet.greenlet(green).switch()
        return fut
    return wrapped
