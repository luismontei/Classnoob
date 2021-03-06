# Generated by Django 4.0.1 on 2022-05-26 16:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0006_comentario_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='data_criacao',
            field=models.DateField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentario',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
