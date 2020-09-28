from .models import Picture


def add_picture(title, author):
    return Picture.objects.create(author=author, title=title)


def list_pictures():
    return Picture.objects.all()


def get_picture(title):
    return Picture.objects.get(title=title)


def delete_picture(title):
    Picture.objects.get(title=title).delete()

