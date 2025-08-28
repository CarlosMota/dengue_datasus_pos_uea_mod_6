"""
Testes para os endpoints da API
"""
import json
import pytest


class TestUserEndpoints:
    """Testes para os endpoints de usuários"""
    
    def test_health_check(self, client):
        """Teste do endpoint de health check"""
        response = client.get('/health')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
    
    def test_get_users_empty(self, client):
        """Teste de recuperação de usuários quando não há nenhum"""
        response = client.get('/api/users')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['data'] == []
    
    def test_create_user_success(self, client):
        """Teste de criação de usuário com sucesso"""
        user_data = {
            'username': 'testuser',
            'email': 'test@example.com'
        }
        
        response = client.post('/api/users', 
                             data=json.dumps(user_data),
                             content_type='application/json')
        
        assert response.status_code == 201
        
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['data']['username'] == 'testuser'
        assert data['data']['email'] == 'test@example.com'
        assert 'id' in data['data']
    
    def test_create_user_invalid_json(self, client):
        """Teste de criação de usuário com JSON inválido"""
        response = client.post('/api/users', 
                             data='invalid json',
                             content_type='text/plain')
        
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert data['success'] is False
    
    def test_create_user_empty_data(self, client):
        """Teste de criação de usuário com dados vazios"""
        response = client.post('/api/users', 
                             data=json.dumps({}),
                             content_type='application/json')
        
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert data['success'] is False
    
    def test_create_user_missing_fields(self, client):
        """Teste de criação de usuário com campos obrigatórios faltando"""
        user_data = {'username': 'testuser'}  # email faltando
        
        response = client.post('/api/users', 
                             data=json.dumps(user_data),
                             content_type='application/json')
        
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert data['success'] is False
        assert 'Email é obrigatório' in data['error']
    
    def test_get_user_by_id(self, client):
        """Teste de recuperação de usuário por ID"""
        # Primeiro criar um usuário
        user_data = {
            'username': 'testuser',
            'email': 'test@example.com'
        }
        
        create_response = client.post('/api/users', 
                                    data=json.dumps(user_data),
                                    content_type='application/json')
        
        created_user = json.loads(create_response.data)['data']
        user_id = created_user['id']
        
        # Agora recuperar o usuário
        response = client.get(f'/api/users/{user_id}')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['data']['id'] == user_id
        assert data['data']['username'] == 'testuser'
    
    def test_get_user_by_id_not_found(self, client):
        """Teste de recuperação de usuário por ID inexistente"""
        response = client.get('/api/users/999')
        assert response.status_code == 404
        
        data = json.loads(response.data)
        assert data['success'] is False
    
    def test_update_user(self, client):
        """Teste de atualização de usuário"""
        # Primeiro criar um usuário
        user_data = {
            'username': 'testuser',
            'email': 'test@example.com'
        }
        
        create_response = client.post('/api/users', 
                                    data=json.dumps(user_data),
                                    content_type='application/json')
        
        created_user = json.loads(create_response.data)['data']
        user_id = created_user['id']
        
        # Atualizar o usuário
        update_data = {'username': 'updateduser'}
        
        response = client.put(f'/api/users/{user_id}',
                            data=json.dumps(update_data),
                            content_type='application/json')
        
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['data']['username'] == 'updateduser'
        assert data['data']['email'] == 'test@example.com'  # Email não mudou
    
    def test_update_user_not_found(self, client):
        """Teste de atualização de usuário inexistente"""
        update_data = {'username': 'updateduser'}
        
        response = client.put('/api/users/999',
                            data=json.dumps(update_data),
                            content_type='application/json')
        
        assert response.status_code == 404
        
        data = json.loads(response.data)
        assert data['success'] is False
    
    def test_delete_user(self, client):
        """Teste de remoção de usuário"""
        # Primeiro criar um usuário
        user_data = {
            'username': 'testuser',
            'email': 'test@example.com'
        }
        
        create_response = client.post('/api/users', 
                                    data=json.dumps(user_data),
                                    content_type='application/json')
        
        created_user = json.loads(create_response.data)['data']
        user_id = created_user['id']
        
        # Remover o usuário
        response = client.delete(f'/api/users/{user_id}')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['success'] is True
        
        # Verificar se foi removido
        get_response = client.get(f'/api/users/{user_id}')
        assert get_response.status_code == 404
    
    def test_delete_user_not_found(self, client):
        """Teste de remoção de usuário inexistente"""
        response = client.delete('/api/users/999')
        assert response.status_code == 404
        
        data = json.loads(response.data)
        assert data['success'] is False
    
    def test_get_all_users_with_data(self, client):
        """Teste de recuperação de todos os usuários com dados"""
        # Criar alguns usuários
        users_data = [
            {'username': 'user1', 'email': 'user1@example.com'},
            {'username': 'user2', 'email': 'user2@example.com'}
        ]
        
        for user_data in users_data:
            client.post('/api/users', 
                       data=json.dumps(user_data),
                       content_type='application/json')
        
        # Recuperar todos os usuários
        response = client.get('/api/users')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['success'] is True
        assert len(data['data']) == 2
        
        usernames = [user['username'] for user in data['data']]
        assert 'user1' in usernames
        assert 'user2' in usernames

