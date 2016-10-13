from __future__ import absolute_import, unicode_literals
import collections
from six import iteritems

class FrozenNamespace(collections.Mapping):
  '''Immutable, hashable dictionary whose items are also available via dot-notation.'''

  RESERVED = frozenset(['_dict', '_hash'])

  def __init__(self, *args, **kwargs):
    self._dict = dict(*args, **kwargs)
    self._hash = None

  def __getattr__(self, name):
    '''Look up item via dot-notation.

    :param str name: Key
    :return: Associated value

    Usage::
      >>> import namespaces as ns
      >>> foo = ns.FrozenNamespace(a=1)
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
    '''Disable setting items via dot-notation to protect against accidental mutations.'''
    if name in FrozenNamespace.RESERVED:
      super(self.__class__, self).__setattr__(name, value)
    else:
      message = "'{}' object has no attribute '{}'"
      raise AttributeError(message.format(type(self).__name__, name))

  def __repr__(self):
    '''Representation is a valid python expression for creating a FrozenNamespace
    (assuming contents also implement __repr__ as valid python expressions).'''
    items = ('{}={}'.format(k,repr(v)) for k,v in sorted(iteritems(self)))
    return '{}({})'.format(type(self).__name__, ', '.join(items))

  def __hash__(self):
    '''Caches lazily-evaluated hash for performance.

    :return: Hash value for this FrozenNamespace
    :rtype: int

    Usage::
      >>> import namespaces as ns
      >>> foo = ns.FrozenNamespace(a=1)
      >>> hash(foo) # calls foo.__hash__()
      -2550060783245333914
    '''
    if self._hash is None:
      self._hash = hash(frozenset(iteritems(self)))
    return self._hash

  # dict pass-through
  ###################

  def __getitem__(self, name):
    '''Get item via bracket-notation.

    :param str name: Key
    :return: Corresponding value

    Usage::
      >>> import namespaces as ns
      >>> foo = ns.FrozenNamespace(a=1)
      >>> foo['a'] # calls foo.__getitem__('a')
      1
    '''
    return self._dict[name]

  def __iter__(self):
    '''Iterator over item keys.

    :return: Key iterator
    :rtype: collections.KeysView

    Usage::

      >>> import namespaces as ns
      >>> foo = ns.FrozenNamespace(a=1, b=2, c=3)
      >>> for key in foo: # calls foo.__iter__()
      ...     print(key)
      a
      b
      c
    '''
    return iter(self._dict)

  def __len__(self):
    '''Calculates length of this FrozenNamespace

    :return: Length of this FrozenNamespace
    :rtype: int

    Usage::

      >>> import namespaces as ns
      >>> foo = ns.FrozenNamespace(a=1, b=2, c=3)
      >>> len(foo) # calls foo.__len__()
      3
    '''
    return len(self._dict)

