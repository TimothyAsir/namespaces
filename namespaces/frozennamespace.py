from __future__ import absolute_import, unicode_literals
import collections

class FrozenNamespace(collections.Mapping):

  RESERVED = frozenset(['_dict', '_hash'])

  def __init__(self, *args, **kwargs):
    self._dict = dict(*args, **kwargs)
    self._hash = None

  def __getattr__(self, name):
    if name not in self._dict:
      message = "'{}' object has no attribute '{}'"
      raise AttributeError(message.format(type(self).__name__, name))
    return self._dict[name]

  def __setattr__(self, name, value):
    if name in FrozenNamespace.RESERVED:
      super(self.__class__, self).__setattr__(name, value)
    else:
      message = "'{}' object has no attribute '{}'"
      raise AttributeError(message.format(type(self).__name__, name))

  def __getitem__(self, name):
    return self._dict[name]

  def __iter__(self):
    return iter(self._dict)

  def __len__(self):
    return len(self._dict)

  def __repr__(self):
    '''Representation is a valid python expression for creating a Namespace
    (assuming contents also implement __repr__ as valid python expressions).'''
    items = ('{}={}'.format(k,repr(v)) for k,v in self.iteritems())
    return '{}({})'.format(type(self).__name__, ', '.join(items))

  def __eq__(self, other):
    return isinstance(other, type(self)) and super(type(self), self).__eq__(other)

  def __ne__(self, other):
    return not self == other

  def __hash__(self):
    if self._hash is None:
      self._hash = hash(frozenset(self._dict.iteritems()))
    return self._hash

