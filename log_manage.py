#-*-coding:utf8-*-
import zipfile
import time
import os
import re

#定义切割文件
def cutLog(logdir):
	timestamp = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	os.chdir(logdir)
	files = os.listdir('.')
	for file in files:
		if re.match(r'.*\.log$',file):
			os.rename(file,file+timestamp)
			os.mkfifo(file)
			break
def restartService(servicename):
	command = 'service {} reload'.format(servicename)
	os.popen(command)
#定义压缩文件函数
def zipLog(filelist):
	timestamp = timestamp = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	file = zipfile.ZipFile('xxxx.zip','w',zipfile.ZIP_DEFLATED)
	file.write('file_to_add.log')
	f.close()
print restartService('/etc/init.d/nginx restart')
