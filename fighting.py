# _*_ coding:utf-8 _*_

#####################################################
#		Master Entrance Examination Countdown		#
#####################################################


from tkinter import *
import time


class timer():
	def __init__(self):
		self.root = Tk()
		self.root.title('Fighting!')
		self.root.geometry('220x70')
		self.time_day = Label(text='')
		self.time_time = Label(text='')
		self.day_last = Label(text='', fg = 'red')
		
		self.time_day.pack()
		self.time_time.pack()
		self.day_last.pack()
		
		self.refresh()
		self.root.mainloop()
		
	
	def refresh(self):
		self.time_day.configure(text=time.strftime('%Y-%m-%d'))
		self.time_time.configure(text=time.strftime('%H:%M:%S'))
		self.day_last.configure(text='%d day last' %((365-(31-23))-time.localtime(time.time()).tm_yday))
		
		self.root.after(1000,self.refresh)


if __name__ == '__main__':
	def main():
		#print(time.localtime(time.time()))
		#print(type((365-(31-23))-time.localtime(time.time()).tm_yday))
		timer()
				
	main()
