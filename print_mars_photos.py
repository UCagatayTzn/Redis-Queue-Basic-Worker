from redis import Redis
from rq import Queue

from mars import get_mars_photo

q = Queue(connection=Redis())

for i in range(10):
    q.enqueue(get_mars_photo, 990 + i)
    print("*** OK ***")