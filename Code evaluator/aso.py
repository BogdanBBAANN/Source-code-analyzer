#! /usr/bin/env python3

import sys
import os
import time
from datetime import date
from shutil import copyfile
import subprocess
import filecmp

def test_code(dirPath,ProgramName):
	# print("gcc -o " + dirPath + '/' + ProgramName[:-2] + " " + dirPath + '/' + ProgramName)
	if subprocess.call(["gcc -o " + dirPath + '/' + ProgramName[:-2] + " " + dirPath + '/' +
		ProgramName], shell = True) == 0:
		print("Successful compilation!")
		#copy input files
		copyfile("input1.txt","aso_dirs/input.txt")
		#run program
		os.system(dirPath + '/' + ProgramName[:-2])
		#check output
		ok=1
		if filecmp.cmp("output1.txt","aso_dirs/output.txt") == False:
			ok=0
			print("test1 failed")
		copyfile("input2.txt","aso_dirs/input.txt")
		#run program
		os.system(dirPath + '/' + ProgramName[:-2])
		#check output
		if filecmp.cmp("output2.txt","aso_dirs/output.txt") == False:
			ok=0
			print("test2 failed")
		copyfile("input3.txt","aso_dirs/input.txt")
		#run program
		os.system(dirPath + '/' + ProgramName[:-2])
		#check output
		if filecmp.cmp("output3.txt","aso_dirs/output.txt") == False:
			ok=0
			print("test3 failed")
		aux_string = dirPath[10:29]
		#print("result-" + ProgramName[:-2] + '-' + aux_string)
		with open(dirPath + '/' + "result-" + ProgramName[:-2] + '-' + aux_string + ".txt", 'w') as fp:
			if ok == 0:
				fp.write("Wrong answer")
			elif ok == 1:
				fp.write("Correct")
		#clean dir
	else:
		print("Compilation error for " + ProgramName)

def main(argv):
	dir_path = "/share/public_files"
	directories_path = "/aso_dirs/"
	print(directories_path)
	fPath = 0
	controlList = []
	while True:
		for fname in os.listdir(dir_path):
			fPath = os.path.join(fname)
			if fPath.endswith('.c') and not(fPath in controlList):
				controlList.append(fPath)
				aux_path = directories_path + date.today().strftime("%Y-%m-%d") + time.strftime("-%H-%M-%S-", time.localtime()) + fPath[:-2]
				print(aux_path)
				try:
					os.mkdir(aux_path, 0o755)
					copyfile(dir_path + '/' + fPath, aux_path + '/' + fPath)
					test_code(aux_path,fPath)
				except OSError:
					print("Error")
		time.sleep(5)
if __name__=='__main__':
	main(sys.argv[:])
