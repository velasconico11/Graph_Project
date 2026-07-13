#Proyecto de grafos
## Entrega 1
Implementación de grafos dirigidos y ponderados usando listas de adyacencia.

## ¿Cómo funciona?
Usamos un diccionario para guardar los nodos y sus conexiones. Es la forma más eficiente y sencilla de representar grafos donde no todos los nodos están conectados entre sí.

## Funciones principales
- **Carga automática:** Lee archivos `.csv` para crear el grafo sin esfuerzo.
- **Análisis:**
    - `vertex_degree`: Cuenta cuántas conexiones salen de un nodo.
    - `is_multigraph`: Detecta si hay lazos o conexiones duplicadas.
    - `is_complete`: Verifica si cada nodo conecta con todos los demás.
    - `is_connected` (Challenge): Verifica si el grafo es conexo, armando una versión no dirigida temporal y recorriéndola con BFS.

## Como nos fue
La lista de adyacencia con diccionario nos resultó simple de armar y de recorrer, y no tuvimos mayor problema con los puntos obligatorios. 


## Entrega 2
Para esta entrega escogimos 4 de los 9 puntos que dejó el profe:
- `is_dag`: dice si el grafo es acíclico (DAG), recorriendo el grafo y viendo si nos topamos con un nodo que ya estábamos visitando en el camino actual.
- `has_euler_circuit` / `has_euler_path`: revisan cuántas flechas entran y salen de cada nodo (y que el grafo sea conexo) para saber si existe un circuito o un camino de Euler.
- `dijkstra`: calcula la distancia más corta desde un nodo hacia todos los demás, asumiendo que los pesos no son negativos.

Escogimos estas cuatro porque le quedaban bien a un grafo dirigido y con pesos como el nuestro. Dejamos por fuera lo de planaridad y número/índice cromático porque son cosas más pensadas para grafos no dirigidos, y hacerlas bien desde cero nos iba a quitar mucho tiempo.

## ¿Cómo nos fue en la Entrega 2?
Como ya teníamos `is_connected` hecho desde la entrega pasada, nos ahorramos trabajo reutilizándolo en las funciones de Euler. Lo que más nos tocó cuidar fue no mezclar las condiciones: para el circuito todos los nodos deben quedar balanceados, pero para el camino se permite que uno quede con una flecha de más saliendo y otro con una de más entrando. Antes de confiar en el resultado con el grafo grande (`grafo32.csv`), probamos las funciones con grafos chiquitos hechos a mano. El Dijkstra lo dejamos en su versión más sencilla, sin usar ninguna librería, para que quedara parejo con el resto del código.

## Ejecución
Solo abre tu terminal en la carpeta y escribe:
```bash
python main.py
