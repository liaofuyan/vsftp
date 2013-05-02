#coding=utf-8
import paramiko
import os
from helper import cal_relative_path

class FTP(object):
    """docstring for FTP"""
    def __init__(self, host, port, user, password, path ="/", local_path="/", protocol = 'FTP'):
        self.transport = paramiko.Transport((host, port))
        self.transport.connect(username = user, password = password)
        self.client = paramiko.SFTPClient.from_transport(self.transport)
        self.path = path
        self.local_path = local_path

    def close(self):
        self.client.close()
        self.transport.close()

    def set_path(self, path):
        self.path = path

    def upload(self,filename):

        if not os.path.exists(filename):
            print 'file not exists: %s' % filename
    	
    	dst_file = self.get_remote_file(filename)
      
        try:
            print "remote:", dst_file
            print "local:", filename
            self.client.put(filename, dst_file)
        except:
            print "upload failed!"
        else:
            print "upload successful!"

    def download(self,filename):
    	dst_file = self.get_remote_file(filename)
       
        try:
            print "remote:", dst_file
            print "local:", filename
            self.client.get(dst_file, filename)
        except:
            print "download failed!"
        else:
            print "download successful!"

    def get_remote_file(self, filename):
    	fullname = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
    	# print self.local_path
    	# print fullname
     	rel_file = cal_relative_path(fullname,self.local_path)

     	
       	rel_file =  rel_file.replace(os.sep,"/").strip("/")
        dst_file = "%s/%s" % (self.path, rel_file) 


        # print '--------------'
        # print fullname
        # print self.local_path
        # print self.path
        # print rel_file
        # print dst_file
        # print '--------------'

        return dst_file

if __name__ == "__main__":
    print "This is ftp.py"
