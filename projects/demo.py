import time

def timeit(func):
    """
    Decorator for measuring function's running time.
    """
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.2f seconds."
              % (func.__qualname__, time.time() - start_time))
        return result

    return measure_time

@timeit
def func():
    while True:
        demo = input("anything: ")
        print(f"So you have {demo} dogs.")
        if demo=='q':
            print(f"Thanks for your using, hope to see you next time, bye~")
            break

if __name__ == "__main__":
    func()