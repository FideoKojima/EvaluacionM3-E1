# 🐍 Proyecto de Programación Básica en Python

Este proyecto abarca cinco ejercicios que exploran diversos conceptos de programación en Python, incluyendo estructuras de datos como listas, sets y diccionarios, así como operaciones de texto y manejo de excepciones. El programa ejecuta todos los ejercicios en secuencia y finaliza automáticamente al completar el último.

## 📚 Ejercicios

### 1️⃣ Ordenar números
- **Objetivo**: Leer y ordenar una lista de números.
- **Funcionamiento**: 
  - Lee entre 10 y 20 números ingresados por el usuario.
  - Los almacena en una lista y los ordena de mayor a menor.
  - Muestra la lista ordenada en pantalla.
- **Nota**: La entrada finaliza cuando el usuario ingresa `0` (no se incluye en la lista final).

### 2️⃣ Palabras únicas
- **Objetivo**: Almacenar palabras únicas ingresadas por el usuario.
- **Funcionamiento**:
  - Guarda las palabras en un conjunto (set) para evitar duplicados.
  - La entrada termina cuando el usuario ingresa `***`.
  - Muestra todas las palabras únicas ingresadas.

### 3️⃣ Puntaje Scrabble
- **Objetivo**: Calcular el puntaje de una palabra según las reglas de Scrabble.
- **Funcionamiento**:
  - Utiliza un diccionario con valores de puntos para cada letra.
  - El usuario ingresa una palabra.
  - El programa calcula y muestra el puntaje total.
- **Puntuación**:
  | Puntos | Letras |
  |--------|--------|
  | 1      | A, E, I, L, N, O, R, S, T, U |
  | 2      | D, G |
  | 3      | B, C, M, P |
  | 4      | F, H, V, W, Y |
  | 5      | K |
  | 8      | J, X |
  | 10     | Q, Z |

### 4️⃣ Anagramas
- **Objetivo**: Determinar si dos palabras son anagramas.
- **Funcionamiento**:
  - El usuario ingresa dos palabras.
  - El programa verifica si tienen las mismas letras en distinto orden.
  - Informa si son anagramas o no.

### 5️⃣ Suma de números
- **Objetivo**: Sumar una serie de números ingresados por el usuario.
- **Funcionamiento**:
  - El usuario ingresa números uno por uno.
  - El programa suma todos los números válidos.
  - Maneja errores si se ingresa un carácter no numérico.
  - Finaliza cuando el usuario presiona "Enter" sin ingresar un número.

## 🛠️ Requisitos

- Python 3.x

## 🚀 Instrucciones de ejecución

1. Clona el repositorio o descarga el archivo `.py`.
2. Abre una terminal y navega hasta el directorio del proyecto.
3. Ejecuta el siguiente comando:
   ```bash
   python Nombre_Apellido_TI_M3_Asignatura.py
   ```
4. Sigue las instrucciones en pantalla para cada ejercicio.
5. El programa finalizará automáticamente después del último ejercicio.

## 🏗️ Estructura del código

| Función | Descripción |
|---------|-------------|
| `ejercicio1()` | Implementa el ordenamiento de números |
| `ejercicio2()` | Maneja el almacenamiento de palabras únicas |
| `ejercicio3()` | Calcula el puntaje Scrabble |
| `ejercicio4()` | Verifica anagramas |
| `ejercicio5()` | Realiza la suma de números |
| `main()` | Coordina la ejecución de todos los ejercicios |

## 🔍 Características adicionales

- ⚠️ Manejo de excepciones en el ejercicio 5 para una ejecución robusta.
- 🔄 Flujo automático entre ejercicios sin intervención manual.

## 👨‍💻 Autor

Desarrollado por **Luis Suarez** para el curso "Programación Básica" Módulo 3.

## 📝 Notas

- Este proyecto cumple con los requisitos específicos del curso.
- Para consultas o reporte de errores, contacta a consejeria@ipp.cl.

---

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) # EvaluacionM3-E1
