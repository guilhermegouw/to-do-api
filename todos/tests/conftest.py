import pytest

from todos.tests.factories import TodoFactory


@pytest.fixture
def one_todo():
    return TodoFactory()
