# Generated by Django 4.2.4 on 2023-10-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_securityanswer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewSecurityQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
