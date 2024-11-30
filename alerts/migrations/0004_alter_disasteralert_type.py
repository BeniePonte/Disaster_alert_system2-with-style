# Generated by Django 5.1.3 on 2024-11-29 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0003_userprofile_location_userprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disasteralert',
            name='type',
            field=models.CharField(choices=[('flood', 'Flood'), ('earthquake', 'Earthquake'), ('storm', 'Storm'), ('wildfire', 'Wildfire'), ('hurricane', 'Hurricane'), ('other', 'Other')], max_length=50),
        ),
    ]
