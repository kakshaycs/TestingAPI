# Generated by Django 3.0.7 on 2020-06-11 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20200610_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question_id',
            new_name='question',
        ),
    ]
