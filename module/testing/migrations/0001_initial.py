# Generated by Django 2.2.1 on 2019-05-31 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254, null=True)),
                ('user_phonenumber', models.IntegerField()),
                ('user_joined_date', models.DateField(auto_now_add=True, null=True)),
                ('user_address', models.CharField(max_length=100)),
                ('user_last_activetime', models.TimeField(auto_now=True)),
                ('user_areaofinterest', models.CharField(max_length=40)),
                ('user_cgpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('user_arrear', models.IntegerField()),
            ],
            options={
                'db_table': 'my_user',
            },
        ),
    ]
