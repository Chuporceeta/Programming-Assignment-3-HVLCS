import os
from time import time
from matplotlib import pyplot as plt

times = []
sizes = []
for i in range(1, 11):
    with open(f'../tests/test{i}.in') as f:
        file = f.readlines()
        K = int(file[0])
        A = file[K+1]
        B = file[K+2]
        sizes.append(len(A)*len(B))

    sum_time = 0
    for _ in range(10):
        st = time()
        os.system(f'py ./main.py --input ../tests/test{i}.in --output temp')
        sum_time += time() - st
    print(i)
    times.append(sum_time/10)
os.remove('./temp')

sizes, times = zip(*sorted(zip(sizes, times)))

plt.plot(sizes, times)
plt.title("HVLCS Running Time vs Input Size")
plt.xlabel("Input Size (len(A) * len(B))")
plt.ylabel("Running Time (avg over 10 runs) (sec)")
plt.savefig("../q1.png")