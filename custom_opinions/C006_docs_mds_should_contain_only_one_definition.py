"""Docs markdown files should contain only one definition.

The `doc` macro is a dbt feature that allows you to re-use documentation.
It is useful for models that share the same columns (e.g. user_id), and ensures consistency
by centralizing the definition of these repeated columns.

However, files containing these definitions can be hard to manage.
To avoid this, we recommend that each markdown file contains only one definition.
This makes it easier to find the documentation for a specific `doc` and keeps the files short.

This opinion checks if each markdown file containing `docs` definitions contains only one.
"""
