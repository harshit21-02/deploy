# Generated by Django 4.2.4 on 2023-08-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_candidateresponse_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="resume",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="resume",
            name="summary",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
