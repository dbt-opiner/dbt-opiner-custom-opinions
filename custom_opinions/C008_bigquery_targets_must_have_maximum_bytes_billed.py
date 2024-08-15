"""Bigquery targets used for development and testing must have maximum_bytes_billed
set to prevent unexpected costs.

This opinion checks if the `maximum_bytes_billed` parameter is set in the target.
An optional list of target names to ignore can be specified in the configuration. By default,
it ignores the `prod` and `production` targets. To disable this and check all targets,
set the `ignore_targets` configuration to an empty list.
Also, an optional `max_bytes_billed` parameter can be set to specify the maximum
number of bytes billed allowed. By default, it is not checked.

Extra configuration:
You can specify these under the `extra_opinions_config>C008` key in your `.dbt-opiner.yaml` file.
  - ignore_targets: list of target names to ignore (default: ['prod', 'production'])
  - max_bytes_billed: maximum bytes billed set (optional)
"""
