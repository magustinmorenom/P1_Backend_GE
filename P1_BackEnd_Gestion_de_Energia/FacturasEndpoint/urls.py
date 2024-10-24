from django.urls import path
from .scanRegisterView import registrarScanView
from .manualRegisterView import  listFacturasView
from .manualRegisterView import listPagosView
from .manualRegisterView import porcentajeBimestreView
from .manualRegisterView import listVencimientosView
from .manualRegisterView import compararBimestreAnteriorView
from .manualRegisterView import manualRegisterView
from .manualRegisterView import historialConsumoView
from .manualRegisterView import actualizarPago
from .manualRegisterView import getFacturaView



urlpatterns = [
    path('scanRegister/', registrarScanView, name='registrarScanView'),
    path('manualRegister/', manualRegisterView, name='manualRegisterView'),
    path('listFacturas/', listFacturasView, name='listFacturasView'),
    path('getFactura/<str:id_factura>/', getFacturaView, name='getFacturaView'),
    path('listPagos/', listPagosView, name='listPagosView'),
    path('actualizarPago/', actualizarPago, name='actualizarPago'),
    path('listVencimientos/<str:id_factura>/', listVencimientosView, name='listVencimientosView'),
    path('listPorcentajeBimestre/<str:id_factura>/', porcentajeBimestreView, name='porcentajeBimestreView'),
    path('compararBimestreAnterior/<str:id_factura>/', compararBimestreAnteriorView, name='compararBimestreAnteriorView'),
    path('historialConsumo/<str:id_suministro>/', historialConsumoView, name='historialConsumoView'),

] 

