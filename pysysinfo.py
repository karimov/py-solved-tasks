#!/usr/bin/env python
#A System Information Gathering Script
import subprocess
#Command 1
def uname_func():

	uname="uname"
	uname_arg = "-a"
	print "Gathering system information with %s command:\n" % uname
	subprocess.call([uname, uname_arg])

#Command 2
def df_func():

	diskspace = "df"
	diskspace_arg = "-h"
	print "Gathering diskspace information %s command:\n" % diskspace
	subprocess.call([diskspace, diskspace_arg])

def main():

	uname_func()
	df_func()
	
main()

