from abc import ABC, abstractmethod
from typing import List, Optional
from django.contrib.auth.models import User
from Sellerprofile.models import Seller
from community_main_page.models import products, ProductUser


# ==== USER REPOSITORY ====
class IUserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def exists_by_username(self, username: str) -> bool:
        pass


class DjangoUserRepository(IUserRepository):
    def get_by_id(self, user_id: int) -> Optional[User]:
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def exists_by_username(self, username: str) -> bool:
        return User.objects.filter(username=username).exists()


# ==== SELLER REPOSITORY ====
class ISellerRepository(ABC):
    @abstractmethod
    def is_seller(self, user: User) -> bool:
        pass

    @abstractmethod
    def get_by_user(self, user: User) -> Optional[Seller]:
        pass


class DjangoSellerRepository(ISellerRepository):
    def is_seller(self, user: User) -> bool:
        return Seller.objects.filter(user_info=user).exists()

    def get_by_user(self, user: User) -> Optional[Seller]:
        return Seller.objects.filter(user_info=user).first()


# ==== PRODUCT REPOSITORY ====
class IProductRepository(ABC):
    @abstractmethod
    def get_favorites_by_user(self, user: User) -> List[products]:
        pass


class DjangoProductRepository(IProductRepository):
    def get_favorites_by_user(self, user: User) -> List[products]:
        favorite_products = ProductUser.objects.filter(user_info=user)
        product_ids = [fav.product_info_id for fav in favorite_products]
        return products.objects.filter(pk__in=product_ids)
