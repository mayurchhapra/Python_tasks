from multiprocessing import Pool, Process
import os

# def f(a):
# 	return a*a

# if __name__ == '__main__':
# 	p = Pool(1)
# 	print(p.map(f,[1,2,3,4]))

def info(title):
	print title
	print "Module Name: ",__name__
	if hasattr(os,'getppid'):
		print 'Parent Process: ',os.getppid()
	print 'process id: ',os.getpid()

def f(name):
	info('Function f')
	print 'Hello',name

if __name__ == '__main__':
	p = Process(target = f,args=('Mayur',))
	p.start()
	p.join()