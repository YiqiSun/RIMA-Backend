# Generated by Django 2.2.3 on 2020-06-21 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0018_paper_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='author',
            new_name='authors',
        ),
    ]
