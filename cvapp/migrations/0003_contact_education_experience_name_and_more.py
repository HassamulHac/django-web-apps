# Generated by Django 5.0 on 2023-12-24 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0002_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=100)),
                ('level_of_education', models.CharField(max_length=50)),
                ('degree_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('job_started', models.DateField()),
                ('job_ended', models.DateField(blank=True, null=True)),
                ('responsibilities', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='cv',
            name='education',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='experience',
        ),
        migrations.AddField(
            model_name='cv',
            name='contacts',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvapp.contact'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cvapp.name'),
        ),
        migrations.AddField(
            model_name='cv',
            name='education',
            field=models.ManyToManyField(to='cvapp.education'),
        ),
        migrations.AddField(
            model_name='cv',
            name='experience',
            field=models.ManyToManyField(to='cvapp.experience'),
        ),
    ]