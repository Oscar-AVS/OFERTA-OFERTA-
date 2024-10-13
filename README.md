# OFERTA-OFERTA-
CONTEXTO E IMPORTANCIA:

Cada vez que nos encontramos buscando algo que comprar ya sea en el súper, en tiendas de ropa, etc... tendemos a buscar ofertas o el mejor precio posible, la idea de la aplicación Oferta Oferta !! Es poder dar al usuario una librería de ofertas comunes que podemos encontrar en algún supermercado o alguna tienda de ropa. Por ejemplo, cuando vamos a cierto supermercado, existen los tan mencionados 3*2 los cuales nos dan un 3 producto gratis al comprar 2, este tipo de ofertas podemos verlas en más lugares y de diferentes maneras. 

El punto de esta aplicación es poder darle al usuario la opción de elegir qué tipo de descuento está obteniendo en su tienda, con datos específicos como la cantidad de productos, su precio unitario y como se mencionó, el descuento que se va a aplicar, poderle dar un desglose de cuánto estaría pagando por cada artículo y  cuánto porcentaje existe de ahorro.  De igual manera el usuario podría ingresar o seleccionar el nombre de la tienda de donde está comprando para que al finalizar pueda comparar su ahorro con otras tiendas. 


Este proyecto tiene una importancia relevante para la sociedad, sobretodo para familias que van al super y que desean economizar lo más que se pueda en sus compras y un problema que he podido ver, es que siempre que encontramos alguna oferta intentamos hacer cuentas rápidas de cuánto conviene comprar o si realmente estamos ahorrando, estas dudas usualmente suelen responderse hasta que se tiene un ticket con el total de la compra. Es por eso que  ésta app hace que sea mucho más fácil poder darse cuenta de si verdaderamente se está haciendo un ahorro en las compras.

Se utilizarán los conceptos de funciones, para poder tener un "banco" de las ofertas más recurrentes como 3x2 o compra 1 y llévate el 2ndo a mitad de precio, 2x1, etc... y poder decirle al usuario qué tanto ahorra por cada producto que lleva.


**Algoritmo General
**

Entrada: 
Usuario ingresa una opción del menú para calcular la oferta, comparar ahorros, ejecutar pruebas o salir 
          Usuario ingresa el tipo de oferta que quiere calcular 
          Usuario selecciona la tienda en donde está comprando del archivo .txt o en su defecto incresa una nueva 

PROCESO: 

Si el usuario selecciona 1. Calcular oferta 
               Desplegar opciones de ofertas para que el usuario seleccione la opción deseada
                         Si la opción es 3x2 
                                   Preguntar cantidad de productos a comprar y precio unitario 
                                   Separar cantidad de productos en grupos de 3 y por cada 3 multiplicar el precio unitario *2 
                         Si la opción es 2x1 
                                    Preguntar cantidad de productos a comprar y precio unitario 
                                   Separar cantidad de productos en grupos de 2 y  solamente sumar 1 precio unitario 
                          Si la opción es 2x1.5 
                                    Preguntar cantidad de productos a comprar y precio unitario 
                                   Separar cantidad de productos en grupos de 2 y  multiplicar precio unitario *0.5 
                        Si la opción es para un porcentaje de descuento, calcular el total a pagar y el ahorro usando la función calcular_descuento_porcentaje().
                                     Almacenar el nombre de la tienda y el ahorro en una lista (lista_tiendas).
                        Si la opción es "Comparar ahorros":
                                       Mostrar una comparación de los ahorros acumulados en cada tienda utilizando la lista de tiendas.
                        Si la opción es "Pruebas":
                                               Ejecutar casos de prueba predefinidos para verificar el correcto funcionamiento de las funciones.
                        Si la opción es "Salir":
                                         Terminar el programa.
Salida:

Mostrar al usuario:
                         El total a pagar y el ahorro obtenido para la oferta seleccionada.
                         La comparación de ahorros entre las diferentes tiendas (si seleccionó la opción de comparar).
                         Mensaje de despedida si elige salir.
Fin
