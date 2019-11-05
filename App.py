from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
# Mysql Connection
app.config['MYSQL_H0ST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'marvel_encyclopedia'
mysql = MySQL(app)

# Settings
app.secret_key = '!my_secret*key?'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/buscar/personaje', methods=['GET'])
def listar_personajes():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM personajeMarvel''')
    rv = cur.fetchall()
    print(rv)
    return render_template('listado_personajes.html', personajes=rv)


@app.route('/buscar/colaborador', methods=['GET'])
def listar_colaboradores():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM colaborador''')
    rv = cur.fetchall()
    print(rv)
    return render_template('listado_colaboradores.html', colaboradores=rv)


@app.route('/buscar/revista', methods=['GET'])
def listar_revistas():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM revistaMarvel''')
    rv = cur.fetchall()
    print(rv)
    return render_template('listado_revistas.html', revistas=rv)


@app.route('/buscar/equipo', methods=['GET'])
def listar_equipos():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM equipoMarvel''')
    rv = cur.fetchall()
    print(rv)
    return render_template('listado_equipos.html', equipos=rv)


@app.route('/nuevo/colaborador', methods=['GET', 'POST'])
def agregar_colaborador():
    if request.method == 'POST':
        colaboradorMArvel = request.form
        colaborador = colaboradorMArvel['colaborador']
        abreviatura = colaboradorMArvel['abreviatura']
        descripcion = colaboradorMArvel['descripcion']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO colaborador (colaborador, abreviatura, descripcion) VALUES (%s, %s, %s);",
            (colaborador, abreviatura, descripcion))
        mysql.connection.commit()
        cur.close()
    flash('Personaje agregado satisfactoriamente')
    return render_template('agregar_colaborador.html')


@app.route('/nueva/revista', methods=['GET', 'POST'])
def agregar_revista():
    if request.method == 'POST':
        revistaMarvel = request.form
        pagina = revistaMarvel['pagina']
        titulo = revistaMarvel['titulo']
        edicion = revistaMarvel['edicion']
        anoPublicacion = revistaMarvel['anoPublicacion']
        resena = revistaMarvel['resena']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO revistaMarvel (pagina, titulo, edicion, anoPublicacion, resena) VALUES (%s, %s, %s, %s, %s);",
            (pagina, titulo, edicion, anoPublicacion, resena))
        mysql.connection.commit()
        cur.close()
    flash('Resvista agregada satisfactoriamente')
    return render_template('agregar_revista.html')


@app.route('/nuevo/personaje', methods=['GET', 'POST'])
def agregar_personaje():
    if request.method == 'POST':
        personajeMarvel = request.form
        pagina = personajeMarvel['pagina']
        personaje = personajeMarvel['personaje']
        nombreEnEspanol = personajeMarvel['nombreEnEspanol']
        nombreReal = personajeMarvel['nombreReal']
        ocupacion = personajeMarvel['ocupacion']
        base = personajeMarvel['base']
        altura = personajeMarvel['altura']
        peso = personajeMarvel['peso']
        ojos = personajeMarvel['ojos']
        pelo = personajeMarvel['pelo']
        primeraAparicion = personajeMarvel['primeraAparicion']
        poderes = personajeMarvel['poderes']
        historia = personajeMarvel['historia']
        curiosidades = personajeMarvel['curiosidades']
        colaboradores = personajeMarvel['colaboradores']
        fechaAparicion = personajeMarvel['fechaAparicion']
        debilidad = personajeMarvel['debilidad']
        obsesiones = personajeMarvel['obsesiones']
        causaDelPoder = personajeMarvel['causaDelPoder']
        genero = personajeMarvel['genero']
        enemigos = personajeMarvel['enemigos']
        planetaDeOrigen = personajeMarvel['planetaDeOrigen']
        argumentosEsenciales = personajeMarvel['argumentosEsenciales']
        aliados = personajeMarvel['aliados']
        relacionSentimental = personajeMarvel['relacionSentimental']
        apodo = personajeMarvel['apodo']
        miembrosClave = personajeMarvel['miembrosClave']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO personajeMarvel "
                    "(pagina, personaje, nombreEnEspanol, nombreReal, "
                    "ocupacion, base, altura, peso, ojos, pelo,primeraAparicion, "
                    "poderes, historia, curiosidades, colaboradores, fechaAparicion, "
                    "debilidad, obsesiones, causaDelPoder, genero, enemigos, "
                    "planetaDeOrigen, argumentosEsenciales, aliados, "
                    "relacionSentimental, apodo, miembrosClave) "
                    "VALUES (%s, %s, %s, %s, %s,"
                    " %s, %s, %s, %s, %s, "
                    "%s, %s, %s, %s, %s, "
                    "%s, %s, %s, %s, %s, "
                    "%s, %s, %s, %s, %s, "
                    "%s, %s);", (
                        pagina, personaje, nombreEnEspanol, nombreReal, ocupacion,
                        base, altura, peso, ojos, pelo,
                        primeraAparicion, poderes, historia, curiosidades, colaboradores,
                        fechaAparicion, debilidad, obsesiones, causaDelPoder, genero,
                        enemigos, planetaDeOrigen, argumentosEsenciales, aliados, relacionSentimental,
                        apodo, miembrosClave))
        mysql.connection.commit()
        cur.close()
        flash('Personaje agregado satisfactoriamente')
    return render_template('create_personaje.html')


@app.route('/nuevo/equipo', methods=['GET', 'POST'])
def agregar_equipo():
    if request.method == 'POST':
        equipoMarvel = request.form
        pagina = equipoMarvel['pagina']
        equipo = equipoMarvel['equipo']
        nombreEnEspanol = equipoMarvel['nombreEspanol']
        numeroIntegrantes = equipoMarvel['numeroIntegrantes']
        paisOrigen = equipoMarvel['paisOrigen']
        departamento = equipoMarvel['departamento']
        lider = equipoMarvel['lider']
        base = equipoMarvel['base']
        primeraAparicion = equipoMarvel['primeraAparicion']
        fecha = equipoMarvel['fecha']
        historia = equipoMarvel['historia']
        colaboradores = equipoMarvel['colaboradores']
        aliados = equipoMarvel['aliados']
        enemigos = equipoMarvel['enemigos']
        argumentosEsenciales = equipoMarvel['argumentosEsenciales']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO equipoMarvel "
                    "(pagina, equipo, nombreEspanol, numeroIntegrantes, paisOrigen, "
                    "departamento, lider, base, primeraAparicion, fecha, "
                    "historia, colaboradores, aliados, enemigos, argumentosEsenciales)"
                    "VALUES (%s, %s, %s, %s, %s,"
                    " %s, %s, %s, %s, %s, "
                    "%s, %s, %s, %s, %s);", (pagina, equipo, nombreEnEspanol, numeroIntegrantes, paisOrigen,
                                             departamento, lider, base, primeraAparicion, fecha,
                                             historia, colaboradores, aliados, enemigos, argumentosEsenciales))
        mysql.connection.commit()
        cur.close()
        flash('Equipo agregado satisfactoriamente')
    return render_template('agregar_equipo.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=3000, debug=True)
