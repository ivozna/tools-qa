import time

from linearsearch import linear_search
from linearsearch import binary_search
from linearsearch import while_binary_search


def exec_time(func, parameters):
    start = time.perf_counter()
    func(*parameters)
    elapsed = time.perf_counter() - start
    print(f"{func.__name__} is run in {elapsed:.10f}")


exec_time(linear_search, [range(1, 100000000), 670000000000])
exec_time(binary_search, [range(1, 100000000), 670000000000, 0, 99999999])
exec_time(while_binary_search, [range(1, 100000000), 670000000000])

