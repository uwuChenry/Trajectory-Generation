import matplotlib.pyplot as plt


f = open("Output.txt", "r")

i = 0

velocity = []
time = []

while True:
    line = f.readline()
    if not line:
        break

    velocity.append(float(line))
    time.append(i)
    i += 0.01
f.close()

plt.axis([0, 10, 0, 10])
plt.xlabel('time (s)')
plt.ylabel('velocity (ft/s)')
plt.plot(time, velocity)
plt.show()
#print('HI')
#print("你好")
