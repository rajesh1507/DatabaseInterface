# Generated by Django 3.1.1 on 2020-09-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0003_auto_20200620_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siteinventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.IntegerField()),
                ('model', models.CharField(max_length=100)),
                ('client', models.CharField(max_length=100)),
                ('scantype1', models.CharField(max_length=100)),
                ('scannum1', models.CharField(max_length=100)),
                ('scantype2', models.CharField(max_length=100)),
                ('scannum2', models.CharField(max_length=100)),
                ('scantype3', models.CharField(max_length=100)),
                ('scannum3', models.CharField(max_length=100)),
                ('scantype4', models.CharField(max_length=100)),
                ('scannum4', models.CharField(max_length=100)),
                ('sitetype', models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue')], max_length=100)),
                ('podnumber', models.IntegerField()),
                ('salesorder', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
    ]
