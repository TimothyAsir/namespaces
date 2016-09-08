> Namespaces are one honking great idea -- let's do more of those!
- [PEP 20: The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

## Install

```bash
$ pip install namespaces
```

## API
`Namespace` is a flexible, mutable version of [`collections.namedtuple`](https://docs.python.org/2/library/collections.html#collections.namedtuple). You can also think about it as a dictionary that uses dot-notation access instead of bracket-notation access (ie. `ns.attr` instead of `ns['attr']`).

The API of `Namespace` is as follows:
```python
import namespaces as ns
ns = ns.Namespace(a=1, b=2)
fns = ns.FrozenNamespace(ns)
fns.b # => 2
ns.c # => AttributeError
ns.c = 3
ns.c # => 3
fns.c = 3 # => AttributeError
```

`FrozenNamespace` is an immutable, hashable `Namespace`. The hash is lazily computed and is cached for performance.

## Tests

### unittest

```bash
$ python setup.py test
```

