# Generated by Django 4.2.11 on 2024-04-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cadastro", "0006_remove_cadastro_is_super_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="cadastro",
            name="is_super_user",
            field=models.BooleanField(default=False),
        ),
    ]
