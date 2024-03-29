# Generated by Django 4.0.6 on 2022-11-11 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0017_alter_lekarze_image'),
        ('rezerwacje', '0002_delete_lekarze'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='YYYY-MM-DD')),
                ('timeslot', models.IntegerField(choices=[(0, '09:00 – 09:30'), (1, '10:00 – 10:30'), (2, '11:00 – 11:30'), (3, '12:00 – 12:30'), (4, '13:00 – 13:30'), (5, '14:00 – 14:30'), (6, '15:00 – 15:30'), (7, '16:00 – 16:30'), (8, '17:00 – 17:30')])),
                ('lekarz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.lekarze')),
                ('pacjent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.pacjenci')),
            ],
            options={
                'unique_together': {('lekarz', 'date', 'timeslot')},
            },
        ),
    ]
