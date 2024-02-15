# Generated by Django 4.1 on 2022-08-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
