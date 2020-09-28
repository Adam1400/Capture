from .models import Author


def add_author(user, name):
    return Author.objects.create(user=user, name=name)



def get_author(name):
    return Author.objects.get(name=name)


def delete_author(name):
    Author.objects.get(name=name).delete()


def list_authors():
    return Author.objects.all()


