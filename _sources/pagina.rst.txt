Pagina Web
============

La clase `PaginaWeb` se define en el módulo `pagina` que documenta en esta página.

La forma típica de utilizar esta clase es

>>> from bccr import PW
>>> PW.buscar("nombre de algún indicador")
>>> datos = PW(indic1 = codigo1, indic2=codigo2)

donde `codigo1` y `codigo2` son los códigos de los indicadorees (posiblemente encontrados con `PW.buscar`), y `indic1` e `indic2` los nombres que se le quiere asignar a estos indicadores.

En la documentación que sigue a continuación aparecen más ejemplos. `En esta página se muestra un cuaderno de Jupyter que ilustra el uso de esta clase <http://randall-romero.com/demo-bccr-paginaweb>`_.

|
|


.. automodule:: bccr.pagina
    :members: