from flask import Flask, render_template

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Configuración de la aplicación
    app.config.from_object('config.Config')

    # Registrar los Blueprints
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Configurar la carpeta de plantillas
    app.template_folder = 'templates'


    # Crear la carpeta de subida si no existe
    #from os import path, mkdir
    #upload_folder = path.join(app.instance_path, app.config['UPLOAD_FOLDER'])
    #if not path.exists(upload_folder):
        #mkdir(upload_folder)

    return app
