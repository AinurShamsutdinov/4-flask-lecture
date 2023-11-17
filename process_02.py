import multiprocessing
import time


def worker(num):
    print(f'Started process {num}')
    time.sleep(3)
    print(f'Finished process {num}')


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)

    for p in processes:
        p.start()
        p.join()

    print('Finished all processes')
