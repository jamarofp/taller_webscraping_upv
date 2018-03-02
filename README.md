# TALLER DE WEBSCRAPING CON PYTHON 02/03/2018
(Pablo)

## Python
- Débilmente tipado
- Lenguaje imperativo con trazas funcionales
- Los desarrolladores en Python están bien valorados

`virtualenv` is a tool to create isolated Python environments.
Pip: Gestiona paquetes de Python
REPL (o iPython)


## Webscraping
- Podemos ver la web como una gran base de datos

- Ejemplo: Descarga masiva de ficheros

### Beautiful Soup
- Librería de webscraping escrita en Python fácil de usar
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/

### El flujo básico
1. Seleccionar el contenido
2. Obtener la url inicial
3. Obtener el HTML de la url
4. Parsear el texto del HTML (Beautiful Soup)
5. Seleccionar datos
6. Procesar los datos
7. (Volver a 3 si hay más urls)

## Problemas o retos
- GET vs POST (requests con parámetros)
- Cookies (request permite gestionar cookies)
- Comportamiento robótico (captchas, slides,... hay librerías que permiten resolverlos, crowsourcing)
- Multi-hilo (cuando se necesita recoger gran cantidad de datos)
- Multi-máquinas (para evitar repetir la misma IP)
- Banear IPs (distintas máquinas o desde distintos servidores, VPN (cambia IP a menudo))
  - Recomendable trabajar con VPN (tunel via, 50 €/año)
- Cambios en el HTML (rediseño web, test AB (marketing))

## Algunos proyectos

- TIPI Ciudadano (GitHub)
- LibreBORME (Boletín Oficial del Registro Mercantil)
- Proyecto Colibrí (GitHub. Votaciones del congreso -> API)
- BOE API (GitHub)
- Canales de chollos de Telegram






--------------

sudo apt install python-pip
pip freeze (indica todo lo que está instalado)
iPython (consola)



Paquetes principales:
- requests
- beautifulsoup4

GET: requests
POST: requests.post



`dir(variable)`: indica los atributos que tiene la variable

`soup = BeautifulSoup(req.text, "html.parser")`: parsea el contenido de la web

con `soup.h2` obtenemos los h2

```
contacts = soup.find_all("a", class_="contact")
contacts[0]['href']
contacts[0].text
```
