"""
Serviço de usuários - Camada de lógica de negócio
Responsável por implementar as regras de negócio e validações
"""
from typing import List, Optional, Dict, Any
from src.models.user import User
from src.repositories.user_repository import UserRepository


class UserService:
    """Serviço para lógica de negócio de usuários"""
    
    def __init__(self):
        self.user_repository = UserRepository()
    
    def get_all_users(self) -> List[Dict[str, Any]]:
        """Retorna todos os usuários como dicionários"""
        users = self.user_repository.get_all()
        return [user.to_dict() for user in users]
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Retorna um usuário pelo ID"""
        user = self.user_repository.get_by_id(user_id)
        return user.to_dict() if user else None
    
    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cria um novo usuário com validações de negócio
        
        Args:
            user_data: Dicionário com os dados do usuário
            
        Returns:
            Dicionário com os dados do usuário criado
            
        Raises:
            ValueError: Se os dados são inválidos ou já existem
        """
        # Validações de negócio
        self._validate_user_data(user_data)
        
        # Verificar se username já existe
        if self.user_repository.exists_by_username(user_data['username']):
            raise ValueError(f"Nome de usuário '{user_data['username']}' já existe")
        
        # Verificar se email já existe
        if self.user_repository.exists_by_email(user_data['email']):
            raise ValueError(f"Email '{user_data['email']}' já está em uso")
        
        # Criar o usuário
        user = User(
            username=user_data['username'],
            email=user_data['email']
        )
        
        created_user = self.user_repository.create(user)
        return created_user.to_dict()
    
    def update_user(self, user_id: int, user_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Atualiza um usuário existente
        
        Args:
            user_id: ID do usuário a ser atualizado
            user_data: Dados para atualização
            
        Returns:
            Dicionário com os dados do usuário atualizado ou None se não encontrado
            
        Raises:
            ValueError: Se os dados são inválidos ou já existem
        """
        user = self.user_repository.get_by_id(user_id)
        if not user:
            return None
        
        # Validar apenas os campos que estão sendo atualizados
        if 'username' in user_data:
            self._validate_username(user_data['username'])
            # Verificar se o novo username já existe (exceto para o próprio usuário)
            existing_user = self.user_repository.get_by_username(user_data['username'])
            if existing_user and existing_user.id != user_id:
                raise ValueError(f"Nome de usuário '{user_data['username']}' já existe")
            user.username = user_data['username']
        
        if 'email' in user_data:
            self._validate_email(user_data['email'])
            # Verificar se o novo email já existe (exceto para o próprio usuário)
            existing_user = self.user_repository.get_by_email(user_data['email'])
            if existing_user and existing_user.id != user_id:
                raise ValueError(f"Email '{user_data['email']}' já está em uso")
            user.email = user_data['email']
        
        updated_user = self.user_repository.update(user)
        return updated_user.to_dict()
    
    def delete_user(self, user_id: int) -> bool:
        """
        Remove um usuário
        
        Args:
            user_id: ID do usuário a ser removido
            
        Returns:
            True se o usuário foi removido, False se não foi encontrado
        """
        user = self.user_repository.get_by_id(user_id)
        if not user:
            return False
        
        self.user_repository.delete(user)
        return True
    
    def _validate_user_data(self, user_data: Dict[str, Any]) -> None:
        """Valida os dados completos do usuário"""
        if not user_data.get('username'):
            raise ValueError("Nome de usuário é obrigatório")
        
        if not user_data.get('email'):
            raise ValueError("Email é obrigatório")
        
        self._validate_username(user_data['username'])
        self._validate_email(user_data['email'])
    
    def _validate_username(self, username: str) -> None:
        """Valida o nome de usuário"""
        if len(username) < 3:
            raise ValueError("Nome de usuário deve ter pelo menos 3 caracteres")
        
        if len(username) > 80:
            raise ValueError("Nome de usuário deve ter no máximo 80 caracteres")
        
        if not username.replace('_', '').replace('-', '').isalnum():
            raise ValueError("Nome de usuário deve conter apenas letras, números, _ e -")
    
    def _validate_email(self, email: str) -> None:
        """Valida o formato do email"""
        if '@' not in email or '.' not in email:
            raise ValueError("Formato de email inválido")
        
        if len(email) > 120:
            raise ValueError("Email deve ter no máximo 120 caracteres")

