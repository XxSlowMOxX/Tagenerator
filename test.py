import wikipedia
import time


wikipedia.set_rate_limiting(True, min_wait=1)
print(wikipedia.random())
