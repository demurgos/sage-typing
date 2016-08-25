<img
  src="./logo.png"
  alt="Sage Typing Logo"
  title="Sage Typing"
  align="right"
/>

# Sage-Typing

This repository provides [Python type hints][typing-pep] for [Sage][sage-website].

This allows editor to provide auto-completion for Sage. It is especially useful when you are
using Windows to write your Python scripts depending on Sage (and then execute them on
another machine).

[typing-pep]: https://www.python.org/dev/peps/pep-0484/
[sage-website]: http://www.sagemath.org/

## Installation

Clone this repository and add it to your `PYTHONPATH` environment variable.

### Windows

```shell
git clone https://github.com/demurgos/sage-typing.git
setx PYTHONPATH "%PYTHONPATH%;%CD%\sage-typing"
```

## Supported editors

The above installation is verified for:

- [PyCharm][pycharm-website]

If you use other editors, send a PR to add it to the list.

[pycharm-website]: https://www.jetbrains.com/pycharm/

## Available modules

I mostly add type hints when I need them, so not all modules are covered (far from it
actually). Check the `sage` directory in this project to get the list of modules.

## Contributing

Any help is welcome, if you add types for a module I would gladly merge it to this project.

To add type hints for a module `sage.foo.bar`, you will have to create an empty Python file
`sage/foo/bar.py` (it acts ace a placeholder) and the corresponding Python Interface
file `sage/foo/bar.pyi` containing the type hints.

Here is the recommended structure for the `*.pyi` file:

```python
# -*- coding: utf8 -*-
u"""
Python interface for the `sage.foo.bar` module.

Documentation:
http://doc.sagemath.org/html/en/reference/foo/sage/foo/bar.html

Source:
https://github.com/sagemath/sage/tree/master/src/sage/foo/bar.py
https://github.com/sagemath/sage/tree/master/src/sage/foo/bar.pyx
"""


from typing import ...

import sage.dependency1
import sage.dependency2


# Type hints...
```

Edit the documentation and source links, import the items you need from `typing` and your
dependenvies, then add the actual type hints.

## License

[MIT License, Copyright © 2016 Charles Samborski](./LICENSE.txt)
