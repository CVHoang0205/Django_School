# Generated by Django 4.1.7 on 2023-03-22 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class_room', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class_room',
            name='Student',
        ),
        migrations.AddField(
            model_name='class_room',
            name='Teacher_Course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='class_room.teacher'),
        ),
    ]
