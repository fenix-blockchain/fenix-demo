import asyncio
import logging
import os

from fenix_pipeline import ConnectionClosed
from fenix_pipeline import RawDataSocket
from fenix_pipeline import SubscriptionTypes
from fenix_pipeline import Trade


log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


async def simple_sample(event_loop):
    # read the API key from a local environment variable called `FENIX_API_KEY`
    socket = RawDataSocket(os.environ.get('FENIX_API_KEY'))
    # using a context manager
    async with await socket.connect(message_handler=print_messages) as subscriber:
        # subscribe to the `btc-usdt` stream
        await subscriber.subscribe(
            SubscriptionTypes.TRADES_BY_MARKET, 'btc-usdt')
        # just receive messages for the next 10 seconds
        await subscriber.monitor(10)
        # unsubscribe from the `btc-usdt` stream
        await subscriber.unsubscribe(
            SubscriptionTypes.TRADES_BY_MARKET, 'btc-usdt')
    # done


async def print_messages(item):
    if isinstance(item, Trade):
        log.info('received: %r', item)
    else:
        log.info('other message: %s', item)


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(simple_sample(event_loop))
