from django.urls import path
from .scanRegisterView import registrarScanView
from .manualRegisterView import  listFacturasView
from .manualRegisterView import listPagosView
from .manualRegisterView import porcentajeBimestreView
from .manualRegisterView import listVencimientosView
from .manualRegisterView import compararBimestreAnteriorView
from .manualRegisterView import manualRegisterView
from .manualRegisterView import historialConsumoView



urlpatterns = [
    path('scanRegister/', registrarScanView, name='registrarScanView'),
    path('manualRegister/', manualRegisterView, name='manualRegisterView'),
    path('listFacturas/', listFacturasView, name='listFacturasView'),
    path('listPagos/', listPagosView, name='listPagosView'),
    path('listVencimientos/<str:id_factura>/', listVencimientosView, name='listVencimientosView'),
    path('listPorcentajeBimestre/<str:id_factura>/', porcentajeBimestreView, name='porcentajeBimestreView'),
    path('compararBimestreAnterior/<str:id_factura>/', compararBimestreAnteriorView, name='compararBimestreAnteriorView'),
    path('historialConsumo/<str:id_suministro>/', historialConsumoView, name='historialConsumoView'),



]