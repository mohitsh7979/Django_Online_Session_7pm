# Generated by Django 5.0.6 on 2024-06-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('address', models.TextField(max_length=200)),
                ('mobile_no', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
