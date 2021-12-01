""" Make comparing version strings super simple.

If you want codes using your package to be able to verify its version as easily as::

  # user_code.py
  import my_package
  assert my_package.__version__ >= "1.1"

Just customize your package as follows::

  # my_package/__init__.py
  import verstr
  __version__ = verstr.verstr("1.2.4")

"""

import collections
import packaging.version


__all__ = ['verstr']


def verstr(str_version, mode="str"):
    """ returns a comparable version object.

    verstr(str_version)
    verstr(str_version, mode)

    Parameters
    ----------
    str_version: str
        A string that follows PEP 440, the standard version scheme for Python packages
    mode: str
        A string to select the type of the returned value.

    Returns
    -------
    VersionCompareMixin
        The comparable version object.
        Its type depends on the `mode` argument:
            'str' -> VersionString
            'userstr' -> VersionUserString
            'interface' -> VersionInterface

    """
    modes = dict(
        str=VersionString,
        userstr=VersionUserString,
        interface=VersionInterface
    )
    try:
        cls = modes[mode]
    except KeyError:
        raise ValueError(
            f"'mode' argument must be in {list(modes)}, "
            f"get {mode!r} instead."
        )
    return cls(str_version)


def to_version(str_version):
    return packaging.version.Version(str(str_version))


class VersionCompareMixin:

    def _comp_op(str_op):
        def op(self, other):
            return getattr(to_version(self), str_op)(to_version(other))
        op.__name__ = str_op
        return op

    __eq__ = _comp_op("__eq__")
    __lt__ = _comp_op("__lt__")
    __le__ = _comp_op("__le__")
    __gt__ = _comp_op("__gt__")
    __ge__ = _comp_op("__ge__")

    del _comp_op


class VersionString(VersionCompareMixin, str):

    def __new__(cls, object):
        return super().__new__(cls, str(to_version(object)))


class VersionUserString(VersionCompareMixin, collections.UserString):

    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self.__dict__['data']

    @data.setter
    def data(self, data):
        self.__dict__['data'] = str(to_version(data))


class VersionInterface(VersionCompareMixin):

    def __init__(self, version):
        self._version = to_version(version)

    def __repr__(self):
        return str(self._version)


try:
    from . import _version
    __version__ = verstr(_version.version)
except ImportError:
    __version__ = None

