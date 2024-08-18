"""The layer directionality must be respected.

Maintaining a good lineage crucial for any dbt project, and
layer directionality is a key part of it.
If the layer directionality is not respected, it can lead to
circular dependencies and make the data model harder to understand and to schedule.

This opinion checks if the layer directionality is respected.

For example:
 - layer `stg` should not select from a layer `fct` or `mrt`.
 - layer `fct` should not select from a layer `mrt`.
 - layer `mrt` should not select from a layer `stg`.

This rule requires extra configuration that state the forbidden layer pairs.
You can specify these under the `extra_opinions_config>C009` key in your `.dbt-opiner.yaml` file.
  - layer_pairs: #list of forbidden layer pairs
     - "staging,stg selects from facts,fct"
     - "staging,stg selects from marts,mrt"
     - "facts,fct selects from marts,mrt"
     ... etc.
The first value is the schema layer name and the second the prefix.
If in CI run all models end up in the same schema a check by prefixes is used in that case.
You can omit the prefix if it's not the case.
"""
