# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_imu_driver')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_imu_driver')
    _imu_driver = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_imu_driver', [dirname(__file__)])
        except ImportError:
            import _imu_driver
            return _imu_driver
        if fp is not None:
            try:
                _mod = imp.load_module('_imu_driver', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _imu_driver = swig_import_helper()
    del swig_import_helper
else:
    import _imu_driver
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class imu_vector_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, imu_vector_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, imu_vector_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _imu_driver.imu_vector_t_x_set
    __swig_getmethods__["x"] = _imu_driver.imu_vector_t_x_get
    if _newclass:
        x = _swig_property(_imu_driver.imu_vector_t_x_get, _imu_driver.imu_vector_t_x_set)
    __swig_setmethods__["y"] = _imu_driver.imu_vector_t_y_set
    __swig_getmethods__["y"] = _imu_driver.imu_vector_t_y_get
    if _newclass:
        y = _swig_property(_imu_driver.imu_vector_t_y_get, _imu_driver.imu_vector_t_y_set)
    __swig_setmethods__["z"] = _imu_driver.imu_vector_t_z_set
    __swig_getmethods__["z"] = _imu_driver.imu_vector_t_z_get
    if _newclass:
        z = _swig_property(_imu_driver.imu_vector_t_z_get, _imu_driver.imu_vector_t_z_set)

    def __init__(self):
        this = _imu_driver.new_imu_vector_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _imu_driver.delete_imu_vector_t
    __del__ = lambda self: None
imu_vector_t_swigregister = _imu_driver.imu_vector_t_swigregister
imu_vector_t_swigregister(imu_vector_t)

class imu_data_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, imu_data_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, imu_data_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["acc"] = _imu_driver.imu_data_t_acc_set
    __swig_getmethods__["acc"] = _imu_driver.imu_data_t_acc_get
    if _newclass:
        acc = _swig_property(_imu_driver.imu_data_t_acc_get, _imu_driver.imu_data_t_acc_set)
    __swig_setmethods__["gyr"] = _imu_driver.imu_data_t_gyr_set
    __swig_getmethods__["gyr"] = _imu_driver.imu_data_t_gyr_get
    if _newclass:
        gyr = _swig_property(_imu_driver.imu_data_t_gyr_get, _imu_driver.imu_data_t_gyr_set)
    __swig_setmethods__["mag"] = _imu_driver.imu_data_t_mag_set
    __swig_getmethods__["mag"] = _imu_driver.imu_data_t_mag_get
    if _newclass:
        mag = _swig_property(_imu_driver.imu_data_t_mag_get, _imu_driver.imu_data_t_mag_set)
    __swig_setmethods__["qw"] = _imu_driver.imu_data_t_qw_set
    __swig_getmethods__["qw"] = _imu_driver.imu_data_t_qw_get
    if _newclass:
        qw = _swig_property(_imu_driver.imu_data_t_qw_get, _imu_driver.imu_data_t_qw_set)
    __swig_setmethods__["qx"] = _imu_driver.imu_data_t_qx_set
    __swig_getmethods__["qx"] = _imu_driver.imu_data_t_qx_get
    if _newclass:
        qx = _swig_property(_imu_driver.imu_data_t_qx_get, _imu_driver.imu_data_t_qx_set)
    __swig_setmethods__["qy"] = _imu_driver.imu_data_t_qy_set
    __swig_getmethods__["qy"] = _imu_driver.imu_data_t_qy_get
    if _newclass:
        qy = _swig_property(_imu_driver.imu_data_t_qy_get, _imu_driver.imu_data_t_qy_set)
    __swig_setmethods__["qz"] = _imu_driver.imu_data_t_qz_set
    __swig_getmethods__["qz"] = _imu_driver.imu_data_t_qz_get
    if _newclass:
        qz = _swig_property(_imu_driver.imu_data_t_qz_get, _imu_driver.imu_data_t_qz_set)
    __swig_setmethods__["roll"] = _imu_driver.imu_data_t_roll_set
    __swig_getmethods__["roll"] = _imu_driver.imu_data_t_roll_get
    if _newclass:
        roll = _swig_property(_imu_driver.imu_data_t_roll_get, _imu_driver.imu_data_t_roll_set)
    __swig_setmethods__["pitch"] = _imu_driver.imu_data_t_pitch_set
    __swig_getmethods__["pitch"] = _imu_driver.imu_data_t_pitch_get
    if _newclass:
        pitch = _swig_property(_imu_driver.imu_data_t_pitch_get, _imu_driver.imu_data_t_pitch_set)
    __swig_setmethods__["yaw"] = _imu_driver.imu_data_t_yaw_set
    __swig_getmethods__["yaw"] = _imu_driver.imu_data_t_yaw_get
    if _newclass:
        yaw = _swig_property(_imu_driver.imu_data_t_yaw_get, _imu_driver.imu_data_t_yaw_set)
    __swig_setmethods__["raw_roll"] = _imu_driver.imu_data_t_raw_roll_set
    __swig_getmethods__["raw_roll"] = _imu_driver.imu_data_t_raw_roll_get
    if _newclass:
        raw_roll = _swig_property(_imu_driver.imu_data_t_raw_roll_get, _imu_driver.imu_data_t_raw_roll_set)
    __swig_setmethods__["raw_pitch"] = _imu_driver.imu_data_t_raw_pitch_set
    __swig_getmethods__["raw_pitch"] = _imu_driver.imu_data_t_raw_pitch_get
    if _newclass:
        raw_pitch = _swig_property(_imu_driver.imu_data_t_raw_pitch_get, _imu_driver.imu_data_t_raw_pitch_set)
    __swig_setmethods__["raw_yaw"] = _imu_driver.imu_data_t_raw_yaw_set
    __swig_getmethods__["raw_yaw"] = _imu_driver.imu_data_t_raw_yaw_get
    if _newclass:
        raw_yaw = _swig_property(_imu_driver.imu_data_t_raw_yaw_get, _imu_driver.imu_data_t_raw_yaw_set)

    def __init__(self):
        this = _imu_driver.new_imu_data_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _imu_driver.delete_imu_data_t
    __del__ = lambda self: None
imu_data_t_swigregister = _imu_driver.imu_data_t_swigregister
imu_data_t_swigregister(imu_data_t)

class LSM9DS0(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LSM9DS0, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LSM9DS0, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _imu_driver.new_LSM9DS0()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _imu_driver.delete_LSM9DS0
    __del__ = lambda self: None

    def read(self) -> "imu_data_t":
        return _imu_driver.LSM9DS0_read(self)

    def getPollInterval(self) -> "int":
        return _imu_driver.LSM9DS0_getPollInterval(self)
LSM9DS0_swigregister = _imu_driver.LSM9DS0_swigregister
LSM9DS0_swigregister(LSM9DS0)

# This file is compatible with both classic and new-style classes.


