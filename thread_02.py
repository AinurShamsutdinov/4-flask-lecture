import threading
import time


def worker(num):
    print(f'Beginning of thread {num}')
    time.sleep(3)
    print(f'End of thread {num}')


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)

for t in threads:
    t.start()
    t.join()

print('All threads finished')
