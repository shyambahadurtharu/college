# Generated by Django 4.2.4 on 2023-09-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='file_upload',
            field=models.FileField(upload_to='note_upload/'),
        ),
    ]
