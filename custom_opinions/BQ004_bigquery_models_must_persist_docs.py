"""The persist_docs option for models must be enabled.

The persist_docs option for models must be enabled to ensure that the documentation
is shown in the BigQuery console.

Add
```yaml
models:
  +persist_docs:
    relation: true
    columns: true
```
To your dbt_project.yml file to enable this option.
"""
