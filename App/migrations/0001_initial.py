# Generated by Django 4.1.2 on 2022-10-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]