from dependency_injector import containers, providers
from .repositories import (
    IUserRepository, DjangoUserRepository,
    ISellerRepository, DjangoSellerRepository,
    IProductRepository, DjangoProductRepository,
)

class Container(containers.DeclarativeContainer):
    user_repo = providers.Singleton(DjangoUserRepository)
    seller_repo = providers.Singleton(DjangoSellerRepository)
    product_repo = providers.Singleton(DjangoProductRepository)
