"""Models materialized as tables in BigQuery should have clustering defined.

Clustering is a feature in BigQuery that allows you to group your data based
on the contents of one or more columns in the table.
This can help improve query performance, reduce costs, and optimize your data
for analysis.
A table with clustering also optimizes "limit 1" queries, as it can skip scanning.

This opinion checks if models materialized as tables in BigQuery have clustering defined.
"""
