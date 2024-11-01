from django.db.models import Model, CharField, TextField

class App(Model):
    title = CharField(max_length=100)
    description = TextField()

    def __str__(self):
        return super().__str__()    