# Generated by Django 4.2.8 on 2024-03-03 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerclub', '0005_user_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='data_passport',
            field=models.IntegerField(default=-992111, verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Никнейм'),
        ),
    ]
