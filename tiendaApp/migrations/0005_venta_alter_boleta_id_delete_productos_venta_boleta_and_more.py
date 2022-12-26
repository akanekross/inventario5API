# Generated by Django 4.1.3 on 2022-12-05 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaApp', '0004_alter_boleta_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cventa', models.CharField(max_length=100)),
                ('Cproductos', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Cantidad', models.CharField(max_length=100)),
                ('Categoria', models.CharField(max_length=100)),
                ('PrecioT', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='boleta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
        migrations.AddField(
            model_name='venta',
            name='boleta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaApp.boleta'),
        ),
        migrations.AddField(
            model_name='venta',
            name='usuario1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaApp.usuario'),
        ),
    ]