import json
from namespaces import FrozenNamespace, Namespace, NamespaceEncoder
import unittest


class FrozenNamespaceTest(unittest.TestCase):

  def test_create_empty(self):
    fn = FrozenNamespace()
    self.assertIsInstance(fn, FrozenNamespace)
    self.assertEqual(len(fn), 0)

  def test_create_via_kwargs(self): # anonymous mapping
    fn = FrozenNamespace(a=1, b=2)
    self.assertIsInstance(fn, FrozenNamespace)
    self.assertEqual(fn.items(), {'a': 1, 'b': 2}.items())

  def test_create_via_dict(self): # named mapping
    d = {'a': 1, 'b': 2, tuple('three'): 3, 4: 4}
    fn = FrozenNamespace(d)
    self.assertIsInstance(fn, FrozenNamespace)
    self.assertEqual(fn.items(), d.items())

  def test_create_via_namespace(self):
    ns = Namespace(a=1, b=2)
    fn = FrozenNamespace(ns)
    self.assertIsInstance(fn, FrozenNamespace)
    self.assertEqual(ns.items(), fn.items())

  def test_item_get(self):
    fn = FrozenNamespace(a=1, b=2)
    self.assertEqual(fn['a'], 1)

  def test_item_set(self):
    fn = FrozenNamespace()
    with self.assertRaises(TypeError) as context:
      fn['c'] = 3
    message = "'FrozenNamespace' object does not support item assignment"
    self.assertEqual(message, context.exception.message)

  def test_attr_get(self):
    fn = FrozenNamespace(a=1, b=2)
    self.assertEqual(fn.a, 1)

  def test_attr_set(self):
    fn = FrozenNamespace()
    with self.assertRaises(AttributeError) as context:
      fn.c = 3
    message = "'FrozenNamespace' object has no attribute 'c'"
    self.assertEqual(message, context.exception.message)

  def test_len(self):
    fn = FrozenNamespace(a=1, b=2)
    self.assertEqual(len(fn), 2)

  def test_iter(self):
    fn = FrozenNamespace(a=1, b=2)
    d = {k: v for k,v in fn.iteritems()}
    self.assertEqual(d, {'a': 1, 'b': 2})

  def test_del(self):
    fn = FrozenNamespace(a=1, b=2)
    with self.assertRaises(TypeError) as context:
      del fn['a']
    message = "'FrozenNamespace' object does not support item deletion"
    self.assertEqual(message, context.exception.message)

  def test_hashable(self):
    fn = FrozenNamespace(a=1, b=2)
    self.assertIsInstance(hash(fn), int)

  def test_json(self):
    d = {'a': 1, 'b': 2}
    fn = FrozenNamespace(d)
    self.assertEqual(json.dumps(d), json.dumps(fn, cls=NamespaceEncoder))

if __name__ == '__main__':
  unittest.main()
