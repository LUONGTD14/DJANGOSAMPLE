# Generated by Django 5.1.6 on 2025-03-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_homePage', models.BooleanField(default=False)),
                ('layout', models.CharField(choices=[('list', 'List'), ('grid', 'Grid')], default='list', max_length=10)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('ordering', models.IntegerField(default=0)),
            ],
        ),
    ]
