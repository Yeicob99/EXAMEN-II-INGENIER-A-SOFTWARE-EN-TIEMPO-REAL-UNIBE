# EXAMEN-II-INGENIER-A-SOFTWARE-EN-TIEMPO-REAL-UNIBE

# Sistema de Gestión de Tareas en Tiempo Real (Versión Avanzada)

## Información Académica

* **Universidad:** UNIBE
* **Estudiante:** Jose Jacobo Restrepo
* **Matrícula:** 23-0335
* **Asignatura:** Ingeniería de Software en Tiempo Real
* **Profesor:** Joeryn Moriano Morfe

---

## Descripción

Este proyecto consiste en el desarrollo de un sistema de gestión de tareas en tiempo real, el cual permite ejecutar múltiples tareas de manera concurrente utilizando hilos (threads). El sistema simula un entorno donde varias tareas son procesadas al mismo tiempo, mostrando eventos de inicio y finalización para cada una.

El objetivo principal es aplicar conceptos fundamentales de ingeniería de software como estructuras de datos, algoritmos, concurrencia, manejo de eventos y control de excepciones.

---

## Características

* Ejecución concurrente de múltiples tareas
* Uso de cola (Queue) para gestión de tareas (FIFO)
* Implementación de múltiples hilos (workers)
* Manejo de eventos (inicio y fin de tareas)
* Control de errores mediante excepciones
* Código modular y organizado

---

## Estructura del Proyecto

```
task_manager_pro/
│
├── main.py        # Punto de entrada del sistema
├── manager.py     # Lógica de gestión de tareas y concurrencia
├── task.py        # Definición de la clase Task
├── README.md      # Documentación del proyecto
```

---

## Requisitos

* Python 3.x instalado

---

## Instalación y Ejecución

1. Descargar o clonar el proyecto
2. Abrir una terminal en la carpeta del proyecto
3. Ejecutar el siguiente comando:

```
python main.py
```

---

## Ejemplo de Ejecución

Al ejecutar el programa, se mostrarán mensajes como:

```
[EVENTO] Iniciando tarea: Tarea A
[EVENTO] Iniciando tarea: Tarea B
[EVENTO] Tarea finalizada: Tarea B
[EVENTO] Tarea finalizada: Tarea A
Todas las tareas procesadas
```

Esto demuestra que las tareas se ejecutan de forma concurrente.

---

## Conceptos Aplicados

* **Estructuras de datos:** Uso de Queue para gestionar tareas
* **Algoritmos:** Modelo productor-consumidor
* **Programación concurrente:** Uso de múltiples hilos
* **Eventos:** Notificación de inicio y finalización de tareas
* **Excepciones:** Manejo de errores para garantizar estabilidad

---

## Posibles Mejoras

* Implementar interfaz gráfica
* Integrar base de datos para persistencia
* Añadir prioridades a las tareas
* Implementar sistema de logs

---

## Autor

Jose Jacobo Restrepo
Estudiante de Ingeniería de Software

---
