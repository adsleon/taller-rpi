# Sistema de Semáforo Completo con Botón de Paso Peatonal usando Raspberry Pi

El objetivo de este ejercicio es construir un sistema de semáforo totalmente funcional, similar a los cruces peatonales reales, controlado mediante una Raspberry Pi.

## Requisitos del sistema

- **Semáforo de coches**
  - Luz roja
  - Luz ámbar
  - Luz verde
- **Semáforo de peatones**
  - Luz roja peatón
  - Luz verde peatón
- **Botón** de solicitud de paso peatonal

Para facilitar el aprendizaje, el proyecto se divide en etapas claramente separadas, cada una con un objetivo concreto.

---

## Etapa 1 — Encendido básico de un solo LED

1. Conectar un único LED rojo.
2. Escribir un programa en Python que encienda ese LED durante 15 segundos.
3. Después de los 15 segundos, el LED debe apagarse.
4. Verificar que el montaje funciona correctamente.

## Etapa 2 — Control independiente de dos LEDs

1. Añadir un segundo LED de color verde.
2. Escribir un programa que:
	- Encienda primero el LED rojo.
	- Apague el LED rojo y encienda el LED verde.
	- Apague el LED verde.
3. El nuevo LED debe permanecer encendido al menos 15 segundos.
4. Comprobar que ambos LEDs responden correctamente.

## Etapa 3 — Semáforo básico para coches (3 colores)

1. Añadir un led para tener los tres: verde (coches), ámbar (coches) y rojo (coches).
2. Programar el ciclo automático del semáforo:
	- Encender verde durante 5 segundos.
	- Apagar verde y encender ámbar durante 2 segundos.
	- Apagar ámbar y encender rojo durante 10 segundos.
	- Repetir el ciclo indefinidamente.
3. Verificar que los LEDs funcionan en el orden correcto.

## Etapa 4 — Incorporación del botón peatonal

1. Conectar un botón a un pin de entrada de la Raspberry Pi.
2. Detectar por software si el botón ha sido pulsado.
3. Mostrar por pantalla el mensaje `Botón pulsado` cuando ocurra.
4. Mantener el semáforo de coches funcionando en su ciclo normal, sin cambios (en esta etapa el botón solo se detecta).

## Etapa 5 — Comportamiento especial al pulsar el botón

1. Modificar el ciclo del semáforo para que:
	- Si el botón no se pulsa, el semáforo sigue funcionando normalmente para coches.
	- Si el botón se pulsa, se inicie un ciclo especial que dé paso a los peatones.
2. El ciclo especial debe funcionar así:
	- Esperar a que el semáforo de coches esté en rojo (o forzar la transición segura).
	- Mantener rojo coches durante al menos 5 segundos adicionales.
3. Una vez activado el ciclo especial, se deben ignorar pulsaciones adicionales hasta que finalice el ciclo.

## Etapa 6 — Añadir el LED de peatones (solo rojo inicialmente)

1. Conectar el LED de rojo peatón.
2. Programar que, mientras el semáforo de coches esté en verde o ámbar, el peatón esté siempre en rojo.
3. Verificar su funcionamiento.

## Etapa 7 — Añadir los dos LEDs del semáforo de peatones

1. Conectar los LEDs faltantes de peatón: rojo y verde.
2. Integrar el comportamiento completo:
	- En ciclo normal: peatón siempre en rojo.
	- Cuando se pulse el botón:
	  1. Cambiar semáforo de coches a rojo.
	  2. Encender verde peatón durante 5 segundos.
	  3. Apagar verde peatón.
	  4. Encender rojo peatón.
	  5. Reiniciar el ciclo normal de coches.
3. Durante el verde peatón, el semáforo de coches debe permanecer estrictamente en rojo.

## Etapa 8 — Sistema completo funcionando de forma autónoma

El sistema final debe:

- Mantener un ciclo automático del semáforo de coches.
- Permitir que un peatón pulse el botón para pedir paso.
- Gestionar la espera para garantizar seguridad.
- Dar paso peatonal de forma ordenada.
- Volver automáticamente al ciclo normal.
