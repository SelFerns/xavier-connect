# Generated by Django 4.2.3 on 2024-03-24 09:36
from library.models import Genre
from django.db import migrations

def create_default_genre(apps, schema_editor):
    Genre.objects.get_or_create(genre="Horror")
    Genre.objects.get_or_create(genre="Science Fiction")
    Genre.objects.get_or_create(genre="Fantasy")
    Genre.objects.get_or_create(genre="Mystery")
    Genre.objects.get_or_create(genre="Romance")
    Genre.objects.get_or_create(genre="Thriller")
    Genre.objects.get_or_create(genre="Adventure")
    Genre.objects.get_or_create(genre="Biography")

class Migration(migrations.Migration):
    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_default_genre),
        ]
