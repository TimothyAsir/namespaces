from __future__ import absolute_import, unicode_literals
import collections

class Namespace(collections.MutableMapping):

  RESERVED = frozenset(['_dict'])

  def __init__(self, *args, **kwargs):
    self._dict = dict(*args, **kwargs)

  def __getattr__(self, name):
    if name not in self._dict:
      message = "'{}' object has no attribute '{}'"
      raise AttributeError(message.format(type(self).__name__, name))
    return self._dict[name]

  def __setattr__(self, name, value):
    if name in type(self).RESERVED:
      super(type(self), self).__setattr__(name, value)
    else:
      self._dict[name] = value

  def __getitem__(self, name):
    return self._dict[name]

  def __setitem__(self, name, value):
    self._dict[name] = value

  def __delitem__(self, name):
    del self._dict[name]

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

