# Generated by Django 2.2.3 on 2020-07-26 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0019_auto_20200621_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='original_keyword_name',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]