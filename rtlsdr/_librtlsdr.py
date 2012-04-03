from ctypes import *

_libraries = {}
_libraries['librtlsdr.so'] = CDLL('librtlsdr.so')
STRING = c_char_p


int8_t = c_int8
int16_t = c_int16
int32_t = c_int32
int64_t = c_int64
uint8_t = c_uint8
uint16_t = c_uint16
uint32_t = c_uint32
uint64_t = c_uint64
int_least8_t = c_byte
int_least16_t = c_short
int_least32_t = c_int
int_least64_t = c_long
uint_least8_t = c_ubyte
uint_least16_t = c_ushort
uint_least32_t = c_uint
uint_least64_t = c_ulong
int_fast8_t = c_byte
int_fast16_t = c_long
int_fast32_t = c_long
int_fast64_t = c_long
uint_fast8_t = c_ubyte
uint_fast16_t = c_ulong
uint_fast32_t = c_ulong
uint_fast64_t = c_ulong
intptr_t = c_long
uintptr_t = c_ulong
intmax_t = c_long
uintmax_t = c_ulong
class rtlsdr_dev(Structure):
    pass
rtlsdr_dev_t = rtlsdr_dev
rtlsdr_dev._fields_ = [
]
rtlsdr_get_device_count = _libraries['librtlsdr.so'].rtlsdr_get_device_count
rtlsdr_get_device_count.restype = uint32_t
rtlsdr_get_device_count.argtypes = []
rtlsdr_get_device_name = _libraries['librtlsdr.so'].rtlsdr_get_device_name
rtlsdr_get_device_name.restype = STRING
rtlsdr_get_device_name.argtypes = [uint32_t]
rtlsdr_open = _libraries['librtlsdr.so'].rtlsdr_open
rtlsdr_open.restype = c_int
rtlsdr_open.argtypes = [POINTER(POINTER(rtlsdr_dev_t)), uint32_t]
rtlsdr_close = _libraries['librtlsdr.so'].rtlsdr_close
rtlsdr_close.restype = c_int
rtlsdr_close.argtypes = [POINTER(rtlsdr_dev_t)]
rtlsdr_set_center_freq = _libraries['librtlsdr.so'].rtlsdr_set_center_freq
rtlsdr_set_center_freq.restype = c_int
rtlsdr_set_center_freq.argtypes = [POINTER(rtlsdr_dev_t), uint32_t]
rtlsdr_get_center_freq = _libraries['librtlsdr.so'].rtlsdr_get_center_freq
rtlsdr_get_center_freq.restype = c_int
rtlsdr_get_center_freq.argtypes = [POINTER(rtlsdr_dev_t)]
rtlsdr_set_freq_correction = _libraries['librtlsdr.so'].rtlsdr_set_freq_correction
rtlsdr_set_freq_correction.restype = c_int
rtlsdr_set_freq_correction.argtypes = [POINTER(rtlsdr_dev_t), c_int]
rtlsdr_get_freq_correction = _libraries['librtlsdr.so'].rtlsdr_get_freq_correction
rtlsdr_get_freq_correction.restype = c_int
rtlsdr_get_freq_correction.argtypes = [POINTER(rtlsdr_dev_t)]
rtlsdr_set_tuner_gain = _libraries['librtlsdr.so'].rtlsdr_set_tuner_gain
rtlsdr_set_tuner_gain.restype = c_int
rtlsdr_set_tuner_gain.argtypes = [POINTER(rtlsdr_dev_t), c_int]
rtlsdr_get_tuner_gain = _libraries['librtlsdr.so'].rtlsdr_get_tuner_gain
rtlsdr_get_tuner_gain.restype = c_int
rtlsdr_get_tuner_gain.argtypes = [POINTER(rtlsdr_dev_t)]
rtlsdr_set_sample_rate = _libraries['librtlsdr.so'].rtlsdr_set_sample_rate
rtlsdr_set_sample_rate.restype = c_int
rtlsdr_set_sample_rate.argtypes = [POINTER(rtlsdr_dev_t), uint32_t]
rtlsdr_get_sample_rate = _libraries['librtlsdr.so'].rtlsdr_get_sample_rate
rtlsdr_get_sample_rate.restype = c_int
rtlsdr_get_sample_rate.argtypes = [POINTER(rtlsdr_dev_t)]
rtlsdr_reset_buffer = _libraries['librtlsdr.so'].rtlsdr_reset_buffer
rtlsdr_reset_buffer.restype = c_int
rtlsdr_reset_buffer.argtypes = [POINTER(rtlsdr_dev_t)]
rtlsdr_read_sync = _libraries['librtlsdr.so'].rtlsdr_read_sync
rtlsdr_read_sync.restype = c_int
rtlsdr_read_sync.argtypes = [POINTER(rtlsdr_dev_t), c_void_p, c_int, POINTER(c_int)]
rtlsdr_async_read_cb_t = CFUNCTYPE(None, STRING, uint32_t, c_void_p)
rtlsdr_wait_async = _libraries['librtlsdr.so'].rtlsdr_wait_async
rtlsdr_wait_async.restype = c_int
rtlsdr_wait_async.argtypes = [POINTER(rtlsdr_dev_t), rtlsdr_async_read_cb_t, c_void_p]
rtlsdr_cancel_async = _libraries['librtlsdr.so'].rtlsdr_cancel_async
rtlsdr_cancel_async.restype = c_int
rtlsdr_cancel_async.argtypes = [POINTER(rtlsdr_dev_t)]
__all__ = ['rtlsdr_read_sync', 'rtlsdr_set_center_freq',
           'rtlsdr_get_freq_correction', 'int32_t', 'uint_least64_t',
           'uintptr_t', 'uintmax_t', 'int_fast32_t', 'int16_t',
           'int64_t', 'int_fast16_t', 'rtlsdr_set_sample_rate',
           'rtlsdr_set_tuner_gain', 'int_fast64_t',
           'rtlsdr_async_read_cb_t', 'uint8_t', 'int_least8_t',
           'rtlsdr_get_device_count', 'rtlsdr_open', 'uint_least16_t',
           'rtlsdr_reset_buffer', 'uint_least32_t', 'int_least64_t',
           'int_least16_t', 'int_fast8_t', 'uint_least8_t',
           'rtlsdr_set_freq_correction', 'intptr_t', 'int_least32_t',
           'int8_t', 'rtlsdr_wait_async', 'rtlsdr_dev',
           'rtlsdr_dev_t', 'rtlsdr_get_tuner_gain',
           'rtlsdr_get_sample_rate', 'rtlsdr_cancel_async',
           'uint_fast32_t', 'uint_fast64_t', 'intmax_t',
           'rtlsdr_close', 'rtlsdr_get_device_name', 'uint_fast16_t',
           'rtlsdr_get_center_freq', 'uint32_t', 'uint64_t',
           'uint16_t', 'uint_fast8_t']
