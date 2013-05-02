" Vim script
" Author: Aliao 
" Last Change: April 25, 2013
" URL: 


" Don't load the plug-in when &compatible is set or it was already loaded.
if &cp || exists('g:ftp_plugin')
  finish
endif
map <S-A-d> :call UploadFile()<CR>

let g:plugin_dir = expand("<sfile>")
function! UploadFile()
    let g:cur_file = CurFile() 
    let g:cur_dir = getcwd()
python << EOF
import vim
cur_file = vim.eval("g:cur_file")
cur_dir= vim.eval("g:cur_dir")
#print cur_file
#print cur_dir
import os
import sys
plugin_dir = os.path.dirname(vim.eval("g:plugin_dir"))
plugin_dir_old = os.getcwd()
  
path = cur_dir #"E:/work/freemerce/project/python/crawler/lfy/ftp/" 
path = os.path.abspath(os.path.join("./", path))
fname = cur_file # "E:/work/freemerce/project/python/crawler/lfy/ftp/1.txt"
fname = os.path.abspath(os.path.join("./", fname))
os.chdir(plugin_dir)
sys.path.append(plugin_dir + "/ftp")

from manager import Manager
mgr = Manager(path)
mgr.uploadfile(fname)

os.chdir(plugin_dir_old)
EOF
endfunction

function! DownloadFile()
    let g:cur_file = CurFile() 
    let g:cur_dir = getcwd()
python << EOF
import vim
cur_file = vim.eval("g:cur_file")
cur_dir= vim.eval("g:cur_dir")
#print cur_file
#print cur_dir
import os
import sys
plugin_dir = os.path.dirname(vim.eval("g:plugin_dir"))
plugin_dir_old = os.getcwd()
  
path = cur_dir #"E:/work/freemerce/project/python/crawler/lfy/ftp/" 
path = os.path.abspath(os.path.join("./", path))
fname = cur_file # "E:/work/freemerce/project/python/crawler/lfy/ftp/1.txt"
fname = os.path.abspath(os.path.join("./", fname))
os.chdir(plugin_dir)
sys.path.append(plugin_dir + "/ftp")

from manager import Manager
mgr = Manager(path)
mgr.downloadfile(fname)

os.chdir(plugin_dir_old)
EOF
endfunction

function! CurFile()
    let curfile = bufname("%")
    let curdir = getcwd()
    return curdir .'/'. curfile 
endfunction

let g:ftp_plugin = 1
