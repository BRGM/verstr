# verstr

Make comparing version strings super simple.

## Quick start

If you want codes using your package to be able to verify its version as easily as:

```python
# user_code.py
import my_package
assert my_package.__version__ >= "1.1"
```

Just customize your package as follows:

```python
# my_package/__init__.py
import verstr
__version__ = verstr.verstr("1.2.4")
```

or if you are using a tool such as [`setuptools_scm`]() to generate a `_version.py` submodule:

```python
# my_package/__init__.py
import verstr
try:
    from . import _version
    __version__ = verstr.verstr(_version.version)
except ImportError:
    __version__ = None
```

## Installation 

Install `verstr` with pip

```bash 
  pip install verstr
```

## Contributing

You are welcome to help the project, see [how](https://github.com/BRGM/verstr/blob/main/CONTRIBUTING.md).

## License

[MIT](https://opensource.org/licenses/MIT)
