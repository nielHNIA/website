# Generated by Django 4.0.1 on 2023-12-22 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0002_alter_university_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websites.university')),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
