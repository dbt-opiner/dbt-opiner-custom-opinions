"""Views must have partition and cluster of underlying tables documented.

Views that select underlying tables must have a description that explains
the partition and clustering that will impact view usage performance.
Since BigQuery does not show the partition and clustering information for views,
it is important to document this information in the view description in dbt.
"""
