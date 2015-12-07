#!/usr/bin/env python
import time

class myCache(object):
	def __init__(self):
		self.cache = {}
		self.time = {}
	def set(self,key,value):
		timestamp = time.time()
		self.cache[key] = value
		self.time[key] = timestamp
	def get(self,key):
		if self.cache.get(key):
			starttime = self.time[key]
			nowtime = time.time() - starttime
			if nowtime > 5:
				self.delete(key)
				return False
			else:
				self.time[key] = time.time()
				return self.cache.get(key)
		else:
			return False
	def delete(self,key):
		if self.cache.get(key):
			self.cache.pop(key)
			self.time.pop(key)
			return True
		else:
			return False
	def clear(self):
		self.cache.clear()
		self.time.clear()
		return True
