# Generated by Django 5.1.1 on 2024-10-29 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usecase', '0003_aktor_fitur_rename_title_usecase_nama_usecase_aktor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usecase',
            name='aktor',
        ),
        migrations.RemoveField(
            model_name='usecase',
            name='fitur',
        ),
        migrations.DeleteModel(
            name='Aktor',
        ),
        migrations.DeleteModel(
            name='Fitur',
        ),
    ]
