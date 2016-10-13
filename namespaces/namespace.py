from __future__ import absolute_import, unicode_literals
import collections
from six import iteritems

class Namespace(collections.MutableMapping):
  '''Pythonic structs | Python `dict` with dot-notation access |
  Javascript-like objects for Python.

  Creation is equivalent to creating a :py:obj:`dict` with the positional
  arguments `args` and keyword arguments `kwargs`. In other words, if it works
  for the :py:obj:`dict` constructor, it will work for the :py:obj:`Namespace`
  constructor.

  :param args: Items as positional arguments.
  :param kwargs: Items as keyword arguments.

  Usage::

    >>> import namespaces as ns
    >>> foo = ns.Namespace(a=1, b=2, c=3)
    >>> foo
    Namespace(a=1, b=2, c=3)
    >>> bar = ns.Namespace({'a': 1, 'b': 2, 'c': 3})
    >>> bar
    Namespace(a=1, b=2, c=3)
    >>> baz = ns.Namespace()
    >>> baz.a = 1
    >>> baz.a
    1
    >>> baz['a']
    1
    >>> baz.a is baz['a']
    True
    >>> baz['b'] = 2
    >>> baz['b']
    2
    >>> baz.b
    2
    >>> baz['b'] is baz.b
    True
  '''

  RESERVED = frozenset(['_dict'])

  def __init__(self, *args, **kwargs):
    self._dict = dict(*args, **kwargs)

  def __getattr__(self, name):
    '''Look up item via dot-notation.

    :param str name: Key
    :return: Associated value

    Usage::

      >>> import namespaces as ns
      >>> foo = ns.Namespace(a=1)
      >>> foo.a # calls foo.__getattr__('a')
      1
      >>> foo.b
      AttributeError: 'Namespace' object has no attribute 'b'
    '''
    if name not in self._dict:
      message = "'{}' object has no attribute '{}'"
      raise AttributeError(message.format(type(self).__name__, name))
    return self._dict[name]

  def __setattr__(self, name, value):
    '''Set item via dot-notation.

    :param str name: Key
    :param value: New associated value

    Usage::

      >>> import namespaces as ns
      >>> foo = ns.Namespace()
      >>> foo.a = 1 # calls foo.__setattr__('a', 1)
      >>> foo
      Namespace(a=1)
    '''
    if name in type(self).RESERVED:
      super(type(self), self).__setattr__(name, value)
    else:
      self._dict[name] = value

  def __repr__(self):
    '''Representation is a valid python expression for creating a Namespace
    (assuming contents also implement __repr__ as valid python expressions).'''
    items = ('{}={}'.format(k,repr(v)) for k,v in sorted(iteritems(self)))
    return '{}({})'.format(type(self).__name__, ', '.join(items))

  # dict pass-through
  ###################

  def __getitem__(self, name):
    '''Get item via bracket-notation.

    :param str name: Key
    :return: Associated value

    Usage::

      >>> import namespaces as ns
      >>> foo = ns.Namespace(a=1)
      >>> foo['a'] # calls foo.__getitem__('a')
      1
    '''
    return self._dict[name]

  def __setitem__(self, name, value):
    '''Set item via bracket-notation.

    :param str name: Key
    :param value: New associated value

    Usage::

      >>> import namespaces as ns
      >>> foo = ns.Namespace()
      >>> foo['a'] = 1 # calls foo.__setitem__('a', 1)
      >>> foo
      Namespace(a=1)
    '''
    self._dict[name] = value

  def __delitem__(self, name):
    '''Delete item via bracket-notation.

    :param str name: Key

    Usage::

      >>> import namespaces as ns
      >>> foo = ns.Namespace(a=1)
      >>> del foo['a'] # calls foo.__delitem__('a')
      >>> foo
      Namespace()
    '''
    del self._dict[name]

  def __iter__(self):
    '''Iterator over keys.

    :return: Key iterator

    Usage::

      >>> import namespaces as ns
      >>> foo = ns.Namespace(a=1, b=2, c=3)
      >>> for key in foo: # calls foo.__iter__()
      >>>   print(key)
      a
      b
      c
    '''
    return iter(self._dict)

  def __len__(self):
    '''Calculates length.

    :return: Length of Namespace
    :rtype: int

    Usage::

      >>> import namespaces as ns
      >>> foo = ns.Namespace(a=1, b=2, c=3)
      >>> len(foo)
      3
    '''
    return len(self._dict)

