# Generated by Django 2.2.3 on 2020-04-18 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [('interests', '0008_auto_20200415_2157')]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_on',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='keyword',
            name='created_on',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='keyword',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
