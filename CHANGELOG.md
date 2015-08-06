1.1
---

- Remove catimg.iterm2. Add dependency on iterm2-tools.
- Lock the usages file (with retries). Usages will now be more accurate for
  concurrent catimg runs.

1.0.4
-----

- Add zip_safe=False to setup.py
- Install the tests

1.0.3
-----

- Fix pip install when requests and imgurpython aren't already installed.
- Use versioneer.

1.0.2
-----

- Grammar fix.
- Correctly print newline after the cat image.
- Add __version__.

1.0.1
-----

- Fix to setup.py.

1.0
---

- Initial release.
