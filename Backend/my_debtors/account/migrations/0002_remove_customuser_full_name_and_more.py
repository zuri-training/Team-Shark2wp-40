# Generated by Django 4.1.4 on 2022-12-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='sch_image',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='unique_number',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cac',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_establishment',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='school_name',
            field=models.CharField(max_length=250),
        ),
    ]