import pytest
from unittest.mock import create_autospec
from dbt_opiner.file_handlers import SQLFileHandler
from dbt_opiner.linter import LintResult, OpinionSeverity
from dbt_opiner.dbt_artifacts import DbtNode
from custom_opinions.C001_facts_and_dimensions_should_be_plural import C001


@pytest.fixture
def mock_sqlfilehandler(request):
    schema, alias, resource_type, expected_passed = request.param
    mock_handler = create_autospec(SQLFileHandler)
    mock_handler.file_type = ".sql"
    mock_handler.dbt_node = DbtNode({
        'schema': schema,
        'alias': alias,
        'resource_type': resource_type
    })
    return mock_handler, expected_passed


@pytest.mark.parametrize('mock_sqlfilehandler, expected_passed', [
    pytest.param(('dimensions', 'dim_customers', 'model', True), True, id='valid_dimension'),
    pytest.param(('facts', 'fact_sales', 'model', True), True, id='valid_fact'),
    pytest.param(('facts', 'fact_sale', 'model', False), False, id='invalid_fact_singular'),
    pytest.param(('dimensions', 'dim_customer', 'model', False), False, id='invalid_dimension_singular'),
], indirect=['mock_sqlfilehandler'])
def test_C001(mock_sqlfilehandler, expected_passed):
    mock_handler, expected_passed = mock_sqlfilehandler
    opinion = C001()
    result = opinion.check_opinion(mock_handler)
    assert result.passed == expected_passed

"""
@pytest.fixture
def mock_sqlfilehandler():
    mock_handler = create_autospec(SQLFileHandler)
    mock_handler.file_type = ".sql"
    mock_handler.dbt_node = DbtNode(
       {'database': 'customers', 'schema': 'main_dimensions', 'name': 'dim_customers', 'resource_type': 'model'}
    )
    return mock_handler

def test_C001(mock_sqlfilehandler):
    opinion = C001()
    result = opinion.check_opinion(mock_sqlfilehandler)
    assert result == LintResult(
        file=mock_sqlfilehandler,
        opinion_code="C001",
        passed=False,
        severity=OpinionSeverity.SHOULD,
        message=f"Facts and dimensions {OpinionSeverity.SHOULD.value} be plural.",
    )
"""