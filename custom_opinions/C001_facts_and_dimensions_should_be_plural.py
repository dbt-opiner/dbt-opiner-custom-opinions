import re
from dbt_opiner.opinions.base_opinion import BaseOpinion
from dbt_opiner.linter import LintResult, OpinionSeverity
from dbt_opiner.file_handlers import SQLFileHandler


class C001(BaseOpinion):
    required_packages = ["numpy==2.0.1"] # TODO: For testing purposes. Remove
    def __init__(self, **kwargs):
        super().__init__(
            code="C001",
            description="Facts and dimensions should be plural.",
            severity=OpinionSeverity.SHOULD,
        )

    def _eval(self, file: SQLFileHandler) -> LintResult:
        # Check type of file and model.
        if file.type != ".sql" or file.dbt_node.type != "model":
            return None
        
        # TODO: remove
        import numpy as np
        t = np.array([1, 2, 3])
        
        if file.dbt_node.alias:
            if self.is_fact_or_dim(file.dbt_node.schema) and self.is_plural(
                file.dbt_node.alias
            ):
                return LintResult(
                    file=file,
                    opinion_code=self.code,
                    passed=True,
                    severity=self.severity,
                    message="Facts and dimensions are plural.",
                )
            if not self.is_fact_or_dim(file.dbt_node.schema):
                return LintResult(
                    file=file,
                    opinion_code=self.code,
                    passed=True,
                    severity=self.severity,
                    message="Not a fact or dimension.",
                )

        return LintResult(
            file=file,
            opinion_code=self.code,
            passed=False,
            severity=self.severity,
            message=f"Facts and dimensions {self.severity.value} be plural.",
        )

    @staticmethod
    def is_plural(word):
        """
        For now use a simple check for s at the end of the word.
        In the future we can use a more sofisiticated check with nltk.
        """
        if word.endswith("s"):
            return True
        return False

    @staticmethod
    def is_fact_or_dim(schema):
        if re.match(r".*(fact|dimension).*", schema):
            return True
        return False
