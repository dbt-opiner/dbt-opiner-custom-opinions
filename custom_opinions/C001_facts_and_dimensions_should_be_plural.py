import re

from dbt_opiner.file_handlers import SqlFileHandler
from dbt_opiner.linter import LintResult
from dbt_opiner.linter import OpinionSeverity
from dbt_opiner.opinions.base_opinion import BaseOpinion
from loguru import logger


class C001(BaseOpinion):
    """Facts and dimensions model names should be plural.

    The name of a fact or a dimension should make the content of the table obvious.
    Using as name a noun in plural form is the best way of doing this.

    For example:
    - fct_user_registration -> each row represents a user registration
    - fct_transactions -> each row represents a transaction
    - fct_item_clicks -> each row represents a click on an item
    - dim_customers -> each row represents a customer
    - dim_products -> each row represents a product

    For verbs like register, add, select, etc. it is better to use a nominalization.
    For example:
      - register -> registrations
      - add -> additions
      - select -> selections

    This opinion checks if the aliases or names of the facts and dimensions models are plural.

    Extra configuration:
    Sometimes when dbt is run in CI all models end up in the same schema.
    By specifying a node alias prefix we can still enforce the naming convention.
    You can specify these under the `extra_opinions_config>C001` key in your `.dbt-opiner.yaml` file.
      - facts_prefix: prefix for fact tables (default: fct_)
      - dimensions_prefix: prefix for dimension tables (default: dim_)
      - facts_schema: schema name for fact tables (default: fact)
      - dimensions_schema: schema name for dimension tables (default: dimension)
    """

    def __init__(self, config: dict = {}, **kwargs):
        super().__init__(
            code="C001",
            description="Facts and dimensions should be plural.",
            severity=OpinionSeverity.SHOULD,
            tags=["naming conventions", "models"],
        )
        self._config = (
            config.get("opinions_config", {})
            .get("extra_opinions_config", {})
            .get("C001", {})
        )

    def _eval(self, file: SqlFileHandler) -> LintResult:
        if file.type != ".sql" or file.dbt_node.type != "model":
            return None

        if file.dbt_node.alias:
            if not self.is_fact_or_dim(file.dbt_node):
                logger.debug("Not a fact or dimension.")
                return None

            if self.is_plural(file.dbt_node.alias):
                return LintResult(
                    file=file,
                    opinion_code=self.code,
                    passed=True,
                    severity=self.severity,
                    message="Facts and dimensions are plural.",
                )

        return LintResult(
            file=file,
            opinion_code=self.code,
            passed=False,
            severity=self.severity,
            message=f"Facts and dimensions {self.severity.value} be plural.",
        )

    def is_fact_or_dim(self, node):
        fact_prefix = self._config.get("facts_prefix", "fct_")
        dimensions_prefix = self._config.get("dimensions_prefix", "dim_")
        fact_schema = self._config.get("facts_schema", "fact")
        dimensions_schema = self._config.get("dimensions_schema", "dimension")

        # Check by schema
        if re.match(rf".*({fact_schema}|{dimensions_schema}).*", node.schema):
            return True
        # Check by alias prefix
        if node.alias.startswith(fact_prefix) or node.alias.startswith(
            dimensions_prefix
        ):
            return True
        return False

    @staticmethod
    def is_plural(word):
        """
        For now use a simple check for s at the end of the word.
        In the future we can use a more sofisiticated check with nltk.
        """
        if word.endswith("s"):
            return True
        return False
