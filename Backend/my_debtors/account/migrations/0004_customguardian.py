# Generated by Django 4.1.4 on 2022-12-11 14:05

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_customuser_date_of_establishment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGuardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('student_name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Guardian',
                'ordering': ['-email'],
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
