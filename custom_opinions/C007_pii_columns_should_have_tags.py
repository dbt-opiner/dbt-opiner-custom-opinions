"""Columns that contain Personal Identifiable Information (PII) should be tagged in the yaml file.

A common practise in data engineering is to tag columns that contain PII.
This allows to easily identify which columns contain sensitive information and
to apply the necessary security measures (e.g. masking, access control, etc.).

This opinion will check the existence in the model of any PII
column name from a list (e.g. ['email', 'phone']) and verify if it is tagged in the yaml file.

In BigQuery is a common practise to tag columns using policy tags instead of regular dbt tags.
Make sure that `policy_tag = True` extra configuration is set if this applies to your case.

Extra configuration:
You can specify these under the `extra_opinions_config>C007` key in your `.dbt-opiner.yaml` file.
  - pii_columns: list of columns that should be tagged as pii (default: [...]).
                 If specified, the opinion will only check for the specified columns
                 and it won't append them to the default list.
  - pii_tags: list of tag(s) to be used for pii columns (default: ['pii']).
              The opinion will check if any of these tags are present in the yaml file.
  - policy_tag: bool (default: false) if true, the opinion will check for
                the presence of a policy tag instead of tags
"""
