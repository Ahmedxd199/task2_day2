# Generated by Django 4.0.1 on 2022-01-31 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intake',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('intakename', models.CharField(max_length=30)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='MYUSERSS',
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]
