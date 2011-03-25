#!/bin/python

import cloudfiles
import mimetypes
import glob

"""
cloud_user = MY_CLOUD_USER
cloud_key = MY_CLOUD_KEY
cloud_container = 'FILES'
"""

class Connector(object):
	def __init__(self, user, api_key, cloud_container):
		self.user = user
		self.api_key = key
		self.cloud_container = cloud_container
		self.conn = cloudfiles.get_connection(self.user, self.api_key)
		self.container = self.conn.get_container(cloud_container)

	def getContentType(self, source):
		return mimetypes.guess_type(source)

	def push(self, source, target='AUTO', content_type='AUTO'):
		if target.lower()=='auto':
			target = source
		if content_type.lower() == 'auto':
			content_type = self.getContentType(source)
	
		# open a file and write the descriptor
		fd = open(source,'rb')
		ob = self.container.create_object(target) # you can use fd.name to pull it from the file descriptor
		ob.content_type = content_type
		# you can use the save(fd) method if the source is changing and you want to provide a stream
		ob.write(fd)
		fd.close()


if __name__=='__main__':
	import sys
	user = sys.argv[1]
	key = sys.argv[2]
	container = sys.argv[3]
	file_ptns = sys.argv[4:]

	manifest = []
	for ptn in file_ptns:
		files = glob.glob(ptn)
		manifest.extend(files)

	connector = Connector(user, key, container)
	for file in manifest:
		connector.push(file)	

