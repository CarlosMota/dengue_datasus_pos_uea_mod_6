"""
Repositório de usuários - Camada de acesso aos dados
Responsável por todas as operações de banco de dados relacionadas aos usuários
"""
from typing import List, Optional
from src.models.user import User, db


class UserRepository:
    """Repositório para operações de dados de usuários"""
    
    @staticmethod
    def get_all() -> List[User]:
        """Retorna todos os usuários"""
        return User.query.all()
    
    @staticmethod
    def get_by_id(user_id: int) -> Optional[User]:
        """Retorna um usuário pelo ID"""
        return User.query.get(user_id)
    
    @staticmethod
    def get_by_username(username: str) -> Optional[User]:
        """Retorna um usuário pelo nome de usuário"""
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def get_by_email(email: str) -> Optional[User]:
        """Retorna um usuário pelo email"""
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def create(user: User) -> User:
        """Cria um novo usuário"""
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def update(user: User) -> User:
        """Atualiza um usuário existente"""
        db.session.commit()
        return user
    
    @staticmethod
    def delete(user: User) -> None:
        """Remove um usuário"""
        db.session.delete(user)
        db.session.commit()
    
    @staticmethod
    def exists_by_username(username: str) -> bool:
        """Verifica se existe um usuário com o nome de usuário fornecido"""
        return User.query.filter_by(username=username).first() is not None
    
    @staticmethod
    def exists_by_email(email: str) -> bool:
        """Verifica se existe um usuário com o email fornecido"""
        return User.query.filter_by(email=email).first() is not None

