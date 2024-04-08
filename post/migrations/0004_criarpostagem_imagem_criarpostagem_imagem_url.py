# Generated by Django 5.0.3 on 2024-03-30 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_criarpostagem_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='criarpostagem',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='post'),
        ),
        migrations.AddField(
            model_name='criarpostagem',
            name='imagem_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]