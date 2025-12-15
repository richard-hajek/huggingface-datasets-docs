.. _api.dataset_dict:

===========
DatasetDict
===========

.. currentmodule:: datasets

Constructor
-----------

.. autosummary::
   :toctree: generated/

   DatasetDict
   DatasetDict.from_csv
   DatasetDict.from_json
   DatasetDict.from_parquet
   DatasetDict.from_text

Attributes
----------

.. autosummary::
   :toctree: generated/

   DatasetDict.data
   DatasetDict.cache_files
   DatasetDict.num_columns
   DatasetDict.num_rows
   DatasetDict.column_names
   DatasetDict.shape

Data processing
---------------

.. autosummary::
   :toctree: generated/

   DatasetDict.map
   DatasetDict.filter
   DatasetDict.sort
   DatasetDict.shuffle
   DatasetDict.set_format
   DatasetDict.reset_format
   DatasetDict.set_transform
   DatasetDict.with_format
   DatasetDict.with_transform
   DatasetDict.flatten
   DatasetDict.cast
   DatasetDict.cast_column
   DatasetDict.remove_columns
   DatasetDict.rename_column
   DatasetDict.rename_columns
   DatasetDict.select_columns
   DatasetDict.class_encode_column

Serialization / IO
------------------

.. autosummary::
   :toctree: generated/

   DatasetDict.save_to_disk
   DatasetDict.load_from_disk
   DatasetDict.push_to_hub
   DatasetDict.prepare_for_task

Caching
-------

.. autosummary::
   :toctree: generated/

   DatasetDict.cleanup_cache_files

Metadata
--------

.. autosummary::
   :toctree: generated/

   DatasetDict.align_labels_with_mapping
