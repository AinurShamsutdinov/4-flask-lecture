import random
import time


def long_running_task():
    for i in range(5):
        print(f'Execution of task {i}')
        time.sleep(random.randint(1, 3))


def main():
    print('Beginning of application')
    long_running_task()
    print('End of application')


if __name__ == '__main__':
    main()
