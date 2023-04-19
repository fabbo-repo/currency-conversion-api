# Generated by Django 4.1.7 on 2023-04-16 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currency',
                'ordering': ['code'],
            },
        ),
    ]