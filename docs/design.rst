Design
======

The goal of `namespaces` is to improve code readability by leveraging
*beautiful* dot-notation instead of relying on :py:obj:`str` when describing
object attributes.

`namespaces` was born out of a desire for a mutable :py:obj:`namedtuple`.

Before & after
--------------

Before:

.. code-block:: python

   joey = {'name': 'joey', 'height': 70, 'age': 24}
   joey['species'] = 'kangaroo'
   print(joey['name'], 'is a', joey['species'])

After:

.. code-block:: python

   import namespaces as ns
   joey = ns.Namespace(name='joey', height=70, age=24)
   joey.species = 'kangaroo'
   print(joey.name, 'is a', joey.species)

namespaces vs dict
------------------

Namespaces is **not** meant as a replacement for `dict`.

Use a namespace if:

* you will be accessing items individually by name
* you can enumerate and name items as you write your code
* you want the semantics of a Javascript object
* you want a dynamic, mutable :py:obj:`namedtuple`

Use a :py:obj:`dict` if:

* you will be accessing items in batches programmatically
* you *cannot* enumerate or name items as you write your code
* you need keys that are not :py:obj:`str`

