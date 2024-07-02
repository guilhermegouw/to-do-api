import factory
from django.contrib.auth.models import User

from todos.models import Todo


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password123")


class TodoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Todo

    title = factory.Sequence(lambda n: f"Todo {n}")
    body = factory.Faker("text")
