"""
Configuração dos testes
"""
import pytest
import sys
import os

# Adicionar o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.main import create_app
from src.models.user import db


@pytest.fixture
def app():
    """Fixture para criar a aplicação de teste"""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    """Fixture para criar o cliente de teste"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Fixture para criar o runner de comandos CLI"""
    return app.test_cli_runner()

