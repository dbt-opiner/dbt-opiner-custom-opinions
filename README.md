# dbt-opiner-custom-opinions
Custom opinions for dbt-opiner tool.

## Usage
Add this repository as a custom opinion source in `.dbt-opiner.yaml`file.

```yaml
opinions_config:
  custom_opinions:
    source: git
    repository: https://github.com/dbt-opiner/dbt-opiner-custom-opinions.git
    rev: 0.1.0
```
