import pytest

from todos.models import Todo


@pytest.mark.django_db
def test_todo_model():
    todo = Todo.objects.create(title="Test Todo", body="Test Todo Body")
    assert todo.title == "Test Todo"
    assert todo.body == "Test Todo Body"
    assert str(todo) == "Test Todo"
