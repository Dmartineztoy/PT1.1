# Generated by Django 4.1.3 on 2022-12-03 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extintores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extintor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagid', models.CharField(max_length=50)),
                ('fecha_ultima_mantencion', models.DateField()),
                ('fecha_sig_mantencion', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Notebook',
        ),
    ]
