## TPComplejidad
### Tales Salesman Problem
#### Introducción
El problema del vendedor viajero responde a la siguiente pregunta: dada una lista de ciudades y las distancias entre cada par de ellas. 

¿Cuál es la ruta más corta posible que visita cada ciudad exactamente una vez y al finalizar regresa a la ciudad origen? Este es un problema  

NP-Hard(conjunto de los problemas de decisión) dentro en la optimización combinatoria.   
El problema fue formulado por primera vez en 1930 y la motivación que encontramos en el problema es que es uno de los problemas de optimización más estudiados. Es usado como prueba para muchos métodos de optimización.Aunque el problema es computacionalmente complejo, una gran cantidad de heurísticas y métodos exactos son conocidos, de manera que, algunas instancias desde cien hasta miles de ciudades pueden ser resueltas.
Encontrar una solución con los conocimientos adquiridos hasta el momento en el curso de complejidad algorítmica es un reto para los alumnos, y ayudara a desarrollar nuestro pensamiento crítico al momento de solucionar problemas
#### Objetivos
- Encontrar la mayor cantidad de conexiones con las minimas distancias de un nodo 'x' a un nodo 'y'
- Encontrar distintos tipos de algoritmos usando DFS, BFS , Backtraking y fuerza bruta 
#### Marco teorico
Los algoritmos que en los cuales nos estamos basando son el UCS(Uniform Cost Solution),DFS y backtraking.  
UCS:La búsqueda uniforme de costos es el mejor algoritmo para un problema de búsqueda, que no implica el uso de heurísticas. Puede resolver cualquier gráfico general para un costo óptimo. UCS porque suena búsquedas en nodos que tienen más o menos el mismo costo.

#### Tiempo asintótico  
UCS:
El tiempo asintótico que presenta el UCS es de si el factor de bifurcación es b, cada vez que expandes un nodo, encontrarás k más nodos. Por lo tanto, hay 
 
- 1 nodo en el nivel 0 
- b nodos en el nivel 1 
- b2 nodos en el nivel 2 
- b3 nodos en el nivel 3 
- ... 
- nodos b^k en el nivel k.

Entonces, supongamos que la búsqueda se detiene después de que alcanzas el nivel k. Cuando esto sucede, la cantidad total de nodos que habrá visitado será    
1 + b + b2 + ... + bk = (bk+1 - 1) / (b - 1)

#### Conclusiones 
Una solución óptima para resolver el problema será utilizar un método divide y vencerás para partir a la cantidad de nodos en segmentos más pequeños dentro de los cuales podemos encontrar el camino más corto entre 2 nodos alejados usando el algoritmo de UCS y luego conectar a los diferentes segmentos formados con los caminos más cortos para pasar dentro de los mismos.  
Con los algoritmos aprendidos hasta el momento en el curso de Complejidad Algorítmica encontrar una solución que conecte los nodos al 100% pasando por la ruta más corta sería un proceso extremadamente largo por lo que solo se intenta encontrar una solución que soluciona el problema en un porcentaje menos al 100%.    
Utilizar fuerza bruta para solucionar problemas tan grandes tiene un tiempo extremadamente extenso por lo que no es una solución óptima para este problema.
