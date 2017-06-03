
# -*- coding: utf-8 -*-
import sys,os



def main():
	print '''

	_                                   
 ___| |_ _ __ __ _ _ __   __ _  ___ _ __ 
/ __| __| '__/ _` | '_ \ / _` |/ _ \ '__|
\__ \ |_| | | (_| | | | | (_| |  __/ |   
|___/\__|_|  \__,_|_| |_|\__, |\___|_|   ---- lazzy erha QQ:1356720321
                         |___/  
未优化未模块化内部测试版：V0.0.2
注意请全部小写!
	'''
	print '读取工具手册还是存入工具手册?'
	try:
		a=raw_input('1为读取，2为存储,3查看目录,4删除相关资料:>')
		a=int(a)
	except:
		print '\n终止退出!'
		exit(0)
	if  a==1:
		print '1——》读取'
		a=raw_input('\n你需要查什么？:> ')
		a=a.lower()
		if os.path.isfile('mankali.ppx'):
			print '目录文件找到!\n'
			mulu=open('mankali.ppx')
			for line in mulu.readlines():
				line=line.strip('\n')
				if a==line:
					print '资料 '+a+'找到,下一行正文起始:\n'
					os.system('leafpad '+a+'help.file\n')
					mulu.close()
					exit(0)
				else:
					pass
			if a!=line:
				print '资料没有找到'
		else:
			try :
				os.system('touch mankali.ppx')
				print '初始化目录文件成功!重新运行开始装填资料'
			except:
				print '无权限失败'
	elif a==2:
		print '2-->存储'
		a=raw_input('给什么工具装填资料?:\n')
		a=a.lower()
		mulu=open('mankali.ppx','r')
		for line in mulu.readlines():
			line=line.strip('\n')
			if a==line:
				print '找到冗余,修改?'+a
				os.system('leafpad '+a+"help.file")
				exit(0)
		if os.path.isfile('mankali.ppx'):
			print '找到目录文件开始装填!:'
			file=open('mankali.ppx','a')
			file.write("\n"+a)
			file.write('\n')
			file.close()
			print '开始装填'
		if not os.path.isfile(a+'help.file'):
			os.mknod(a+"help.file")
			os.system('leafpad '+a+"help.file")
			print '写完了！'
	elif a==3:
		os.system('cat mankali.ppx')

	elif a==4:
		a=raw_input('要删除什么工具的资料？: ')
		os.system('rm '+a+'help.file')
		mulu=open('mankali.ppx','wr')
		lis=['']
		for line in mulu.readlines():
			line=line.strip('\n')
			if line!=a:
				lis.append(line)
		for i in lis[0:]:
			mulu.write(i+'\n')
		mulu.close()
	else:
		print '不是1或者2 无效'


if __name__ == '__main__':
	main()
