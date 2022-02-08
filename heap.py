from math import inf

class Heap(object):
	def __init__(self):
		self.arr = []

	def getLeftChildIdx(self, idx):
		if idx < 0 or idx >= len(self.arr):
			return -1
		return 2*idx+1

	def getRightChildIdx(self, idx):
		if idx < 0 or idx >= len(self.arr):
			return -1
		return 2*idx+2

	def getParentIdx(self, idx):
		if idx < 0 or idx >= len(self.arr):
			return -1
		return (idx-1)//2

	def getParent(self, idx):
		if idx < 0 or idx >= len(self.arr):
			return -1
		return self.arr[self.getParentIdx(idx)]

	def getLeftChild(self, idx):
		if idx < 0 or idx >= len(self.arr):
			return inf
		cidx = self.getLeftChildIdx(idx)
		if cidx == -1 or cidx >= len(self.arr):
			return inf
		return self.arr[cidx]

	def getRightChild(self, idx):
		if idx < 0 or idx >= len(self.arr):
			return inf
		cidx = self.getRightChildIdx(idx)
		if cidx == -1 or cidx >= len(self.arr):
			return inf
		return self.arr[self.getRightChildIdx(idx)]

	def heapifyUp(self):
		idx = len(self.arr)-1
		while 1:
			if idx <= 0:
				break
			itm = self.arr[idx]
			if itm >= self.getParent(idx):
				break
			parent_idx = self.getParentIdx(idx)
			self.arr[parent_idx],self.arr[idx] = self.arr[idx],self.arr[parent_idx]
			idx = parent_idx

	def heapifyDown(self):
		idx = 0
		while 1:
			if self.getLeftChild(idx) == inf:
				break

			itm = self.arr[idx]
			lc = self.getLeftChild(idx)
			rc = self.getRightChild(idx)

			if itm <= lc and itm <= rc:
				break

			nidx = None
			if lc < rc:
				nidx = self.getLeftChildIdx(idx)
			else:
				nidx = self.getRightChildIdx(idx)

			if nidx == -1:
				break

			self.arr[nidx],self.arr[idx] = self.arr[idx],self.arr[nidx]
			idx = nidx

	def add(self, itm):
		self.arr.append(itm)
		self.heapifyUp()

	def peek(self):
		if len(self.arr) == 0:
			return None
		return self.arr[0]

	def poll(self):
		if len(self.arr) == 0:
			return None
		itm = self.peek()
		last_idx = len(self.arr)-1
		self.arr[last_idx],self.arr[0] = self.arr[0],self.arr[last_idx]
		self.arr.pop()
		self.heapifyDown()
		return itm

h=Heap()

h.add(5)
h.add(4)
h.add(2)
h.add(1)
h.add(7)
h.add(6)

print(h.arr)

h.poll()

print(h.arr)
