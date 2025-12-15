.. _api.iterable_dataset:

================
IterableDataset
================

.. currentmodule:: datasets

Constructor
-----------

.. autosummary::
   :toctree: generated/

   IterableDataset
   IterableDataset.from_generator

Attributes
----------

.. autosummary::
   :toctree: generated/

   IterableDataset.n_shards

Data processing
---------------

.. autosummary::
   :toctree: generated/

   IterableDataset.map
   IterableDataset.filter
   IterableDataset.shuffle
   IterableDataset.skip
   IterableDataset.take
   IterableDataset.with_format

Iteration
---------

.. autosummary::
   :toctree: generated/

   IterableDataset.__iter__
   IterableDataset.iter

Column operations
-----------------

.. autosummary::
   :toctree: generated/

   IterableDataset.add_column
   IterableDataset.remove_columns
   IterableDataset.rename_column
   IterableDataset.rename_columns
   IterableDataset.select_columns
   IterableDataset.cast
   IterableDataset.cast_column
