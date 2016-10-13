namespaces
==========

   Namespaces are one honking great idea -- let's do more of those!

   -- `PEP 20: The Zen of Python <https://www.python.org/dev/peps/pep-0020/>`_

Namespaces are:

* Pythonic structs
* Python `dict` with dot-notation access
* Javascript-like objects for Python


Basic Usage
^^^^^^^^^^^

.. code-block:: python

   import namespaces as ns
   ab = ns.Namespace(a=1, b=2)
   frozen_ab = ns.FrozenNamespace(ab)
   frozen_ab.b # => 2
   ab.c # => AttributeError
   ab.c = 3
   ab.c # => 3
   frozen_ab.c = 3 # => AttributeError

Installation
^^^^^^^^^^^^

.. code-block:: bash

    $ pip install namespaces

Navigation
^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   design
   faq
   api
   support
   contribute
   license

