import threading
import random
import time

class Reader_writer(object):
	def __init__(self):
		self.data = 0
		self.readers = 0
		self.writers = 0
		self.mutex1 = threading.Lock()
		self.mutex2 = threading.Lock()
		self.reading = threading.Lock()
		self.write_blocking = threading.Lock()
		self.read_blocking = threading.Lock()


	def reader(self):

		print("Reader is acquiring lock..")
		time.sleep(1)
		self.reading.acquire()
		self.read_blocking.acquire()
		self.mutex1.acquire()
		self.readers = self.readers + 1
		if self.readers == 1: self.write_blocking.acquire()
		self.mutex1.release()
		self.read_blocking.release()
		self.reading.release()
		self.mutex1.acquire()
		self.readers = self.readers - 1
		print("The reader has now read the data..")
		print(f"The data is {self.data}")
		time.sleep(1)
		if self.readers == 0: self.write_blocking.release()
		self.mutex1.release()
		print("The reader is now releasing the lock..")

	def writer(self):
		"Writer of readers and writers algorithm"
		print("The writer is now acquiring the lock..")
		time.sleep(1)
		self.mutex2.acquire()
		self.writers = self.writers + 1
		if self.writers == 1: self.read_blocking.acquire()
		self.mutex2.release()
		self.write_blocking.acquire()
		self.write_blocking.release()
		self.mutex2.acquire()
		print("The writer has now written the data...")
		self.data += 1
		print(f"The data now is {self.data}")
		time.sleep(1)
		self.writers = self.writers - 1
		if self.writers == 0: self.read_blocking.release()
		self.mutex2.release()




if __name__ == '__main__':
    for i in range(10):
        n = random.randint(0, 100)
        if(n >= 65):
            Thread1 = threading.Thread(target = Reader_writer().reader())
            Thread1.start()
        else:
            Thread2 = threading.Thread(target = Reader_writer().writer())
            Thread2.start()

Thread1.join()
Thread2.join()