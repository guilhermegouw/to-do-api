import pytest
from django.urls import reverse

from todos.tests.factories import TodoFactory


@pytest.mark.django_db
def test_todo_list_view(client):
    TodoFactory.create_batch(5)
    response = client.get(reverse("todo_list"))
    assert response.status_code == 200
    assert len(response.json()) == 5


@pytest.mark.django_db
def test_todo_detail_view(client):
    todo = TodoFactory()
    response = client.get(reverse("todo_detail", kwargs={"pk": todo.id}))
    assert response.status_code == 200
    assert response.json()["title"] == todo.title
