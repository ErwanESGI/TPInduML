"""
This module contains an example test.

Tests should be placed in src/tests, in modules that mirror your
project's structure, and in files named test*.py. They are simply functions
named ``test* which test a unit of logic.

To run the tests, run kedro test`` from the project root directory.
"""

from pathlib import Path

import pytest

from kedro.framework.project import settings
from kedro.config import ConfigLoader
from kedro.framework.context import KedroContext
from kedro.framework.hooks import _create_hook_manager


@pytest.fixture
def config_loader():
    return ConfigLoader(conf_source=str(Path.cwd() / settings.CONF_SOURCE))


@pytest.fixture
def project_context(config_loader):
    return KedroContext(
        package_name="projet",
        project_path=Path.cwd(),
        config_loader=config_loader,
        hook_manager=_create_hook_manager(),
    )


class TestProjectContext:
    def test_project_path(self, project_context):
        assert project_context.project_path == Path.cwd()