# Ejercicios- 
En esta carpeta se revisaran alguos ejercicios de estadística.
# Ejercicios-

## Prueba de Hipotesis con shapiro.test. 
Una prueba de hipótesis examina dos hipótesis que se contraponen en relaci??n a una misma muestra o poblaci??n. 

Pra este caso tenemos dos hipotesis que son:
??? __Hip??tesis nula (H0)__: es aquella que afirma


## Ejemplo 
Para inicar creamos dos distribuciones una uniforme y una distribuci??n normal. 

`dataset_1 <- runif(300, min=100, max = 500)`
`dataset_2 <- rnorm(300, mean = 50, sd = 10)`

A continuacion crearemos una funci??n para evaluar la normalidad de una distribuci??n. Esta funcion que vamos a realizar, tendra la capacidad de realizar la prueba de normalidad, graficar su histrograma de densidad junto con la curva de nomalidad y anotara dentro del plot los valores de la prueba de normalidad.

* Dentro de esta funci??n calcularemos la media, la desviacion est??ndar.
* Enseguida se realiza la prueba de normalidad e imprime en la consola los resultados.
* Finalmente se graficar?? el histograma de densidad, se adicionar?? una legenda donde se mostrara el valor < W > y el valor de < p >. Aunado a esto, se dibujara una cruva correspondiente a la funcion de normalidad 

`shapirowilk_plo <- function(x, main = 'Distribucion') {`
 `media <- mean(x)`
 `des <- sd(x)`
  
 `prueba_norm <- shapiro.test(x)`
 `print(prueba_norm)`

  `hist(x,freq=FALSE,xlab = 'Valores',ylab = "Densidad", main = main)`
  `legend ("topleft", legend = c(prueba_norm$method, "W", prueba_norm$statistic, "p.value", prueba_norm$p.value), bty = 'n', cex = 0.4, y.intersp = 0.5, text.font=2)`
  `curve(dnorm(x,media,des), add = T, col="red", lwd = 3)`
}`

Finalmente para corroborar nuestra funci??n, con objetivos didacticos, graficamos las dos distribuciones en una misma ventana.

`par(mfcol = c(2,1))`
`plot_distribucion(dataset_1,main="Distribucion uniforme")`
`plot_distribucion(dataset_2,main="Distribucion normal")`



