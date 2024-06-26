# Generated by Django 4.2.5 on 2023-09-30 12:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proletary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_work', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ведите тип работы (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Описание', max_length=1000)),
                ('isbn', models.CharField(help_text='13 Character <a href="httpsNO LINKSwww.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN')),
                ('Proletary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.proletary')),
                ('View', models.ManyToManyField(help_text='Тип работы', to='catalog.view')),
            ],
        ),
        migrations.CreateModel(
            name='WorkInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID work', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Work availability', max_length=1)),
                ('work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.work')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
    ]
