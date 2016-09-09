[![PyPI version](https://badge.fury.io/py/namespaces.svg)](https://badge.fury.io/py/namespaces)
[![Build Status](https://travis-ci.org/pcattori/namespaces.svg?branch=master)](https://travis-ci.org/pcattori/namespaces)
[![Test Code Coverage](https://codecov.io/gh/pcattori/namespaces/branch/master/graph/badge.svg)](https://codecov.io/gh/pcattori/namespaces)
[![Documentation Status](https://readthedocs.org/projects/namespaces/badge/?version=latest)](http://namespaces.readthedocs.io/en/latest/?badge=latest)

> Namespaces are one honking great idea -- let's do more of those!
- [PEP 20: The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

## Install

```bash
$ pip install namespaces
```

## API
`Namespace` is like a flexible, mutable version of [`collections.namedtuple`](https://docs.python.org/2/library/collections.html#collections.namedtuple). You can also think about it as a dictionary whose items are also accessible via dot-notation (ie. `ns.attr` is equivalent to `ns['attr']`).

The API of `Namespace` is as follows:
```python
import namespaces as ns
ab = ns.Namespace(a=1, b=2)
frozen_ab = ns.FrozenNamespace(ab)
frozen_ab.b # => 2
ab.c # => AttributeError
ab.c = 3
ab.c # => 3
frozen_ab.c = 3 # => AttributeError
```

`FrozenNamespace` is an immutable, hashable `Namespace`. The hash is lazily computed and is cached for performance.

## Tests

### unittest

```bash
$ python setup.py test
```

