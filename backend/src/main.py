import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.controllers.user_controller import UserController
from src.config import config


def create_app(config_name=None):
    """Factory function para criar a aplicação Flask"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
    
    # Carregar configurações
    app.config.from_object(config[config_name])
    
    # Habilitar CORS
    CORS(app, origins=app.config['CORS_ORIGINS'])
    
    # Inicializar banco de dados
    db.init_app(app)
    
    # Registrar controladores
    user_controller = UserController()
    app.register_blueprint(user_controller.blueprint, url_prefix='/api')
    
    # Criar tabelas do banco de dados
    with app.app_context():
        db.create_all()
    
    # Rota para servir arquivos estáticos (frontend)
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        static_folder_path = app.static_folder
        if static_folder_path is None:
            return "Static folder not configured", 404

        if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
            return send_from_directory(static_folder_path, path)
        else:
            index_path = os.path.join(static_folder_path, 'index.html')
            if os.path.exists(index_path):
                return send_from_directory(static_folder_path, 'index.html')
            else:
                return "index.html not found", 404
    
    # Rota de health check
    @app.route('/health')
    def health_check():
        return {'status': 'healthy', 'message': 'API está funcionando'}, 200
    
    return app


# Criar a aplicação
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
