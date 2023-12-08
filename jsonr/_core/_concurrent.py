import threading
import multiprocessing
import multiprocessing.shared_memory
import concurrent
import concurrent.futures
import subprocess
import sched
import queue
import contextvars
import _thread

class Concurrency:
    def __init__(self):
        self.threading: object = threading
        self.multiprocessing: object = multiprocessing
        self.multiprocessing_shared_memory: object = multiprocessing.shared_memory
        self.concurrent: object = concurrent
        self.concurrent_futures: object = concurrent.futures
        self.subprocess: object = subprocess
        self.sched: object = sched
        self.queue: object = queue
        self.contextvars: object = contextvars
        self._thread: object = _thread
