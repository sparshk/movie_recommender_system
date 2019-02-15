# Generated by Django 2.0.6 on 2019-02-15 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=100)),
                ('imdb_url', models.CharField(max_length=100)),
                ('img_url', models.CharField(max_length=500)),
                ('movie_id', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('users_rating', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'movies',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(null=True)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('account', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rating',
                'managed': True,
            },
        ),
    ]
