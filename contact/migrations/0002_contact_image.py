# Generated by Django 4.2.13 on 2024-06-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(null=True, upload_to='contact/image'),
        ),
    ]