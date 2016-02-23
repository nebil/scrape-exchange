
# ScrapeExchange
El objetivo de este _script_ es obtener el `id` del usuario más reciente,
en cualquier sitio relativo a [Stack Exchange](http://stackexchange.com).

## Receta

### Ingredientes
:snake: [Python] será nuestra herramienta de trabajo.  
:warning: Para evitar posibles fallas de compatibilidad,
se **deberá** usar una versión de Python superior a **3.2**.

#### Librerías de Python
Las librerías utilizadas están resumidas en la siguiente tabla.

Nombre           | Descripción                                 | Versión
---------------- | ------------------------------------------- | ---------
[requests]       | Una librería para generar solicitudes HTTP. | **2.9.1**
[beautifulsoup4] | Una librería para realizar _web scraping_.  | **4.4.1**

Estas librerías también aparecen en `requirements.txt`.
Luego, se **deberá** usar este archivo para instalarlas con [pip].  
Esto nos permitirá trabajar con las mismas versiones,
consiguiendo instalaciones **replicables**, sin hacer esfuerzo.  
Bueno, un poco: debemos escribir...

```sh
$ pip install -r requirements.txt
```

En efecto, esto es... _as easy as **py**_. :grinning:

### Preparación
Para utilizar este _script_, debes seguir los siguientes pasos.

1. :sheep:
   Clona el repositorio. Luego, accede.

   ```sh
   $ git clone https://github.com/nkawasg/scrape-exchange.git
   $ cd scrape-exchange
   ```

2. :wrench:
   Genera un entorno virtual de Python v3.**X** con [virtualenv].
   En este caso, se llamará `venv`.  
   No olvides que **X** debe ser: {2, 3, 4, 5}.

   ```sh
   $ virtualenv --python=python3.X venv
   ```

3. :arrow_forward:
   Activa el entorno virtual.

   ```sh
   $ source venv/bin/activate
   ```

4. :white_check_mark:
   Instala las dependencias con [pip].

   ```sh
   $ pip install -r requirements.txt
   ```

5. :snake:
   Ejecuta el _script_, escribiendo el nombre de algún sitio.
   Por ejemplo, busca para `french`.

   ```sh
   $ python3 scrape.py --site french
   ```

6. :tada:
   _Voilà, mon camarade!_  
   Ahora conoces el número de usuarios registrados en [:fr:].

#### ProTip™
Si no escribes **ninguna** opción, este _script_ te entregará todos los sitios.  
Es decir, para recibir todos los sitios con su respectiva cantidad de usuarios,
sólo debes escribir...

```sh
$ python3 scrape.py
```

:potable_water: Muy bien. Ahora, ve a buscar un vaso de agua.  
:sparkles: Al volver, una flamante tabla te estará esperando.

### Ayuda
Además, puedes pedir (algo de) ayuda al escribir...

```sh
$ python3 scrape.py --help
```

[/]:# (Referencias implícitas)

[python]:         http://www.pyzo.org/_images/xkcd_python.png
[requests]:       https://pypi.python.org/pypi/requests/2.9.1
[beautifulsoup4]: https://pypi.python.org/pypi/beautifulsoup4/4.4.1

[virtualenv]:     https://virtualenv.pypa.io/en/stable
[pip]:            https://pip.pypa.io/en/stable
[:fr:]:           http://french.stackexchange.com
