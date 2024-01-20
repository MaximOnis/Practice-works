import tracemalloc


# Декоратор
def memory_usage(func):
    def wrap():
        tracemalloc.start()
        func()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Memory used by \"{func.__name__}\": {peak / (1024 ** 2):.4f} MB")
    return wrap

# Приклади функцій
@memory_usage
def example_function():
    data = [i for i in range(100000)]
    dat = [i for i in range(10000)]
    f = 1065**4+787**45+8989**675
    print("ex")
    return data

@memory_usage
def example_function1():
    data = [i for i in range(100000)]
    dat = [i for i in range(10000)]
    print("ex1")


@memory_usage
def example_function2():
    data = [i for i in range(500000)]
    print("ex2")
    return data


# Виклик
example_function()
example_function1()
example_function2()
