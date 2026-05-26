#Proyecto de grafos

Implementación de grafos dirigidos y ponderados usando listas de adyacencia.

## ¿Cómo funciona?
Usamos un diccionario para guardar los nodos y sus conexiones. Es la forma más eficiente y sencilla de representar grafos donde no todos los nodos están conectados entre sí.

## Funciones principales
- **Carga automática:** Lee archivos `.csv` para crear el grafo sin esfuerzo.
- **Análisis:**
    - `vertex_degree`: Cuenta cuántas conexiones salen de un nodo.
    - `is_multigraph`: Detecta si hay lazos o conexiones duplicadas.
    - `is_complete`: Verifica si cada nodo conecta con todos los demás.

## Ejecución
Solo abre tu terminal en la carpeta y escribe:
```bash
python main.py
