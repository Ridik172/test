# Generated by Django 4.2.5 on 2023-10-04 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set work as returned'),)},
        ),
    ]
