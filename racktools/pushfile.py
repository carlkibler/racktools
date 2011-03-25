import cloudfiles
cloud_user = MY_CLOUD_USER
cloud_key = MY_CLOUD_KEY
cloud_container = 'FILES'

conn =  cloudfiles.get_connection(cloud_user, cloud_key)
container = conn.get_container(cloud_container)

# open a file and write the descriptor
fd = open(FILENAME,'rb')
ob = container.create_object('name of my file') # you can use fd.name to pull it from the file descriptor
ob.content_type = 'application/zip'
# you can use the save(fd) method if the source is changing and you want to provide a stream
ob.write(fd)
fd.close()

