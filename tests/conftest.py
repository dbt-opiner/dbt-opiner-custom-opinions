from unittest.mock import patch

import pytest


@pytest.fixture
def mock_sqlfilehandler():
    with patch("dbt_opiner.file_handlers.SqlFileHandler") as MockClass:
        MockClass.type = ".sql"
        yield MockClass


@pytest.fixture
def mock_yamlfilehandler():
    with patch("dbt_opiner.file_handlers.YamlFileHandler") as MockClass:
        MockClass.type = ".yaml"
        yield MockClass
