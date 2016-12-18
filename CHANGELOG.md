1.2   (..........)
----------------
- Don't ignore the --no-delete option.
- Print better message when run out of retries.
- Delete images even if no usable ones were found.
- Reset usages for downloaded images. Now the same image that was seen before
  can be downloaded again if it makes it to the top of the imgur results
  again.

1.1.1 (2016-04-07)
------------------

- Add catimg --version
- Enable Travis CI
- Add description to catimg --help

1.1 (2015-08-06)
----------------

- Remove catimg.iterm2. Add dependency on iterm2-tools.
- Lock the usages file (with retries). Usages will now be more accurate for
  concurrent catimg runs.

1.0.4 (2015-08-04)
------------------

- Add zip_safe=False to setup.py
- Install the tests

1.0.3 (2015-07-16)
------------------

- Fix pip install when requests and imgurpython aren't already installed.
- Use versioneer.

1.0.2 (2015-07-16)
------------------

- Grammar fix.
- Correctly print newline after the cat image.
- Add __version__.

1.0.1 (2015-07-14)
------------------

- Fix to setup.py.

1.0 (2015-07-14)
----------------

- Initial release.
