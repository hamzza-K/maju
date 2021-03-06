import threading
import random
import time
import os


class Readers_Writer_Problem(object):


	def reader(self):
		print(f"{self.n}:Reader is acquiring lock..")
		time.sleep(1)
		self.reading.acquire()
		self.read_blocking.acquire()
		self.m1.acquire()
		self.readers = self.readers + 1
		if self.readers == 1: self.write_blocking.acquire()
		self.m1.release()
		self.read_blocking.release()
		self.reading.release()
		self.m1.acquire()
		prob = self.probability()
		if prob != 0:
			print(f"{self.n}:The reader did not read the data.")
		else: 
			print(f"{self.n}:The reader has now read the data..")
			time.sleep(1)
		self.readers = self.readers - 1
		if self.readers == 0: self.write_blocking.release()
		self.m1.release()
		print(f"{self.n}:The reader is now releasing the lock..")
	
	def __init__(self, n):
		self.n = n
		self.readers = 0
		self.writers = 0
		self.m1 = threading.Lock()
		self.m2 = threading.Lock()
		self.reading = threading.Lock()
		self.write_blocking = threading.Lock()
		self.read_blocking = threading.Lock()

	def writer(self):
		print(f"{self.n}:The writer is now acquiring the lock..")
		time.sleep(1)
		self.m2.acquire()
		self.writers = self.writers + 1
		if self.writers == 1: self.read_blocking.acquire()
		self.m2.release()
		self.write_blocking.acquire()
		self.write_blocking.release()
		self.m2.acquire()
		prob = self.probability()
		if prob == 0:
			print(f"{self.n}:The writer did not write the data.")
		else:
			print(f"{self.n}:The writer has now written the data...")
			time.sleep(1)
		self.writers = self.writers - 1
		if self.writers == 0: self.read_blocking.release()
		self.m2.release()

	def probability(self):
		x = random.randint(10, 100)
		x %= 2
		return x



if __name__ == '__main__':
    for i in range(10):
        x = random.randint(10000, 9999999)
        if(x % 2 == 0):
            Thread1 = threading.Thread(target=Readers_Writer_Problem(x).reader())
        
            Thread1.start()
        else:
            Thread2 = threading.Thread(target = Readers_Writer_Problem(x).writer())
        
            Thread2.start()

Thread1.join()
Thread2.join()
