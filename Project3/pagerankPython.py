import numpy as np
M=np.array([[0,1/2,1,0],
  [1/3,0,0,1/2],
  [1/3,0,0,1/2],
  [1/3,1/2,0,0]])

v=[0.25,0.25,0.25,0.25]

count = 0
for i in range(100):
    count += 1
    print(count)
    v = M @ v
    print(v)
    if sum(abs(v-M@v))<0.000000001:
        break
