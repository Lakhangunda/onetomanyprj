# Generated by Django 4.2.7 on 2023-11-21 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=50)),
                ('u_reg', models.CharField(max_length=50)),
                ('u_address', models.CharField(max_length=50)),
                ('u_email', models.EmailField(max_length=254)),
                ('u_mobile', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
                ('c_address', models.CharField(max_length=50)),
                ('c_mobile', models.BigIntegerField()),
                ('c_code', models.CharField(max_length=50)),
                ('c_email', models.EmailField(max_length=254)),
                ('abc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onetomanyapp.university')),
            ],
        ),
    ]
