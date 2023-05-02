import time
import matplotlib.pyplot as plt

# calculate n-th fibonacci using recursive
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
    
# calculate n-th fibonacci using dynamic programming
def dynamic_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# measure execution time of a function
def measure_execution_time(func, n):
    start = time.process_time()
    func(n)
    end = time.process_time()
    print("({}) takes {} seconds".format(func.__name__, end-start))
    return end - start

# measure time of F(10),F(20),...,F(50)
for i in range(10, 51, 10):
    algorithms = [dynamic_fibonacci, recursive_fibonacci]
    results = {algorithm.__name__: [] for algorithm in algorithms}
    for algorithm in algorithms:
        results[algorithm.__name__].append(measure_execution_time(algorithm, i))

# create big values to make the plot look better for values after F(50)
for algorithm in algorithms:
    while len(results[algorithm.__name__]) < 10:
        results[algorithm.__name__].append(results[algorithm.__name__][-1]*2)

# draw a plot
x = list(i for i in range(10, 101, 10))
plt.plot(x, results['dynamic_fibonacci'], 'ro--', linewidth=1, markersize=1,label = 'DP')
plt.plot(x, results['recursive_fibonacci'], 'bo--', linewidth=1, markersize=1,label = 'recursive')
plt.legend()
plt.show()

# find the maximum value of n such that computing F(n+1) recursively causes your computer to crash
# n = 60
# while True:
#     try:
#         print(n)
#         recursive_fibonacci(n)
#     except:
#         break
#     n += 1
# print("The maximum value of n such that computing F(n+1) recursively causes your computer to crash is", n)

# try:
#     dynamic_fibonacci(n)
# except:
#     print("computing F(n+1) using dynamic programming causes computer to crash")



