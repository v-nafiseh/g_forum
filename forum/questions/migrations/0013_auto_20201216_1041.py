# Generated by Django 3.1.4 on 2020-12-16 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0012_auto_20201210_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'پاسخ', 'verbose_name_plural': 'پاسخ ها'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'سوال', 'verbose_name_plural': 'سوال ها'},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='date_published',
        ),
        migrations.RemoveField(
            model_name='question',
            name='date_published',
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(verbose_name='محتوا'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question', verbose_name='شناسه سوال'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('published', 'published'), ('draft', 'draft')], max_length=15, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='آراء'),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='محتوا'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.CharField(blank=True, choices=[('published', 'published'), ('draft', 'draft')], max_length=15, null=True, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(null=True, to='questions.Tag', verbose_name='تگ ها'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='question',
            name='votes',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='آراء'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام'),
        ),
    ]
