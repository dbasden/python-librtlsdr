#! /usr/bin/env python

import _librtlsdr as sdr
import ctypes
from ctypes import pointer
import sys

class RtlSDR(object):
	READ_SIZE = 16 * 16384

	def __init__(self, device_index=0, center_frequency=105400000, sample_rate=1024000, tuner_gain=0):
		'''initialise the rtlsdr device and tune to initial frequency
		'''
		self.dev = sdr.rtlsdr_dev_t()
		self.devp = pointer(self.dev)
		self.devidx = device_index

		if sdr.rtlsdr_open(self.devp, device_index) < 0:
			raise IOError("Couldn't open sdr device index %d" % (device_index,) )
		print >> sys.stderr, "Using", sdr.rtlsdr_get_device_name(0)
		self.__closed = False

		self.set_sample_rate(sample_rate)
		self.set_center_freq(center_frequency)
		self.set_tuner_gain(tuner_gain)
		self._buf = ctypes.create_string_buffer(self.READ_SIZE)

	def set_sample_rate(self, sample_rate):
		if sdr.rtlsdr_set_sample_rate(self.devp, sample_rate) != 0:
			self.close()
			raise IOError("Couldn't set sample rate")
		self._sample_rate = sample_rate
	def get_sample_rate(self):
		return self._sample_rate
	sample_rate = property(get_sample_rate, set_sample_rate)

	def set_tuner_gain(self, gain):
		if sdr.rtlsdr_set_tuner_gain(self.devp, gain) < 0:
			raise IOError("Couldn't set tuner gain")
		self._tuner_gain = gain
	def get_tuner_gain(self):
		return self._tuner_gain
	tuner_gain = property(get_tuner_gain, set_tuner_gain)


	def set_center_freq(self, center_freq):
		if sdr.rtlsdr_set_center_freq(self.devp, center_freq) != 0:
			self.close()
			raise IOError("Couldn't set center frequency")
		self._center_freq = center_freq
	def get_center_freq(self):
		return self._center_freq
	center_freq = property(get_center_freq, set_center_freq)
	frequency = property(get_center_freq, set_center_freq)

	def reset_buffer(self):
		'''reset hardware buffers
		MUST be called before first read
		'''
		if sdr.rtlsdr_reset_buffer(self.devp) < 0:
			raise IOError("Couldn't reset hardware buffers")

	def read(self):
		'''read data into our buffer
		You'll be returned a ctypes string buffer.
		THIS IS PRETTY DANGEROUS. Treat it as you would
		C memory. You can pretty easily crash python
		messing with it

		The buffer is re-used, so get stuff out before you
		call read() again
		'''
		readp = pointer(ctypes.c_int32())
		r = sdr.rtlsdr_read_sync(self.devp,self._buf, self.READ_SIZE, readp)
		if r < 0: raise IOError("Error reading from device")
		if readp < self.READ_SIZE: raise IOError("Short read!")

		return self._buf.raw

	def close(self):
		if not self.__closed:
			sdr.rtlsdr_close(self.devp)
			self.__closed = True

	@staticmethod
	def get_device_count():
		return sdr.rtlsdr_get_device_count()

if __name__ == "__main__":
	if RtlSDR.get_device_count() < 1:
		raise IOError("No known devices found")

	s = RtlSDR(0, 105700000, 1024000)
	s.frequency = 54000000
	s.frequency = 927000000
	s.frequency = 435012000
	s.frequency = 145125000
	s.frequency = 130100000
	s.frequency = 105700000
	s.reset_buffer()
	f = open("pytest.bin", "w")
	buf = s.read()
	f.write(buf)
	f.close()
	s.close()
