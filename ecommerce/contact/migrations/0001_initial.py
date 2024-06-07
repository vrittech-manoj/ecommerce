# Generated by Django 4.2.13 on 2024-06-07 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=323)),
                ('email', models.EmailField(max_length=23)),
                ('message', models.TextField()),
            ],
        ),
    ]