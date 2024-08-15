"""Dbt project must not send anonymous statistics.

Sending anonymous statistics is enabled by default (opt-out).
Although is a good way to help the dbt team improve the product, for privacy
reasons we recommend to disable this feature.

This opinion checks if the `send_anonymous_usage_stats` parameter is set to false
in the `dbt_project.yml` file.
"""
