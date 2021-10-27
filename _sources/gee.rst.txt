Servicio Web
============

La clase `ServicioWeb` se define en el módulo `gee` que documenta  en esta página.

La forma típica de utilizar esta clase es

>>> from bccr import SW
>>> SW.buscar("nombre de algún indicador")
>>> datos = SW(indic1 = codigo1, indic2=codigo2)

donde `codigo1` y `codigo2` son los códigos de los indicadorees (posiblemente encontrados con `SW.buscar`), y `indic1` e `indic2` los nombres que se le quiere asignar a estos indicadores.

En la documentación que sigue a continuación aparecen más ejemplos.

|
|

.. automodule:: bccr.gee
    :members: