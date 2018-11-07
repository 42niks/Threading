import threading as th

class ThreadPool(object):
	"""ThreadPool is like Pool from multiprocessing for true threads"""

	# the maximum number of threads that are allowed to be alive at a time
	noOfThreads = 0
	# list of threads alive
	aliveThreads = []

	def __init__(self, noOfThreads):
		self.noOfThreads = noOfThreads
		self.aliveThreads = [None for i in range(noOfThreads)]

	def map(self, target, list_of_arg_tuples):
		if self.noOfThreads == 0:
			print("noOfThreads is zero, continuing after making it 1.")
			self.noOfThreads = 0

		if len(list_of_arg_tuples) == 0:
			return

		idx = 0

		while len(aliveThreads)!=0 or idx!=(len(list_of_arg_tuples)-1):
			i = 0
			for i, thread in enumerate(aliveThreads):
				if not thread.isAlive():
					aliveThreads.pop(i)

			while len(aliveThreads)<noOfThreads and
				idx!=(len(list_of_arg_tuples)-1):
				aliveThreads.append(th.Thread(target=target,
					args=list_of_arg_tuples[idx]))
				idx+=1
				aliveThreads[-1].start()
			
			
