# Generated by Django 4.0.3 on 2022-04-12 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_add_resource_constraint'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['slug']},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ['slug']},
        ),
        migrations.AlterModelOptions(
            name='offering',
            options={'ordering': ['-start', 'slug']},
        ),
    ]
