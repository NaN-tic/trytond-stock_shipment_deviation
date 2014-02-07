=====================================================
Stock. Movimientos con más cantidad respeto al pedido
=====================================================

Cuando en una albarán de salida existen movimientos en los que se envía más
cantidad de producto de los que figuran en el pedido de venta que lo genera, el
comportamiento por defecto de Tryton es regalar dicho exceso.

Este módulo asigna el movimiento de stock que crea Tryton con la diferencia de
la cantidad enviada respecto a la cantidad pedida al pedido de venta, y
avisa al usuario que la diferencia se facturará normalmente. La factura creada
no añade ninguna línea sino que en una única línea incluye la totalidad de la
cantidad de producto enviada.
