# Practica_Semana_1
El objetivo de esta semana es crear un crawler y estudiar el lenguaje de programación Python. 

Para la realización del scrap se utilizó el paquete Selenium, ya que la naturaleza de la página corresponde a una página web dinámica.
Se destaca la posibilidad de realizar este con Rstudio, a través del paquete RSelenium.

Selenium es una herramienta, que a través de un driver, genera una navegación web simulada. 

Este driver permite la navegación a través de la definición de un url. Cabe señalar, que la composición web de cada página puede variar, ya sea de manera física, para caso de scrapping de tablas, o dinámica, para el caso de elementos que se carguen a medida que el usuario interactue con la página (generalmente a través de scroll).

En efecto, una vez se genera la navegación web, se procede a determinar los elementos a extraer; estos se ubican detro de <div> o <a> <href> (elementos codificados en HTML).

Así, se efectuó un scrap a la página web de retail, generando un pequeño dataset con información relativa a productos, precios y marcas.
