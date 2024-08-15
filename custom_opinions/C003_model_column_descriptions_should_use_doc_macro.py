"""Model column descriptions should use the `docs` macro.

The `doc` macro is a dbt feature that allows you to re-use documentation.
It is useful for models that share the same columns (e.g. user_id),
and ensures consistency by centralizing the definition of these repeated columns.
Sharing these definitions also encourages better column naming,
for example `user_id` instead of `id`.

This opinion checks if all the columns descriptions in the model are
defined using the `doc` macro.
"""
