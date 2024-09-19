"""Yaml files used for model documentation should have only one model.

Although dbt allows to put multiple models inside the same yaml file,
having only one model per yaml file makes it easier to find the documentation
for a specific model and keeps the files short.

This opinion checks if each yaml file containing models contains only one.
"""
