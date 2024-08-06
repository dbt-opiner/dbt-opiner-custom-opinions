import re
from dbt_opiner.opinions.base_opinion import BaseOpinion
from dbt_opiner.linter import LintResult, OpinionSeverity
from dbt_opiner.file_handlers import SQLFileHandler

class C001(BaseOpinion):
    def __init__(self):
        super().__init__(
            code="C001",
            description="Facts and dimensions should be plural.",
            severity=OpinionSeverity.SHOULD,
            applies_to_file_type=".sql",
            applies_to_node_type="model",
        )

    def _eval(self, file: SQLFileHandler) -> LintResult:
        if file.dbt_node.alias:
          if self.is_fact_or_dim(file.dbt_node.schema):
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
    
    @staticmethod
    def is_plural(word):
      """
      For now use a simple check for s at the end of the word.
      In the future we can use a more sofisiticated check with nltk.
      """
      if word.endswith('s'):
        return True
      return False
    
    @staticmethod
    def is_fact_or_dim(schema):
      if re.match(r'.*(fact|dimension).*', schema):
           return True
      return False
