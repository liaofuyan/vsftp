#coding=utf-8
import ConfigParser
import os
class config(object):
    def __init__(self):
        pass
    def load_conf(self,cfg_file):

        cf = ConfigParser.ConfigParser()
        cf.read(cfg_file)

        host = cf.get('ftp',"host")
        port = cf.getint('ftp',"port")
        protocol = cf.get('ftp',"protocol")
        user = cf.get('ftp',"user")
        password = cf.get('ftp',"password")
        path= cf.get('ftp',"path")
        conf = {}
        conf['host'] = host
        conf['port'] = port
        conf['protocol'] = protocol
        conf['user'] = user
        conf['password'] = password
        conf['path'] = path 

        return conf
    def get_parent_path(self,path):
        print path
        parent = os.path.dirname(path)
        if parent == path:
            return ""
        return parent

    def get_cfg_file(self,path, name = "ftp.conf"):
        file_name = name
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), path))
        file_dir = path
        while 1:
            full_name = "%s/%s" % (file_dir, file_name)
            if os.path.isfile(full_name):
                return full_name
            # print full_name
            # print file_dir
            print '-------------'
            print file_dir
            file_dir = self.get_parent_path(file_dir)
            if not os.path.isdir(file_dir):
                break

        return None

    def get_cfg(self,path,name = "ftp.conf"):
        # print path
        # print nameile
        print '++++++++++++'
        print path
        print name
        print '++++++++++++'
        cfg_file = self.get_cfg_file(path, name)
        print '++++++++++++'
        print cfg_file
        local_path = self.get_parent_path(cfg_file)
        if not os.path.isfile(cfg_file):
            return None
        conf = self.load_conf(cfg_file)
        conf['local_path'] = local_path
        return conf


  

if __name__ == "__main__":

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "\\www\\text"))
    print os.path.dirname(__file__)
    print __file__
    print path
    # print config().cal_relative_path(p1,p2)
