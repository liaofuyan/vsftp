 #coding=utf-8
import os
def cal_relative_path(path1, path2):
    '''为了简化，必须传入全路径'''
    if path1 == path2:
        return ""
    tmp_p1 = path1 if len(path1) >= len(path2) else path2
    tmp_p2 = path1 if len(path1) < len(path2) else path2

    return tmp_p1.replace(tmp_p2,"")

