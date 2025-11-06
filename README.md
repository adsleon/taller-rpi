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
taller-rpi/
├── Documentacion/
│   ├── enlaces.txt            # Recursos y documentación adicional
│   └── GPIO-PINOUT.jpeg       # Diagrama de pines de la Raspberry Pi
├── src/
│   ├── buttonAccion.py        # Acciones básicas con un botón
│   ├── led17blink.py          # Parpadeo de un LED conectado al pin 17
│   ├── led17off.py            # Apagado manual del LED
│   └── pressToLed.py          # Encendido del LED al presionar el botón
└── README.md
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

En la carpeta [`Documentacion/`](./Documentacion) encontrarás el esquema de pines de la Raspberry Pi (`GPIO-PINOUT.jpeg`) y un archivo con enlaces útiles (`enlaces.txt`) para profundizar tras el taller.

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
