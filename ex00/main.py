from queue import Queue
from random import randint
import re


queue = Queue()

def generate_request():

    request: int = randint(1, 100)

    print("Generated:\t", request)

    queue.put(request)


def process_request():
    if queue.empty():
        print("Queue is empty")
        return

    request: int = queue.get()

    print("Processing:\t", request)


def main():

    while True:

        try:
            user_input: int = int(input("Please input amount of requests: "))
        except KeyboardInterrupt:
            return
        except ValueError:
            print("Amount must be a number")
            continue

        print()
        for _ in range(user_input):
            generate_request()
        print()
        for _ in range(user_input):
            process_request()


if __name__ == "__main__":
    main()
