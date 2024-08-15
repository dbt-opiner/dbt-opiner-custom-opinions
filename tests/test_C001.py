import pytest
from dbt_opiner.dbt import DbtNode
from custom_opinions.C001_facts_and_dimensions_should_be_plural import C001


@pytest.mark.parametrize(
    "mock_sqlfilehandler, expected_passed",
    [
        pytest.param(
            (
                DbtNode(
                    {
                        "schema": "dimensions",
                        "alias": "dim_customers",
                        "resource_type": "model",
                    }
                )
            ),
            True,
            id="valid_dimension",
        ),
        pytest.param(
            (
                DbtNode(
                    {"schema": "facts", "alias": "fact_sales", "resource_type": "model"}
                )
            ),
            True,
            id="valid_fact",
        ),
        pytest.param(
            (
                DbtNode(
                    {"schema": "facts", "alias": "fact_sale", "resource_type": "model"}
                )
            ),
            False,
            id="invalid_fact_singular",
        ),
        pytest.param(
            (
                DbtNode(
                    {
                        "schema": "dimensions",
                        "alias": "dim_customer",
                        "resource_type": "model",
                    }
                )
            ),
            False,
            id="invalid_dimension_singular",
        ),
        pytest.param(
            (
                DbtNode(
                    {
                        "schema": "staging",
                        "alias": "stg_customer",
                        "resource_type": "model",
                    }
                )
            ),
            True,
            id="valid_staging_singular",
        ),
    ],
    indirect=["mock_sqlfilehandler"],
)
def test_C001(mock_sqlfilehandler, expected_passed):
    opinion = C001()
    result = opinion.check_opinion(mock_sqlfilehandler)
    if result:
        assert result.passed == expected_passed
    else:
        assert expected_passed
