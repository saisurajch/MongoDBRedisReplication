# API Reference

## `main.py`

### Functions

#### `write_to_mongo(collection_name, key, value)`

Writes or updates a document in the specified MongoDB collection based on the given key and value. If the value is `None`, the document is deleted from the collection.

- **Parameters:**
  - `collection_name` (str): The name of the MongoDB collection.
  - `key` (str): The key (or document `_id`) for the MongoDB document.
  - `value` (dict or None): The value to write to MongoDB. If `None`, the document is deleted.

- **Usage:**
  ```python
  write_to_mongo('my_collection', 'document_id', {'field': 'value'})
