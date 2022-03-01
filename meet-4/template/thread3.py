import threading


def worker(num):
    print("worker: " + str(num))


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
