# Generated by Django 4.0.1 on 2022-04-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0002_link_delete_pergunta_delete_resposta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
    ]
