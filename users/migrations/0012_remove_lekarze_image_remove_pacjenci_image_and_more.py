# Generated by Django 4.0.6 on 2022-11-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_lekarze_tytul_alter_lekarze_specjalizacja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lekarze',
            name='image',
        ),
        migrations.RemoveField(
            model_name='pacjenci',
            name='image',
        ),
        migrations.AddField(
            model_name='myuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='konto_pics'),
        ),
    ]
