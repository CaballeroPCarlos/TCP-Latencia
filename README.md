## ▶️ Cómo ejecutar la simulación paso a paso

### 1. Preparación del entorno
- Instala [Python 3](https://www.python.org/downloads/) en ambas laptops.
- Se recomienda usar **Visual Studio Code** (VS Code) como editor, ya que:
  - Permite abrir varios archivos fácilmente.
  - Integra la terminal para ejecutar scripts.
  - Es compatible con entornos virtuales y extensiones útiles como Python.

### 2. Clonar o copiar los archivos
Guarda los siguientes archivos `.py` en una carpeta compartida del proyecto:
- `servidor_tcp.py`
- `cliente_tcp.py`
- `README.md` (este documento)

### 3. Verificar conexión de red
- Conecta ambas laptops a la **misma red Wi-Fi** del router (no importa si no hay internet).
- Abre una terminal en cada una y comprueba la conectividad con `ping`.

```bash
ping [IP de la otra laptop]
```

### 4. Ejecutar el servidor

- En la laptop que actuará como **controlador**, abre VS Code.
- Abre el archivo `servidor_tcp.py` o `servidor_con_gui.py`.
- Pulsa `Ctrl + Shift + ñ` para abrir la terminal de VS Code.
- Ejecuta el script:

```bash
python servidor_tcp.py
```

### 5. Ejecutar el cliente

- En la otra laptop, abre VS Code y el archivo `cliente_tcp.py`.
- Repite el paso anterior para abrir la terminal integrada.
- Ejecuta el script:

```bash
python cliente_tcp.py
```

### 6. Realizar pruebas

- En el cliente, presiona **Enter** o el **botón** según el archivo usado.
- Observa en el servidor cómo se reciben los datos y se activa el actuador.
- Comprueba si hay errores cuando se simula jitter (retardos aleatorios).

---

### 🧪 Sugerencia para pruebas

- Ejecuta al menos **5 señales** con jitter activado para observar la acumulación de errores.
- Cambia el valor `umbral_ms` en el cliente si deseas usar un criterio de error más o menos estricto.

---
