# Generated by Django 4.2.7 on 2024-02-09 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('sprincipal', models.CharField(max_length=100)),
                ('slocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stname', models.CharField(max_length=100)),
                ('sage', models.IntegerField()),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='app.school')),
            ],
        ),
    ]
