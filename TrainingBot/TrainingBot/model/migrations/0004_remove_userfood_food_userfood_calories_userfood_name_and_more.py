# Generated by Django 4.2.11 on 2024-03-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_alter_targetuser_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfood',
            name='food',
        ),
        migrations.AddField(
            model_name='userfood',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userfood',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]
