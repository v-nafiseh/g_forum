# Generated by Django 3.1.4 on 2020-12-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20201204_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
