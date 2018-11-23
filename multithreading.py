import threading as th
from timeit import default_timer as timer
import time

class ThreadPool(object):
	"""ThreadPool is like Pool from multiprocessing for true threads"""

	# the maximum number of threads that are allowed to be alive at a time
	noOfThreads = 0
	# list of threads alive
	aliveThreads = []

	def __init__(self, noOfThreads):
		self.noOfThreads = noOfThreads
		self.aliveThreads = []

	def map(self, target, list_of_args):
		if self.noOfThreads == 0:
			print("noOfThreads is zero, continuing after making it 1.")
			self.noOfThreads = 1

		if len(list_of_args) == 0:
			return
		list_of_arg_tuples = list(list_of_args)
		while self.aliveThreads or list_of_arg_tuples:
			for i, thread in enumerate(self.aliveThreads):
				if not thread.isAlive():
					# cleanup
					self.aliveThreads[i].join()

					# delete thread
					self.aliveThreads.pop(i)

			while len(self.aliveThreads)<self.noOfThreads and \
				list_of_arg_tuples:
				self.aliveThreads.append(th.Thread(target=target,
					args=list_of_arg_tuples[0]))
				list_of_arg_tuples.pop(0)
				self.aliveThreads[-1].start()

			# yield the thread
			time.sleep(0)
