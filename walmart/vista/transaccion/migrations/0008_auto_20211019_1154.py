# Generated by Django 2.2.12 on 2021-10-19 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0007_auto_20210806_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='folio_boleto',
            field=models.ForeignKey(default=28370, on_delete=django.db.models.deletion.CASCADE, related_name='get_transaccion', to='transaccion.Boleto', verbose_name='Folio boleto'),
        ),
    ]