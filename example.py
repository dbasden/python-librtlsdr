#! /usr/bin/env python

from rtlsdr import RtlSDR
import sys

if __name__ == "__main__":

	if len(sys.argv) < 2:
		print >> sys.stderr, sys.argv[0], "<outfile>"
		sys.exit(1)

	if RtlSDR.get_device_count() < 1:
		raise IOError("No known devices found")

	s = RtlSDR(0, 105700000, 1024000)

	# This is actually a property that changes the frequency
	s.frequency = 54000000
	s.frequency = 927000000
	s.frequency = 435012000
	s.frequency = 145125000
	s.frequency = 130100000
	s.frequency = 105700000

	s.reset_buffer() # Must do before first read
	buf = s.read()
	outf = open(sys.argv[1], "w")

	try:
		while True:
			outf.write(s.read())
	except KeyboardInterrupt:
		pass
	finally:
		outf.close()
		s.close()
