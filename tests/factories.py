import factory
from faker import Faker
from src.models import TodoItem

fake = Faker()

class TodoFactory(factory.Factory):
    class Meta:
        model = TodoItem

    title = factory.LazyAttribute(lambda x: fake.sentence(nb_words=3))
    completed = False