# Generated by Django 4.1.7 on 2023-06-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=100)),
                ('image_file', models.FileField(upload_to='image/')),
            ],
        ),
    ]