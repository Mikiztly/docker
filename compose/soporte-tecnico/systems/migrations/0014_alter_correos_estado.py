# Generated by Django 5.0.6 on 2024-06-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0013_correos_empresa_correos_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correos',
            name='estado',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
