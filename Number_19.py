def cached(func):
    int_arr = {}

    def memoize(n):
        if n in int_arr.keys():
            return int_arr[n]
        int_arr[n] = func(n)
        return int_arr[n]

    return memoize


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(int(input())))