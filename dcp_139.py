'''
	This problem was asked by Google.

	Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also implements peek(). peek shows the next element that would be returned on next().

	Here is the interface:

	class PeekableInterface(object):
		def __init__(self, iterator):
			pass

		def peek(self):
			pass

		def next(self):
			pass

		def has_next(self):
			pass
'''

class PeekableInterface(object):
		def __init__(self, iterator):
			self.iterator = iterator
			self.next_val = next(iterator)
			self.has_next_val = True

		def peek(self):
			return self.next_val

		def next(self):
			next_val = self.next_val
			# update next value variables for the next iteration
			try:
				self.next_val = next(iterator)
			except StopIteration:
				self.has_next_val = False
				self.next_val = None
			
			return next_val
			
			return next_val

		def has_next(self):
			return self.has_next_val
			
			
			
# Tests

sample_list = [1, 2, 3, 4, 5]
iterator = iter(sample_list)
peekable = PeekableInterface(iterator)

assert peekable.peek() == 1
assert peekable.has_next()

assert peekable.next() == 1
assert peekable.next() == 2
assert peekable.next() == 3

assert peekable.peek() == 4
assert peekable.has_next()

assert peekable.next() == 4
assert peekable.has_next()
assert peekable.peek() == 5
assert peekable.next() == 5

assert not peekable.has_next()
assert not peekable.peek()