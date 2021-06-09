import sys
import struct

def amplifier(input_file,output_file,amp):
	i = open(input_file,"rb")
	o = open(output_file , "wb")
	header = i.read(44)
	o.write(header)
	sample = i.read(2)
	while sample:
		sample = i.read(2)
		if sample:
			ip_data = struct.unpack('h' , sample)
			val = ip_data[0]
			val *= amp
			val = int(val)
			op_data = struct.pack('h', val)
			o.write(op_data)
	i.close()
	o.close()
	
def main():
	source = sys.argv[1]
	target = sys.argv[2]
	amplification = float(sys.argv[3])
	amplifier(source,target,amplification)

main()
	
	
