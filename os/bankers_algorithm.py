import numpy as np
from time import sleep


class Bankers_Algorithm(object):

    def __init__(self, resources, number_of_processes):
        self.resources = resources
        self.n = number_of_processes
        self.matrix = list()
        self.max_matrix = list()
        self.current = list()
        self.Remaining = list()
        self.sequence = list()

        Bankers_Algorithm.allocation(self)
        Bankers_Algorithm.maximum_need(self)
        Bankers_Algorithm.current_availability(self)
        Bankers_Algorithm.show(self)
        Bankers_Algorithm.algorithm(self)

    def __random(self, k=1):
    	if k == 0:
    		return np.random.randint(np.min(self.resources))
    	return np.random.randint(np.min(self.resources), np.max(self.resources))

    def allocation(self):
        self.matrix = np.zeros((self.n, 4), dtype=int)
        for i in range(n):
            for j in range(4):
                if j == 0:
                	self.matrix[i][j] = i+1
                else:
                    self.matrix[i][j] = self.__random(0)

    def algorithm(self):
    	self.Remaining = np.subtract(self.max_matrix, self.matrix)
    	self.Remaining = np.array([[7,4,3],[1,2,2], [6,0,0], [0,1,1], [4,3,1]])
    	self.matrix = np.array([[0,1,0], [2, 0, 0], [3,0,2], [2, 1, 1], [0, 0, 2]])

    	while True:
    		max_tries = len(self.Remaining)
    		for i in range(len(self.Remaining)):
    			# if (0 > np.subtract(self.current, self.Remaining[i])).any():
    			# 	print(self.Remaining[i])
    			# 	print("done")
    			# 	continue

    			if self.Remaining[i][1] <= self.current[0] and self.Remaining[i][2] <= self.current[1] and self.Remaining[i][3] <= self.current[2]:
    			# elif np.sum(self.Remaining[i][1:]) <= np.sum(self.current):
    				sleep(1)
    				print("="*30)
    				print("----------Remaining--------")
    				print("="*30)
    				print(self.Remaining)
    				self.sequence.append(self.matrix[i][0])
    				self.update_cv(i)
    				print("="*30)
    				print("---------Current-----------")
    				print("="*30)
    				print(self.current)
    				self.matrix = np.delete(self.matrix, obj=i, axis=0)
    				self.Remaining = np.delete(self.Remaining, obj=i, axis=0)
    				break


    		
    		if len(self.Remaining) != 0 and len(self.Remaining) == max_tries:
	    		print("="*30)
	    		print("The Algorithm is unSafe")
	    		print("="*30)
	    		self.Remaining = list()
	    		break
	    	elif np.sum(self.matrix) == 0 and np.sum(self.Remaining) == 0:
	    		print("\n\n")
	    		print("="*30)
	    		print("The Algorithm is Safe")
	    		print("="*30)
	    		break

    def update_cv(self, m):
    	self.current = np.array(self.current, dtype=int)
    	self.current = np.add(self.current, self.matrix[m][1:])


    def current_availability(self):
    	# total = np.sum(self.matrix, axis=0)
    	# total = total[1:]
    	# for i in range(len(self.resources)):
    	# 	z = abs(self.resources[i] - total[i])
    	# 	self.current.append(z) 
    	self.current = np.array([3,3,2])



    def maximum_need(self):
    	self.max_matrix = np.zeros((self.n, 4), dtype=int)
    	for i in range(n):
    		for j in range(4):
    			if j == 0:
    				self.max_matrix[i][j] = i+1
    			else:
    				self.max_matrix[i][j] = self.__random()

    def show(self):
    	print("="*30)
    	print("allocated resources: ")
    	alloc = np.delete(self.matrix, obj=0, axis=1)
    	print(alloc)
    	print("maximum resources needed:")
    	max_alloc = np.delete(self.max_matrix, obj=0, axis=1)
    	print(max_alloc)
    	print("Current Availability:")
    	print(self.current)
    	print("Remaining Need:")
    	remaining_need = np.delete(np.subtract(self.max_matrix, self.matrix), obj=0, axis=1)
    	print(remaining_need)
    	print("="*30)


if __name__ == '__main__':
	resources = list()
	for i in range(3):
		r = int(input(f"Please enter the resource of R{i+1}: "))
		resources.append(r)

	n = int(input("Please enter the number of processes: "))
	banker = Bankers_Algorithm(resources, n)
	# banker.show()

	for i in banker.sequence:
		print(f"P{i}", end="->")
	print("\n")
