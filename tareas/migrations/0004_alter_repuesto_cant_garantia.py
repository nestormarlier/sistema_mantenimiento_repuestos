# Generated by Django 4.2.5 on 2023-09-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0003_repuesto_cant_garantia_alter_repuesto_garantia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesto',
            name='cant_garantia',
            field=models.IntegerField(default=0, verbose_name='Cantidad meses de garantía'),
        ),
    ]
