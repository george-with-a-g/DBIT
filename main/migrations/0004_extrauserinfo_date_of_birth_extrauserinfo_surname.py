# Generated by Django 5.1.7 on 2025-06-06 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_usertype_extrauserinfo_usertypeallocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrauserinfo',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extrauserinfo',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
