#coding=utf-8

from ftp import FTP
from cfg import config

class Manager(object):
    def __init__(self, path):

        self.init_ftp(path)

    def init_ftp(self, path):
        pass
        conf = config().get_cfg(path, 'ftp.conf')
        try:
            self.ftp = FTP(conf['host'], conf['port'],conf['user'], conf['password'], conf['path'], conf['local_path'], conf['protocol'])
        except Exception, e:
            raise e
    def uploadfile(self, fname):
        pass
        self.ftp.upload(fname)
    def downloadfile(self, fname):
        pass
        self.ftp.download(fname)
    
if __name__ == "__main__":
    path = "./"
    mgr = Manager(path)
    fname = "./1.txt"
    # mgr.uploadfile(fname)
    mgr.downloadfile(fname)
