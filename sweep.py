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

	outf = open(sys.argv[1], "w")
	#s.reset_buffer() # Must do before first read

	try:
		for n in range(500,10000,5):
			n = n *.1
			print >> sys.stderr, n,"MHz", 
			s.frequency = int(n * 10**6)
			s.reset_buffer()
			for c in xrange(3):
				outf.write(s.read())
	except KeyboardInterrupt:
		pass
	finally:
		outf.close()
		s.close()
