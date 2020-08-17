from time import time, sleep

start_time = time()

sleep(2)

int_time = int(time() - start_time)

if int(time() - start_time) > 1:
	print('yes')

print(time())
print(start_time)
print(int_time)
