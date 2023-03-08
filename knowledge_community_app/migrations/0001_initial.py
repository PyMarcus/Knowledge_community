# Generated by Django 4.1.7 on 2023-03-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Create at ')),
                ('modify', models.DateTimeField(auto_now=True, verbose_name='Modify at ')),
                ('active', models.BooleanField(default=True, verbose_name='Active? ')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]