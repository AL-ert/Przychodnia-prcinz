# Generated by Django 4.0.6 on 2022-11-11 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_lekarze_options_alter_pacjenci_options'),
        ('rezerwacje', '0003_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appointment',
            new_name='Rezerwacje',
        ),
        migrations.AlterModelOptions(
            name='rezerwacje',
            options={'verbose_name_plural': 'Rezerwacje'},
        ),
    ]
