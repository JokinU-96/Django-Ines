# Generated by Django 5.1.6 on 2025-03-20 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_empleado_imagen_alter_empleado_fecha_nacimiento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='Imagen',
            new_name='imagen',
        ),
    ]
