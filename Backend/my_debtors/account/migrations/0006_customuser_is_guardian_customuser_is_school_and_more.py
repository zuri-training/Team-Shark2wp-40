# Generated by Django 4.1.4 on 2022-12-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_delete_customguardian_customuser_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_guardian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_school',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cac',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='school_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='student_name',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
