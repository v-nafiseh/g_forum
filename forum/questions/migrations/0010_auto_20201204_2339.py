# Generated by Django 3.1.4 on 2020-12-04 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_answer_content'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('title', 'content')},
        ),
    ]
