# Generated by Django 5.1.2 on 2024-10-21 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suministrosEndPoint', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(null=True)),
                ('bimestre', models.IntegerField(null=True)),
                ('consumo_resultante', models.IntegerField()),
                ('cta_2_fecha_corte', models.DateField(null=True)),
                ('cta_2_primer_vencimiento', models.DateField()),
                ('cta_2_primer_vencimiento_importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cta_2_segundo_vencimiento', models.DateField()),
                ('cta_2_segundo_vencimiento_importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('detalle_facturacion', models.TextField(null=True)),
                ('dias_medidos', models.IntegerField(null=True)),
                ('domicilio_suministro', models.TextField()),
                ('fecha_corte', models.DateField(null=True)),
                ('fecha_emision', models.DateField()),
                ('fecha_lectura_actual', models.DateField()),
                ('fecha_lectura_anterior', models.DateField()),
                ('id_factura', models.CharField(max_length=20, unique=True)),
                ('lectura_actual', models.IntegerField(null=True)),
                ('lectura_anterior', models.IntegerField(null=True)),
                ('nombre_titular', models.CharField(max_length=255)),
                ('nro_medidor', models.IntegerField(null=True)),
                ('primer_vencimiento', models.DateField()),
                ('primer_vencimiento_importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('segundo_vencimiento', models.DateField()),
                ('segundo_vencimiento_importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tarifa', models.TextField(null=True)),
                ('tipo_consumo', models.TextField(null=True)),
                ('total_factura', models.DecimalField(decimal_places=2, max_digits=10)),
                ('file_name', models.CharField(max_length=255, null=True)),
                ('etiqueta', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id_suministro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suministrosEndPoint.suministromodel')),
            ],
        ),
        migrations.CreateModel(
            name='PagoFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuota', models.CharField(choices=[('Primera', 'Primera Cuota'), ('Segunda', 'Segunda Cuota')], max_length=7)),
                ('importe_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateField(blank=True, null=True)),
                ('estado_pago', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado'), ('Vencido', 'Vencido')], default='Pendiente', max_length=10)),
                ('fecha_vencimiento_1', models.DateField()),
                ('fecha_vencimiento_2', models.DateField()),
                ('fecha_corte', models.DateField()),
                ('metodo_pago', models.CharField(blank=True, max_length=50, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='FacturasEndpoint.facturamodel', to_field='id_factura')),
                ('suministro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='suministrosEndPoint.suministromodel')),
            ],
            options={
                'unique_together': {('factura', 'suministro', 'cuota')},
            },
        ),
    ]
