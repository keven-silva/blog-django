# Generated by Django 4.1.5 on 2023-01-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_alter_comment_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_publicated',
            field=models.BooleanField(default=False, verbose_name='Publicated'),
        ),
    ]
