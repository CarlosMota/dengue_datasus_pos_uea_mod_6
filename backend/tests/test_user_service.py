"""
Testes para o serviço de usuários
"""
import pytest
from src.services.user_service import UserService
from src.models.user import User, db


class TestUserService:
    """Testes para a classe UserService"""
    
    def setup_method(self):
        """Configuração executada antes de cada teste"""
        self.user_service = UserService()
    
    def test_create_user_success(self, app):
        """Teste de criação de usuário com sucesso"""
        with app.app_context():
            user_data = {
                'username': 'testuser',
                'email': 'test@example.com'
            }
            
            result = self.user_service.create_user(user_data)
            
            assert result['username'] == 'testuser'
            assert result['email'] == 'test@example.com'
            assert 'id' in result
    
    def test_create_user_duplicate_username(self, app):
        """Teste de criação de usuário com username duplicado"""
        with app.app_context():
            # Criar primeiro usuário
            user_data = {
                'username': 'testuser',
                'email': 'test1@example.com'
            }
            self.user_service.create_user(user_data)
            
            # Tentar criar segundo usuário com mesmo username
            user_data2 = {
                'username': 'testuser',
                'email': 'test2@example.com'
            }
            
            with pytest.raises(ValueError, match="Nome de usuário 'testuser' já existe"):
                self.user_service.create_user(user_data2)
    
    def test_create_user_duplicate_email(self, app):
        """Teste de criação de usuário com email duplicado"""
        with app.app_context():
            # Criar primeiro usuário
            user_data = {
                'username': 'testuser1',
                'email': 'test@example.com'
            }
            self.user_service.create_user(user_data)
            
            # Tentar criar segundo usuário com mesmo email
            user_data2 = {
                'username': 'testuser2',
                'email': 'test@example.com'
            }
            
            with pytest.raises(ValueError, match="Email 'test@example.com' já está em uso"):
                self.user_service.create_user(user_data2)
    
    def test_create_user_invalid_data(self, app):
        """Teste de criação de usuário com dados inválidos"""
        with app.app_context():
            # Username muito curto
            user_data = {
                'username': 'ab',
                'email': 'test@example.com'
            }
            
            with pytest.raises(ValueError, match="Nome de usuário deve ter pelo menos 3 caracteres"):
                self.user_service.create_user(user_data)
            
            # Email inválido
            user_data2 = {
                'username': 'testuser',
                'email': 'invalid-email'
            }
            
            with pytest.raises(ValueError, match="Formato de email inválido"):
                self.user_service.create_user(user_data2)
    
    def test_get_all_users(self, app):
        """Teste de recuperação de todos os usuários"""
        with app.app_context():
            # Criar alguns usuários
            user_data1 = {'username': 'user1', 'email': 'user1@example.com'}
            user_data2 = {'username': 'user2', 'email': 'user2@example.com'}
            
            self.user_service.create_user(user_data1)
            self.user_service.create_user(user_data2)
            
            users = self.user_service.get_all_users()
            
            assert len(users) == 2
            assert any(user['username'] == 'user1' for user in users)
            assert any(user['username'] == 'user2' for user in users)
    
    def test_get_user_by_id(self, app):
        """Teste de recuperação de usuário por ID"""
        with app.app_context():
            user_data = {'username': 'testuser', 'email': 'test@example.com'}
            created_user = self.user_service.create_user(user_data)
            
            result = self.user_service.get_user_by_id(created_user['id'])
            
            assert result is not None
            assert result['username'] == 'testuser'
            assert result['email'] == 'test@example.com'
    
    def test_get_user_by_id_not_found(self, app):
        """Teste de recuperação de usuário por ID inexistente"""
        with app.app_context():
            result = self.user_service.get_user_by_id(999)
            assert result is None
    
    def test_update_user(self, app):
        """Teste de atualização de usuário"""
        with app.app_context():
            # Criar usuário
            user_data = {'username': 'testuser', 'email': 'test@example.com'}
            created_user = self.user_service.create_user(user_data)
            
            # Atualizar usuário
            update_data = {'username': 'updateduser'}
            result = self.user_service.update_user(created_user['id'], update_data)
            
            assert result is not None
            assert result['username'] == 'updateduser'
            assert result['email'] == 'test@example.com'  # Email não mudou
    
    def test_delete_user(self, app):
        """Teste de remoção de usuário"""
        with app.app_context():
            # Criar usuário
            user_data = {'username': 'testuser', 'email': 'test@example.com'}
            created_user = self.user_service.create_user(user_data)
            
            # Remover usuário
            result = self.user_service.delete_user(created_user['id'])
            assert result is True
            
            # Verificar se foi removido
            user = self.user_service.get_user_by_id(created_user['id'])
            assert user is None
    
    def test_delete_user_not_found(self, app):
        """Teste de remoção de usuário inexistente"""
        with app.app_context():
            result = self.user_service.delete_user(999)
            assert result is False

