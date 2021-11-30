# verstr

Make comparing version strings super simple.

## Quick start

If you want to check that a code use the appropriate version of your package as easy as:

```python
# user_code.py
import my_package
assert my_package.__version__ >= "1.1"
```

You can custom your package as follows:

```python
# my_package/__init__.py
import verstr
__version__ = verstr.verstr("1.2.4")
```

or, if you are using `setuptools_scm`:

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

You are welcome to help the project, see [how](/CONTRIBUTING.md).

## License

[MIT](https://opensource.org/licenses/MIT)
