# Generated by Django 4.1.5 on 2023-03-04 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=4)),
                ('room_floor', models.IntegerField()),
                ('room_description', models.TextField()),
                ('room_image', models.ImageField(default='sorry no image available', upload_to='')),
                ('room_type', models.CharField(choices=[('Normal', 'Normal'), ('Standard', 'Standard'), ('Luxary', 'Luxalary')], default='Normal', max_length=8)),
                ('current_price_pernight', models.IntegerField(default=800)),
                ('is_boocked', models.BooleanField(default=False)),
                ('beds', models.IntegerField(default=1)),
                ('capasity', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(default=None, null=True)),
                ('check_out', models.DateField(default=None, null=True)),
                ('total_price', models.IntegerField()),
                ('gauest_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel.room')),
            ],
        ),
    ]