# Report issues
If you have any issue with `verstr`, please start by updating to the last version and see if the bug is still there.

If it is, check if the problem has not already been [reported](https://github.com/BRGM/verstr/issues) and if not, just [open an issue](https://github.com/BRGM/verstr/issues/new) with with the basic information.
If in doubt, check out [what to put in your bug report](https://www.contribution-guide.org/#what-to-put-in-your-bug-report).

Feature requests are also welcome on the [issue tracker](https://github.com/BRGM/verstr/issues) but keep in mind that `verstr` aims to keep it simple.

# Make a pull request
Please fork the `verstr` repository on Github, and create a new branch containing your work. When you are done, open a pull request.

# Developing

[Create and activate a Python 3 virtual environment.](https://docs.python.org/3/tutorial/venv.html)

Install `verstr` for development:

```bash
pip install -r requirements.txt
pip install -e .
```

Run unit tests:

```bash
pytest
```
