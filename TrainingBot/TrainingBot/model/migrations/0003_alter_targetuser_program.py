# Generated by Django 4.2.11 on 2024-03-05 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_alter_infouser_ideal_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetuser',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='target', to='model.userprogram'),
        ),
    ]
