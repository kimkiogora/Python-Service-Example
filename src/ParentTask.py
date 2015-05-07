################################################################################################
# @Author	: Kim Kiogora <kimkiogora@gmail.com>
# @version	: 2.0 , 15/01/12
# @Usage
#-------
#This is the Daemon's job class. It performs any request sent to it from the parent class
##################################################################################################
import urllib
import string
import os

class Task:
	#variables
	global mydata;

	#constructor
	def __init__(self,data):
		"""Pass your data here"""
		self.mydata = data

	#initfunction
	def processData(self):
		"""Do something with your data, mydata variable """
		
	
#############################################
#END THE  JOB CLASS
#############################################
