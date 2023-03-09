from numba import njit
import time

@njit
def main():
    veces = 200000000
    num = 1
    a = 0
    for a in range(veces):
        num = num + num - num
    print(num)

start = time.time()
main()
end = time.time()
print(end - start)
