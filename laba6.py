import threading

def thread_safe(func):
    lock = threading.Lock()

    def wrapper(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)
    return wrapper

counter = [0]

@thread_safe
def increment():
    counter[0] += 1
    return counter[0]


def worker(n):
    for _ in range(n):
        increment()

if __name__ == "__main__":
    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker, args=(1000,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Кінцеве значення лічильника:", counter[0])
