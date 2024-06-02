'''Caesar brute force lib'''

from threading import Thread
from queue import Queue

class Crypt:

    thread = None
    orders = Queue()
    results = Queue()

    def processor(self, orders, results):
        while True:
            order = orders.get()
            r = []
            
            if order[0] == 1:
                n = order[1]
                c = order[2]

                for i in range(n):
                    m = []
                    for letter in c:
                        m.append(chr((ord(letter) - i - 160) % n))
                    m = ''.join(m)
                    r.append((m, i))

            elif order[0] == 0:
                break

            results.put(r)

    def brute(self, msg, n):
        self.orders.put([1, n, msg])

        return self.results.get()

    def __init__(self):
        self.thread = Thread(target=self.processor, args=(self.orders, self.results))
        self.thread.start()

    def __del__(self):
        self.orders.put([0, 0, 0])

        self.thread.join()