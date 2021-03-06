# Generated by Django 3.1.4 on 2020-12-05 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20201204_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='category',
            new_name='categories',
        ),
        migrations.AddField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('published', 'published'), ('draft', 'draft')], default='c++', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question'),
        ),
    ]
