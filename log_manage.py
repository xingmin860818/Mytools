#-*-coding:utf8-*-
import zipfile
import time
import os
import re
import shutil

class Logs(object):
	def __init__(self,logpath):
		self.logpath = logpath
	#统计运行日志文件
	def statisticsLog(self):
		self.logfiles = []
		os.chdir(self.logpath)
		files = os.listdir(self.logpath)
		for file in files:
			if re.match(r'.*\.log$',file):
				self.logfiles.append(file)
		return self.logfiles
	#切割日志文件，补当前日期，并且创建新日志文件，调用服务重启接口
	def cutLog(self):
		self.timestamp = time.strftime('%Y-%m-%d',time.localtime(time.time()))
		for file in self.logfiles:
			os.rename(file,file+self.timestamp)
			os.mknod(file,0644)
	#切割日志后进行服务重新加载（nginx）
	def restartService(self,servicename):
		command = 'service {} reload'.format(servicename)
		#os.popen(command).readlines()
		os.system(command)
	#定义压缩文件函数
	def zipLog(self):
		os.chdir(self.logpath)
		files = os.listdir(self.logpath)
		for file in files:
			if re.match(r'.*\.log\d{4}-\d{2}-\d{2}$',file):
				f = zipfile.ZipFile(file+'.zip','w',zipfile.ZIP_DEFLATED)
				f.write(file)
				f.close()
				os.remove(file)
	#备份压缩日志文件
	def backup(self,backpath):
		backdir = os.path.join(backpath,self.timestamp)
		if not os.path.exists(backdir):
			os.mkdir(backdir,0755)
		os.chdir(self.logpath)
		files = os.listdir(self.logpath)
		for file in files:
			if re.match(r'.*\.log\d{4}-\d{2}-\d{2}\.zip$',file):
				shutil.copy(file,backdir)
				os.remove(file)

if __name__ == '__main__':
	l = Logs('/var/log/nginx/')
	l.statisticsLog()
	l.cutLog()
	l.restartService('nginx')
	l.zipLog()
	l.backup('/tmp/')


        
