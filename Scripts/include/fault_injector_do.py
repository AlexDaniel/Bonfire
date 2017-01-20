import random
import sys
import numpy
from Scripts.include.package import *

class fault:
	location = None
	bitwidth = None
	Type = None
	mean_time = None
	std_dev = None 
	shut_down_time = None

	def __init__(self, loc, width, fault_type, mean_time, std_dev, shut_down_time):
		random_position = random.randint(0, width-1)
		self.location = loc+"("+str(random_position)+")"
		self.bitwidth = width
		self.Type = fault_type
		self.mean_time = mean_time
		self.std_dev = std_dev
		self.shut_down_time = shut_down_time

	def report(self):
		"""
		The fault reports its location, signal width, type, MTBF, STD_Dev and shutdown time!
		"""
		print "Location: ", self.location, "\twidth: ", self.bitwidth,  "\tfault_type: ", self.Type,\
			  "\tMTBF: ", self.mean_time, "\tstd deviation: ", self.std_dev , "\tshutdown time", \
			  self.shut_down_time

def report_faults(fault_list):
	"""
	Reports all the faults in the fault list
	"""
	print "---------------------------------------"
	print "fault injection points:"
	for fault in fault_list:
		fault.report()
	print "---------------------------------------"

def list_all_the_links(network_size):
	"""
	takes the network size and returns a list of all the RX signals in the network
	"""
	list_of_ports = []
	for i in range(0, network_size*2):
		list_of_ports.append("tb_network_"+str(network_size)+"x"+str(network_size)+":NoC:R_"+str(i)+":RX_L")
		if i/network_size != 0:
			list_of_ports.append("tb_network_"+str(network_size)+"x"+str(network_size)+":NoC:R_"+str(i)+":RX_N")
		if i/network_size != network_size-1:
			list_of_ports.append("tb_network_"+str(network_size)+"x"+str(network_size)+":NoC:R_"+str(i)+":RX_S")
		if i%network_size != 0:
			list_of_ports.append("tb_network_"+str(network_size)+"x"+str(network_size)+":NoC:R_"+str(i)+":RX_E")
		if i%network_size != network_size-1:
			list_of_ports.append("tb_network_"+str(network_size)+"x"+str(network_size)+":NoC:R_"+str(i)+":RX_W")
	return list_of_ports

def generate_links_dictionary(network_size, sim_time):
	"""
	This function generates random faults on all RX signals of the network
	"""
	list_of_ports = list_all_the_links(network_size)
	random.seed(FAULT_RANDOM_SEED)
	fault_list = []
	for item in list_of_ports:
		fault_type = random.choice(["T", "P", "I"])
		shut_down_time = None
		if fault_type == "T":
			frequency = random.choice(["H", "M", "L"])
			if frequency == "H":
				mean_time = int((1000000000/Fault_Per_Second)/HIGH_FAULT_RATE)
			elif frequency == "M":
				mean_time = int((1000000000/Fault_Per_Second)/LOW_FAULT_RATE)
			else:
				mean_time = int((1000000000/Fault_Per_Second)/MEDIUM_FAULT_RATE)
		elif fault_type == "I":
			mean_time = int(MTB_INTERMITTENT_BURST)
		else:	# its Permentent fault
			mean_time = int(1000000000/Fault_Per_Second)
			shut_down_time = random.randint(int(sim_time*0.1), int(sim_time*0.9))

		new_fault = fault(item, 32, fault_type, mean_time, int(mean_time*0.1+1), shut_down_time)
		fault_list.append(new_fault)

	report_faults(fault_list)
	return fault_list

def parse_fault_info_file(file_path):
	"""
	If you want to feed the fault info from a file...
	the file lines should be organized like this:

	fault_location:	signal_width  fault_type  MTBF  std_deviation  shutdown_time

	fault_location: the signal bit that you want to inject the fault on. 
	signal_width: 	The width of the signal that you intend to inject the bit-flip in
	fault_type: 	should be chosen from the follwoing list:
							* T : Transient
							* I : Intermittent
							* F : Faulty
	MTBF: 			Mean time between the faults
	std_deviation:	Standard deviation used for generating faults
	shutdown_time:	Time in ns when the signal would be permanently faulty only used when 
					you need permanent fault. otherwise "None".

	Example:
			tb_network_2x2:NoC:R_0:RX_L(21) 	32 	I 	1000 	101		None	
	"""

	fault_list = []
	fault_info_file = open(file_path, 'r')
	line = fault_info_file.readline()
	while line != "":
		split_line =  line.split()	
		fault_location = split_line[0]
		signal_width = int(split_line[1])
		fault_type = split_line[2]
		fault_MTBF = split_line[3]
		fault_STD = split_line[4]
		shut_down_time = split_line[5]

		new_fault = fault(fault_location, signal_width, fault_type, fault_MTBF, fault_STD, shut_down_time)
		fault_list.append(new_fault)
		line = fault_info_file.readline()

	return fault_list 


def generate_fault_injection_do(file_path, sim_time, sim_end, fault_list):
	"""
	fault_path:	string	: path to the fault_inject.do
	sim_time: integer 	: How long do you want to inject faults in the simulation ns
	sim_end:  integer 	: end of simulation
	fault_list: list  	: list of fault objects for injection
	"""
	list_of_links = fault_list
	delay = 1000000000/Fault_Per_Second
	deviation = int(delay/10)
	if deviation == 0:
		deviation = 1
	fault_inject_file = open(file_path+'/fault_inject.do', 'w')

	permanently_faulty_locations = []
	temp_dict = {}
	for item in list_of_links:
		if item.Type == "T": 
			fault_time = 0
			time_until_next_fault = numpy.random.normal(item.mean_time, item.std_dev)
			fault_time += time_until_next_fault
			while fault_time < sim_time:
				if int(fault_time) in temp_dict.keys():
					temp_dict[int(fault_time)].append(item)
				else:
					temp_dict[int(fault_time)] = [item]
				time_until_next_fault = numpy.random.normal(item.mean_time, item.std_dev)
				fault_time += time_until_next_fault
		if item.Type == "I": 
			fault_time = 0
			time_until_next_fault = numpy.random.normal(item.mean_time, item.std_dev)
			fault_time += time_until_next_fault
			while fault_time < sim_time:
				for event in range(0, EVENTS_PER_BURST):
					if int(fault_time+event) in temp_dict.keys():
						temp_dict[int(fault_time+event)].append(item)
					else:
						temp_dict[int(fault_time+event)] = [item]
				time_until_next_fault = numpy.random.normal(item.mean_time, item.std_dev)
				fault_time += time_until_next_fault

		if item.Type == "P":
			permanently_faulty_locations.append(item)
			fault_time = 0
			time_until_next_fault = numpy.random.normal(item.mean_time, item.std_dev)
			fault_time += time_until_next_fault
			while fault_time < int(item.shut_down_time*0.5):
				if int(fault_time) in temp_dict.keys():
					temp_dict[int(fault_time)].append(item)
				else:
					temp_dict[int(fault_time)] = [item]
				time_until_next_fault = numpy.random.normal(item.mean_time, item.std_dev)
				fault_time += time_until_next_fault
			time_until_next_fault = numpy.random.normal(int(MTB_INTERMITTENT_BURST), \
														int(MTB_INTERMITTENT_BURST*0.1+1))
			fault_time += time_until_next_fault
			while fault_time+EVENTS_PER_BURST < int(item.shut_down_time):
				for event in range(0, EVENTS_PER_BURST):
					if int(fault_time+event) in temp_dict.keys():
						temp_dict[int(fault_time+event)].append(item)
					else:
						temp_dict[int(fault_time+event)] = [item]
				time_until_next_fault = numpy.random.normal(int(MTB_INTERMITTENT_BURST), \
															int(MTB_INTERMITTENT_BURST*0.1+1))
				fault_time += time_until_next_fault
			

	fault_inject_file.write("#################################\n")
	current_time = 0
	for i in range(0, sim_time):
		for permanent_fault_location in permanently_faulty_locations:
			if i == permanent_fault_location.shut_down_time:
				location  = permanent_fault_location.location
				fault_inject_file.write("force -drive sim/:"+location+" U 1ns\n")
		if i in temp_dict.keys():
			last_time = current_time
			current_time = i
			fault_inject_file.write("run "+str(current_time-last_time)+"ns\n") 
			for item in temp_dict[i]:
				location = item.location
				if item.Type == "I" or item.Type == "P":
					string = "force -drive sim/:"+location+" " + str(random.choice(["0", "1"])) 
					string +=  " 0 ns -cancel 1ns"
				else:
					string = "force -drive sim/:"+location+" " + str(random.choice(["0", "1"])) 
					random_start = random.randint(0, deviation)
					string +=  " "+str(random_start)+"ns -cancel "+str(random_start+1)+"ns"
				fault_inject_file.write(string+"\n")
	
	fault_inject_file.write("run "+str(sim_end-sim_time)+"ns\n") 
	fault_inject_file.write("stop")
	fault_inject_file.close()