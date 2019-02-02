# Generated by Django 2.1.4 on 2019-02-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190201_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='despesa',
            name='dia_semana',
        ),
        migrations.AddField(
            model_name='despesa',
            name='cliente',
            field=models.CharField(default='', max_length=200, verbose_name='cliente'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='descricao',
            field=models.CharField(default='', max_length=200, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='produto',
            field=models.CharField(default='', max_length=200, verbose_name='produto'),
        ),
    ]
