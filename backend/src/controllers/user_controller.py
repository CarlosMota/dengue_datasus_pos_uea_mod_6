"""
Controlador de usuários - Camada de apresentação
Responsável por lidar com requisições HTTP e respostas
"""
from flask import Blueprint, jsonify, request
from src.services.user_service import UserService


class UserController:
    """Controlador para endpoints de usuários"""
    
    def __init__(self):
        self.user_service = UserService()
        self.blueprint = Blueprint('user', __name__)
        self._register_routes()
    
    def _register_routes(self):
        """Registra todas as rotas do controlador"""
        self.blueprint.add_url_rule('/users', 'get_users', self.get_users, methods=['GET'])
        self.blueprint.add_url_rule('/users', 'create_user', self.create_user, methods=['POST'])
        self.blueprint.add_url_rule('/users/<int:user_id>', 'get_user', self.get_user, methods=['GET'])
        self.blueprint.add_url_rule('/users/<int:user_id>', 'update_user', self.update_user, methods=['PUT'])
        self.blueprint.add_url_rule('/users/<int:user_id>', 'delete_user', self.delete_user, methods=['DELETE'])
    
    def get_users(self):
        """GET /users - Retorna todos os usuários"""
        try:
            users = self.user_service.get_all_users()
            return jsonify({
                'success': True,
                'data': users,
                'message': 'Usuários recuperados com sucesso'
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e),
                'message': 'Erro ao recuperar usuários'
            }), 500
    
    def create_user(self):
        """POST /users - Cria um novo usuário"""
        try:
            # Validar se o corpo da requisição é JSON
            if not request.is_json:
                return jsonify({
                    'success': False,
                    'error': 'Content-Type deve ser application/json',
                    'message': 'Dados inválidos'
                }), 400
            
            data = request.get_json()
            
            # Validar se os dados foram fornecidos
            if not data:
                return jsonify({
                    'success': False,
                    'error': 'Corpo da requisição vazio',
                    'message': 'Dados são obrigatórios'
                }), 400
            
            user = self.user_service.create_user(data)
            return jsonify({
                'success': True,
                'data': user,
                'message': 'Usuário criado com sucesso'
            }), 201
            
        except ValueError as e:
            return jsonify({
                'success': False,
                'error': str(e),
                'message': 'Dados inválidos'
            }), 400
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e),
                'message': 'Erro interno do servidor'
            }), 500
    
    def get_user(self, user_id):
        """GET /users/<id> - Retorna um usuário específico"""
        try:
            user = self.user_service.get_user_by_id(user_id)
            
            if not user:
                return jsonify({
                    'success': False,
                    'error': f'Usuário com ID {user_id} não encontrado',
                    'message': 'Usuário não encontrado'
                }), 404
            
            return jsonify({
                'success': True,
                'data': user,
                'message': 'Usuário recuperado com sucesso'
            }), 200
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e),
                'message': 'Erro ao recuperar usuário'
            }), 500
    
    def update_user(self, user_id):
        """PUT /users/<id> - Atualiza um usuário existente"""
        try:
            # Validar se o corpo da requisição é JSON
            if not request.is_json:
                return jsonify({
                    'success': False,
                    'error': 'Content-Type deve ser application/json',
                    'message': 'Dados inválidos'
                }), 400
            
            data = request.get_json()
            
            # Validar se os dados foram fornecidos
            if not data:
                return jsonify({
                    'success': False,
                    'error': 'Corpo da requisição vazio',
                    'message': 'Dados são obrigatórios'
                }), 400
            
            user = self.user_service.update_user(user_id, data)
            
            if not user:
                return jsonify({
                    'success': False,
                    'error': f'Usuário com ID {user_id} não encontrado',
                    'message': 'Usuário não encontrado'
                }), 404
            
            return jsonify({
                'success': True,
                'data': user,
                'message': 'Usuário atualizado com sucesso'
            }), 200
            
        except ValueError as e:
            return jsonify({
                'success': False,
                'error': str(e),
                'message': 'Dados inválidos'
            }), 400
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e),
                'message': 'Erro interno do servidor'
            }), 500
    
    def delete_user(self, user_id):
        """DELETE /users/<id> - Remove um usuário"""
        try:
            success = self.user_service.delete_user(user_id)
            
            if not success:
                return jsonify({
                    'success': False,
                    'error': f'Usuário com ID {user_id} não encontrado',
                    'message': 'Usuário não encontrado'
                }), 404
            
            return jsonify({
                'success': True,
                'message': 'Usuário removido com sucesso'
            }), 200
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e),
                'message': 'Erro ao remover usuário'
            }), 500

