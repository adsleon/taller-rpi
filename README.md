# Taller de Iniciación a Raspberry Pi — ADS

> **Asociación de Desarrollo de Software de la Universidad de León (ADS)**
> Aprende a programar, experimentar y crear proyectos con Raspberry Pi desde cero

---

## Introducción

Este repositorio contiene todos los recursos, ejemplos y documentación del **taller de iniciación a Raspberry Pi** impartido por la **Asociación de Desarrollo de Software de la Universidad de León (ADS)**.
El objetivo del taller es aprender los fundamentos del uso de la Raspberry Pi en proyectos de informática, ingeniería y programación con **Python**.

Durante la sesión veremos cómo controlar **LEDs**, **botones**, y entender el funcionamiento del **GPIO** (General Purpose Input/Output) paso a paso.

---

## Estructura del repositorio

```bash
❯ tree
.
├── Documentacion
│   ├── enlaces.md
│   ├── GPIO-PINOUT.jpeg
│   └── Librería_RPi.GPIO_diferenciacion_pines.md
├── enunciados
│   ├── ejercicio1-pinout.png
│   ├── Enunciado1.md
│   └── Enunciado2.md
├── README.md
└── src
   ├── taller0.0
   │   ├── buttonAccion.py
   │   ├── led17blink.py
   │   ├── led17off.py
   │   └── pressToLed.py
   └── taller1.0
      ├── gipozero
      │   ├── etapa1.py
      │   ├── etapa2.py
      │   ├── etapa3.py
      │   ├── etapa4.py
      │   ├── etapa5.py
      │   ├── etapa6.py
      │   ├── etapa7.py
      │   └── etapa8.py
      └── rpi.gpio
         ├── etapa1.py
         ├── etapa2.py
         ├── etapa3.py
         ├── etapa4.py
         ├── etapa5.py
         ├── etapa6.py
         ├── etapa7.py
         └── etapa8.py

8 directories, 27 files
```

---

## Contenidos del taller

1. **Introducción a la Raspberry Pi**

   * ¿Qué es y cómo funciona?

2. **Primeros pasos en Python**

   * Control de pines GPIO.
   * Ejecución de scripts en la terminal.

3. **Ejercicios prácticos**

   * Encender y apagar un LED.
   * Detectar pulsaciones de un botón.
   * Crear una mini interacción entre ambos.

---

## ⚙️ Ejecución de ejemplos

1. Clona este repositorio:

   ```bash
   git clone https://github.com/adsleon/taller-rpi.git
   cd taller-rpi/src
   ```

2. Ejecuta un script, por ejemplo:

   ```bash
   python3 led17blink.py
   ```

3. Observa el resultado en tu Raspberry Pi

---

## Documentación visual

En la carpeta [`Documentacion/`](./Documentacion) encontrarás el esquema de pines de la Raspberry Pi (`GPIO-PINOUT.jpeg`) y un archivo con enlaces útiles (`enlaces.md`) para profundizar tras el taller.

Puedes consultar la lista de recursos directamente aquí: [Documentacion/enlaces.md](./Documentacion/enlaces.md)

---

## Sobre ADS

La **Asociación de Desarrollo de Software de la Universidad de León (ADS ULE)** es un grupo de estudiantes apasionados por la informática, el desarrollo y la tecnología.
Organizamos charlas, talleres y proyectos colaborativos abiertos a toda la comunidad universitaria.

---

## Créditos

Taller desarrollado y coordinado por **ADS**.
Contribuciones, sugerencias o mejoras son siempre bienvenidas.

```bash
# Si quieres colaborar:
git fork https://github.com/adsleon/taller-rpi
```

---

 *Explora, programa y haz que tu Raspberry Pi cobre vida.*
