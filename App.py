from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
# Mysql Connection
app.config['MYSQL_H0ST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'marvel_encyclopedia'
mysql = MySQL(app)


# Settings
app.secret_key = '!my_secret*key?'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/eliminar/revista/<id>')
def eliminar_revista(id):
    cur = mysql.connection.cursor()
    sql = 'DELETE FROM revistaMarvel WHERE id LIKE %s'
    args = [id,]
    cur.execute(sql, args)
    mysql.connection.commit()
    flash('Revista eliminada satisfactoriamente')
    return listar_revistas()


@app.route('/eliminar/colaborador/<id>')
def eliminar_colaborador(id):
    cur = mysql.connection.cursor()
    sql = 'DELETE FROM colaborador WHERE id LIKE %s'
    args = [id,]
    cur.execute(sql, args)
    mysql.connection.commit()
    flash('Colaborador eliminado satisfactoriamente')
    return listar_colaboradores()


@app.route('/eliminar/equipo/<id>')
def eliminar_equipo(id):
    cur = mysql.connection.cursor()
    sql = 'DELETE FROM equipoMarvel WHERE id LIKE %s'
    args = [id,]
    cur.execute(sql, args)
    mysql.connection.commit()
    flash('Equipo eliminado satisfactoriamente')
    return listar_equipos()


@app.route('/eliminar/personaje/<id>')
def eliminar_personaje(id):
    cur = mysql.connection.cursor()
    sql = 'DELETE FROM equipoMarvel WHERE id LIKE %s'
    args = [id,]
    cur.execute(sql, args)
    mysql.connection.commit()
    flash('Personaje eliminado satisfactoriamente')
    return listar_personajes()


@app.route('/editar/revista/<id>')
def obtener_revista(id):
    cur = mysql.connection.cursor()
    sql = 'SELECT * FROM revistaMarvel WHERE id = %s'
    args = [id, ]
    cur.execute(sql, args)
    rv = cur.fetchall()
    print(rv)
    return render_template('editar_revista.html', revista=rv[0])


@app.route('/editar/colaborador/<id>')
def obtener_colaborador(id):
    cur = mysql.connection.cursor()
    sql = 'SELECT * FROM colaborador WHERE id = %s'
    args = [id, ]
    cur.execute(sql, args)
    rv = cur.fetchall()
    print(rv)
    print('LO obtiene de la DB')
    return render_template('editar_colaborador.html', colaborador=rv[0])


@app.route('/editar/equipo/<id>')
def obtener_equipo(id):
    cur = mysql.connection.cursor()
    sql = 'SELECT * FROM equipoMarvel WHERE id = %s'
    args = [id, ]
    cur.execute(sql, args)
    rv = cur.fetchall()
    print(rv)
    print('Lo obtiene de la DB')
    return render_template('editar_equipo.html', equipo=rv[0])


@app.route('/editar/personaje/<id>')
def obtener_personaje(id):
    cur = mysql.connection.cursor()
    sql = 'SELECT * FROM personajeMarvel WHERE id = %s'
    args = [id, ]
    cur.execute(sql, args)
    rv = cur.fetchall()
    print(rv)
    print('Lo obtiene de la DB')
    return render_template('editar_personaje.html', personaje=rv[0])


@app.route('/editar/revista<id>', methods=['POST'])
def editar_revista(id):
    print (id)
    if request.method =='POST':
        revista = request.form
        print(revista)
        pagina = revista['pagina']
        titulo = revista['titulo']
        edicion = revista['edicion']
        anoPublicacion = revista['anoPublicacion']
        resena = revista['resena']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE revistaMarvel "
                    "SET pagina = %s, "
                    "titulo = %s, "
                    "edicion = %s, "
                    "anoPublicacion = %s, "
                    "resena = %s "
                    "WHERE id = %s;", (int(pagina), titulo, edicion, int(anoPublicacion), resena, int(id)))
        mysql.connection.commit()
        flash('Revista actualizada satisfactoriamente')
    return listar_revistas()


@app.route('/editar/colaborador<id>', methods=['POST'])
def editar_colaborador(id):
    if request.method =='POST':
        c = request.form
        abreviatura = c['abreviatura']
        colaborador = c['colaborador']
        descripcion = c['descripcion']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE colaborador "
                    "SET abreviatura = %s, "
                    "colaborador = %s, "
                    "descripcion = %s "
                    "WHERE id = %s;", (abreviatura, colaborador, descripcion, int(id)))
        mysql.connection.commit()
        flash('Colaborador actualizado satisfactoriamente')
    return listar_colaboradores()


@app.route('/editar/equipo<id>', methods=['POST'])
def editar_equipo(id):
    if request.method =='POST':
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
        cur.execute("UPDATE equipoMarvel "
                    "SET pagina = %s, equipo = %s, nombreEspanol = %s, numeroIntegrantes = %s, paisOrigen = %s, "
                    "departamento = %s, lider = %s, base = %s, primeraAparicion = %s, fecha = %s, "
                    "historia = %s, colaboradores = %s, aliados = %s, enemigos = %s, argumentosEsenciales = %s "
                    "WHERE id = %s;", (pagina, equipo, nombreEnEspanol, numeroIntegrantes, paisOrigen,
                                             departamento, lider, base, primeraAparicion, fecha,
                                             historia, colaboradores, aliados, enemigos, argumentosEsenciales, int(id)))
        mysql.connection.commit()
        flash('Equipo actualizado satisfactoriamente')
    return listar_equipos()


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
    cur.execute('''SELECT * FROM revistaMarvel ORDER BY pagina;''')
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
        return redirect(url_for('listar_colaboradores'))
    else:
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
        return redirect(url_for('listar_revistas'))
    else:
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
        return redirect(url_for('listar_equipos'))
    else:
        return render_template('agregar_equipo.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=3000, debug=True)