"""Sources must only be used in staging.

Staging models are the entrypoint for raw data in dbt projects, and it is the
only place were we can use the source macro.
See more [here](https://docs.getdbt.com/best-practices/how-we-structure/2-staging)

This opinion checks if the source macro is only used in staging models.

Extra configuration:
Sometimes when dbt is run in CI all models end up in the same schema.
By specifying a node alias prefix we can still enforce this rule.
You can specify these under the `extra_opinions_config>C005` key in your `.dbt-opiner.yaml` file.
 - staging_schema: schema name for staging tables (default: staging)
 - staging_prefix: prefix for staging tables (default: stg_)
"""
