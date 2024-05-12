# Generated by Django 3.2 on 2023-04-08 16:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('calories', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advice', models.TextField(blank=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('answer1', models.IntegerField(blank=True, null=True)),
                ('answer2', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesKey', models.CharField(max_length=50)),
                ('order', models.PositiveIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.TextField(blank=True, null=True)),
                ('last_name', models.TextField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('datetime_start', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserStageGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(blank=True, default=-1, null=True)),
                ('question', models.IntegerField(blank=True, default=1, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stage', to='model.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('start_dci', models.IntegerField(blank=True, default=0, null=True)),
                ('cur_dci', models.IntegerField(blank=True, default=0, null=True)),
                ('phase1', models.IntegerField(blank=True, default=0, null=True)),
                ('phase2', models.IntegerField(blank=True, default=0, null=True)),
                ('cur_day', models.IntegerField(blank=True, default=0, null=True)),
                ('cur_weight', models.FloatField(blank=True, default=0, null=True)),
                ('achievement', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program', to='model.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='model.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='model.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserDayFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('calories', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_food', to='model.user')),
            ],
        ),
        migrations.CreateModel(
            name='TargetUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True, default='None', null=True)),
                ('activity', models.TextField(blank=True, default='None', null=True)),
                ('dci', models.IntegerField(blank=True, default=0, null=True)),
                ('cur_dci', models.IntegerField(blank=True, default=0, null=True)),
                ('cur_weight', models.FloatField(blank=True, default=0, null=True)),
                ('target_weight', models.FloatField(blank=True, default=0, null=True)),
                ('percentage_decrease', models.IntegerField(default=15)),
                ('achieved', models.BooleanField(default=False)),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='model.userprogram')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='model.user')),
            ],
        ),
        migrations.CreateModel(
            name='ResultDayDci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('calories', models.IntegerField(default=0)),
                ('deficit', models.IntegerField(blank=True, null=True)),
                ('cur_weight', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_day_dci', to='model.user')),
            ],
        ),
        migrations.CreateModel(
            name='RemindUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remind_first', models.BooleanField(default=True)),
                ('remind_second', models.BooleanField(default=True)),
                ('day_without_indication_weight', models.PositiveIntegerField(default=1)),
                ('remind_weight', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remind', to='model.user')),
            ],
        ),
        migrations.CreateModel(
            name='InfoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('height', models.IntegerField(blank=True, default=0, null=True)),
                ('gender', models.TextField(blank=True, default='None', null=True)),
                ('ideal_weight', models.TextField(blank=True, default=0, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='model.user')),
            ],
        ),
    ]