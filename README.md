# modmat_ex
Ejercicios de la clase de modelación matemática

## marea_fft.py
Realiza una aproximación del nivel de marea, a partir de las componentes con mayor magnitud obtenidas por medio de FFT. Genera un gráfica del espectro obtenido con la FFT, así como un acercamiento a las componentes diurnas y semidiurnas. La gráfica del espectro se muestra con escalas logarítmicas para observar mejor el resultado. Las componentes encontradas se muestran en morado, y se resaltan en rojo las componentes seleccionadas (mayores a la magnitud indicada). En los acercamientos se muestra con líneas punteadas la posición de las 7 componentes indicadas en el material del curso (M2, N2, S2, K2, K1, O1, P1).

Una segunda figura muestra (en la parte superior) una porción de los datos junto a la aproximación correspondiente, mientras que en la parte inferior se muestra una gráfica del error absoluto (escala para todo el periodo).

Lee los datos de nivel de marea de un archivo de texto (csv sin encabezado, formato dado), la ruta y nombre del archivo se deben pasar com parámetro.

Ejemplo: python marea_fft.py ../datos/acapulco2013.txt

### Requiere 
* numpy
* matplotlib
* cmm_lib (archivo incluido)
