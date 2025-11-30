#### **Fuente:** [Raspberry Pi GPIO (RPi.GPIO) — SourceForge](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)

# Diferenciación de pines en RPi.GPIO

En RPi.GPIO, al configurar los pines puedes usar dos esquemas diferentes para referenciarlos. El esquema determina cómo se interpreta el número que pasas a las funciones como `GPIO.setup()` o `GPIO.output()`.

---

## Modos disponibles

- **BCM (Broadcom SOC channel)**
	- Usa los números de los pines según el controlador Broadcom integrado en la Raspberry Pi.
	- Ejemplos de identificadores: `GPIO17`, `GPIO27`, `GPIO22`.
	- Se activa con:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
```

- **BOARD (número físico del pin)**
	- Usa la numeración física de los pines del conector de 40 pines (1–40).
	- Ejemplo: el **pin físico 11** corresponde a **GPIO17** en el esquema BCM (en modelos Pi con conector de 40 pines como la Pi 3/4).
	- Se activa con:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
```

> Importante: solo hay que llamar a `GPIO.setmode()` una vez al inicio del programa. Después, todos los números de pines que uses (en `GPIO.setup()`, `GPIO.input()`, `GPIO.output()`, etc.) corresponderán al esquema elegido.

---

## Ejemplos rápidos

- Usando BCM (GPIO17):

```python
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Configura GPIO17
GPIO.output(17, GPIO.HIGH)
```

- Usando BOARD (pin físico 11 — que es GPIO17 en BCM):

```python
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # Configura el pin físico 11
GPIO.output(11, GPIO.HIGH)
```

## Recomendaciones

- Para proyectos que usan esquemas o documentación basada en GPIO (por ejemplo ejemplos que dicen "GPIO17"), es más claro usar `GPIO.BCM`.
- Para montajes físicos o esquemas que referencian los pines por su posición física (p. ej. tutoriales con diagramas del conector), `GPIO.BOARD` puede ser más intuitivo.
- Evita mezclar ambos esquemas en el mismo script — puede causar errores difíciles de depurar.

## Referencias útiles

- Documentación de RPi.GPIO: consulta la [documentación oficial](#fuente-raspberry-pi-gpio-rpigpio--sourceforge) o la ayuda integrada (`help(RPi.GPIO)`) para detalles adicionales.
