namespaces API
==============

Namespace
---------

.. autoclass:: namespaces.Namespace
   :members: __getattr__, __setattr__, __getitem__, __setitem__, __delitem__, __iter__, __len__

FrozenNamespace
---------------

.. autoclass:: namespaces.FrozenNamespace
   :members: __getattr__, __hash__, __getitem__, __iter__, __len__

utils
-----

.. automodule:: namespaces.utils
   :members:

Reserved keys
-------------

:py:obj:`Namespace` reserves the key ``_dict``.

:py:obj:`FrozenNamespace` reserves the keys ``_dict`` and ``_hash``.

In general, any and all reserved keys will be prefixed with an ``_``.

.. warning::
   If you override the values for the reserved keys, all bets are off.
