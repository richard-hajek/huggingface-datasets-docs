.. _api.dataset:

=======
Dataset
=======

.. currentmodule:: datasets

Constructor
-----------

.. autosummary::
   :toctree: generated/

   Dataset
   Dataset.from_file
   Dataset.from_buffer
   Dataset.from_pandas
   Dataset.from_dict
   Dataset.from_generator

Attributes and underlying data
-------------------------------

.. autosummary::
   :toctree: generated/

   Dataset.data
   Dataset.cache_files
   Dataset.num_columns
   Dataset.num_rows
   Dataset.column_names
   Dataset.shape
   Dataset.info
   Dataset.split
   Dataset.builder_name
   Dataset.citation
   Dataset.config_name
   Dataset.dataset_name
   Dataset.description
   Dataset.download_checksums
   Dataset.download_size
   Dataset.features
   Dataset.homepage
   Dataset.license
   Dataset.size_in_bytes
   Dataset.supervised_keys
   Dataset.task_templates
   Dataset.version

Reshaping, reorganizing
------------------------

.. autosummary::
   :toctree: generated/

   Dataset.flatten
   Dataset.unflatten
   Dataset.cast
   Dataset.cast_column
   Dataset.add_column
   Dataset.remove_columns
   Dataset.rename_column
   Dataset.rename_columns
   Dataset.select_columns
   Dataset.class_encode_column

Sorting, selecting, filtering
------------------------------

.. autosummary::
   :toctree: generated/

   Dataset.sort
   Dataset.shuffle
   Dataset.select
   Dataset.filter
   Dataset.unique
   Dataset.train_test_split
   Dataset.shard

Data processing
---------------

.. autosummary::
   :toctree: generated/

   Dataset.map
   Dataset.batch
   Dataset.with_format
   Dataset.with_transform
   Dataset.set_format
   Dataset.set_transform
   Dataset.reset_format
   Dataset.formatted_as

Indexing, iteration
--------------------

.. autosummary::
   :toctree: generated/

   Dataset.__len__
   Dataset.__iter__
   Dataset.iter
   Dataset.__getitem__

Serialization / IO / conversion
--------------------------------

.. autosummary::
   :toctree: generated/

   Dataset.save_to_disk
   Dataset.load_from_disk
   Dataset.to_csv
   Dataset.to_pandas
   Dataset.to_dict
   Dataset.to_json
   Dataset.to_parquet
   Dataset.to_sql
   Dataset.to_iterable_dataset
   Dataset.push_to_hub
   Dataset.prepare_for_task

Caching
-------

.. autosummary::
   :toctree: generated/

   Dataset.cleanup_cache_files

Indexing
--------

.. autosummary::
   :toctree: generated/

   Dataset.add_faiss_index
   Dataset.add_faiss_index_from_external_arrays
   Dataset.save_faiss_index
   Dataset.load_faiss_index
   Dataset.add_elasticsearch_index
   Dataset.load_elasticsearch_index
   Dataset.list_indexes
   Dataset.get_index
   Dataset.drop_index
   Dataset.search
   Dataset.search_batch
   Dataset.get_nearest_examples
   Dataset.get_nearest_examples_batch

Metadata
--------

.. autosummary::
   :toctree: generated/

   Dataset.align_labels_with_mapping
