# Generated by Django 2.2.6 on 2019-11-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20191118_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=100)),
                ('work_ex', models.CharField(max_length=100)),
                ('progress', models.CharField(max_length=100)),
                ('routes', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='destination',
            name='date',
        ),
    ]
