import matplotlib.pyplot as matplotlib_inline
from collections import Counter

years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
matplotlib_inline.plot(years, gdp, color='green', marker='o', linestyle='solid')
matplotlib_inline.title("Nominal GDP")
matplotlib_inline.ylabel("Billion of $")
matplotlib_inline.show()
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
xs = [i for i,_ in enumerate(movies)]
matplotlib_inline.bar(xs,num_oscars)
matplotlib_inline.ylabel("# de Premios Oscar")
matplotlib_inline.title("Películas")
matplotlib_inline.xticks([i for i,_ in enumerate(movies)],movies)
matplotlib_inline.show()
calificaciones=[83,95,91,87,70,0,85,82,100,67,73,77,0]
deciaml = lambda calificacion: calificacion//10*10
histograma = Counter(deciaml(calificacion) for calificacion in calificaciones)
matplotlib_inline.bar([x for x in histograma.keys()],histograma.values(),8)
matplotlib_inline.xticks([i*10 for i in range(11)])
matplotlib_inline.axis([-5,105,0,5])
matplotlib_inline.ylabel("# de estudiantes")
matplotlib_inline.xlabel("Nota")
matplotlib_inline.title("Primer examen")
matplotlib_inline.show()
varianza=[1,2,4,8,16,32,64,128,256]
tendenciaCuadrada = [256,128,64,32,16,8,4,2,1]
xs = [i for i,_ in enumerate(tendenciaCuadrada)]
error=[x+y for x,y in zip(varianza,tendenciaCuadrada)]
matplotlib_inline.plot(xs,varianza,"r-",label="Varianza")
matplotlib_inline.plot(xs,tendenciaCuadrada,"p-",label="Tendencia^2")
matplotlib_inline.plot(xs,error,"b:",label="Error")
matplotlib_inline.legend(loc=9)
matplotlib_inline.xlabel("Complejidad del modelo")
matplotlib_inline.title("El intercambio del sesgo-varianza")
matplotlib_inline.show()
amigos=[70, 65, 72, 63, 71, 64, 60, 64, 67]
minutos=[175, 170, 205, 120, 220, 130, 105, 145, 190]
etiquetas=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
matplotlib_inline.scatter(amigos,minutos)
for etiqueta,cuentaAmigos,cuentaMinutos in zip(etiquetas,amigos,minutos):
    matplotlib_inline.annotate(etiqueta,xy=(cuentaAmigos,cuentaMinutos),xytext=(5,-5),textcoords='offset points')
matplotlib_inline.xlabel("# de amigos")
matplotlib_inline.ylabel("# de minutos en el sitio")
matplotlib_inline.title("Minutos vs Amigos")
matplotlib_inline.show()
notasExamen1 = [99, 90, 85, 97, 80]
notasExamen2 = [100, 85, 60, 90, 70]
matplotlib_inline.scatter(notasExamen1,notasExamen2)
matplotlib_inline.xlabel("Notas examen 1")
matplotlib_inline.ylabel("Notas examen 2")
matplotlib_inline.title("Relacionadas")
matplotlib_inline.axis("equal")
matplotlib_inline.show()