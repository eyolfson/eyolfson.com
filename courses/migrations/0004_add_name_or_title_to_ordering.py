# Generated by Django 4.0.3 on 2022-03-09 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_add_constraints'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['offering', 'resource', 'number', 'title']},
        ),
        migrations.AlterModelOptions(
            name='offering',
            options={'ordering': ['-start', 'name']},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'ordering': ['offering', 'kind', 'number', 'title']},
        ),
    ]
