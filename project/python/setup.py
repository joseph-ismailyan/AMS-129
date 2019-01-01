import os
import numpy as np
import matplotlib.pyplot as plt
from subprocess import call

# compiles, creates txt files, removes extra files
def compile_fortran():
	os.chdir("../fortran")
	call(["make"])
	call(["make", "clean"])
	call(["./euler"])
	call(["rm", "euler"])

	return None

# calculates real value of the function
def exact_result(t):
	to_root = 2*np.log(t**2 + 1)

	return (-1 * np.sqrt(to_root + 4))

# read in file and output a tuple, t values and y values
def read_file(file_name):
	array = np.fromfile(file_name, float, -1, " ")

	t_values = array[0::2]
	y_values = array[1::2]

	return t_values, y_values

# plots the functions
def plot(t_values, y_values, nodes, output_name):

	x = t_values
	y = exact_result(x)

	error = 0
	for i in range(len(x)):
		error += abs(y[i] - y_values[i])

	plt.grid(color='gray', alpha=0.4)
	plt.title(error)
	plt.xlabel('t-axis')
	plt.ylabel('y-axis')
	plt.plot(x,y, color='blue')
	plt.plot(x,y_values, color='red', marker='o', markersize='3', ls='dashed')

	# change to ../python
	os.chdir("../python")

	# delete existing graphs
	if os.path.exists(output_name):
		os.remove(output_name)

	# save and go back to ../fortran to grab next file
	plt.savefig(output_name, dpi=300, bbox_inches='tight')
	plt.close()
	os.chdir("../fortran")
	#plt.show()

	return None
	

def main():

	# names of files to iterate through
	file_path = ["./output_8.txt", 
		     "./output_16.txt",
		     "./output_32.txt",
		     "./output_64.txt"]

	output_files = ["result_8.png",
			"result_16.png",
			"result_32.png",
			"result_64.png"]

	num_nodes = [8, 16, 32, 64]

	compile_fortran()

	# iterate thru while plotting
	for i in range(4):
		plot(read_file(file_path[i])[0], read_file(file_path[i])[1], num_nodes[i], output_files[i])

	return None

main()









