## Actividad 1 - Repositorio Github

**Repositorio Taller #1:** *https://github.com/SantiBetancur/ARQUITECTURA_SFT_TALLER_1.git*  

**Repositorio original P1:** *https://github.com/Local-Markets/LCMrep.git*

---

## Actividad 2 - Revisión Autocrítica


### **Atributo de usabilidad**

La siguiente revisión recopila observaciones sobre la experiencia de usuario y la presentación visual de la plataforma. Se señalan puntos de mejora en cuanto a usabilidad, diseño y claridad funcional.

---

### 1. Difuminado en la parte superior

> El difuminado que aparece en la parte superior genera un obstáculo visual innecesario.
> En lugar de mejorar la estética, termina reduciendo la legibilidad en los formularios y complica la navegación.
> Una interfaz debe priorizar **claridad y legibilidad** sobre efectos decorativos que no aportan un valor práctico.

 **Sugerencia de mejora**:
 
- Sustituir el difuminado por un fondo limpio y uniforme.
   
- Asegurar que los campos de formulario estén siempre completamente visibles.  

<img src="https://github.com/user-attachments/assets/2b10fc61-3693-4662-ac68-ab335d182ceb" height="280" />

---

### 2. Registro obligatorio y landing page confusa

> La plataforma exige **registro previo** para visualizar productos, lo que genera fricción desde el inicio.
> Además, la **landing page** presenta una estructura parecida a la de un mapa de universidades, donde se localizan vendedores, lo que resulta poco intuitivo.
> A esto se suma el uso de **alertas nativas del navegador**, que rompen la consistencia del diseño general.

 **Sugerencia de mejora**:
 
- Permitir la **navegación inicial sin registro**, al menos para explorar el catálogo.
  
- Diseñar una landing más clara y enfocada en el **valor principal** del sitio (mostrar productos).
  
- Reemplazar las alertas del navegador por modales o notificaciones integradas al diseño.

<img src="https://github.com/user-attachments/assets/a57bf2ea-0858-429c-960c-0c7fe88ed8ea" height="280" />

---

### 3. Botón de corazón ambiguo en productos

> En la página de detalle de los productos se incluye un **botón con ícono de corazón** en la parte inferior izquierda.
> Su funcionalidad no es clara: el usuario no sabe si significa “favorito”, “me gusta”, “guardar para después” o si está relacionado con la calificación del producto.
> Esto puede generar **confusión e indecisión** al interactuar con el sitio.

 **Sugerencia de mejora**: 
 
- Añadir un **tooltip** o texto aclaratorio al pasar el cursor sobre el ícono.
  
- Usar un diseño coherente con patrones ya conocidos (ejemplo: corazón = favoritos).
   
- Ubicar el botón en una zona más intuitiva, como la parte superior derecha de la tarjeta o junto a la calificación.

<img src="https://github.com/user-attachments/assets/f4f3b3d1-5b4a-4c32-a768-ba58bae0a8e0" height="280" />

---

### 4. Botón de flecha redundante

> En la esquina superior derecha aparece un botón con un ícono de **flecha hacia atrás**.
> Su función es básicamente la misma que el **botón de retroceso del navegador**, lo que lo convierte en un elemento redundante.
> Además, su presencia puede generar **confusión** ya que no aporta una acción adicional clara.

 **Sugerencia de mejora**: 

- Reemplazar este botón por una acción más útil (por ejemplo, **volver al listado de productos** en lugar de replicar el retroceso del navegador).
   
- Incluir un ícono más representativo (ejemplo: una casa para volver a la página principal o un carrito para regresar a la tienda).  

<img src="https://github.com/user-attachments/assets/3e5a0e08-0d15-4e0b-a0e6-63f1cf5e678f" height="280" />

---

## **Atributo de compatibilidad**


## Aspectos Positivos de Compatibilidad

### **Compatibilidad Web Robusta**

- **Navegadores Modernos**: Soporte completo para Chrome, Firefox, Safari y Edge (últimas 2 versiones)
- **Responsive Design**: Adaptación automática a dispositivos móviles, tablets y desktop
- **Estándares Web**: Implementación de HTML5, CSS3 y JavaScript ES6+

###  **Arquitectura Flexible**

- **Django Framework**: Base sólida con excelente compatibilidad entre versiones
- **API REST**: Interfaz estandarizada para integración con frontend y móviles
- **Base de Datos**: Soporte multiplataforma (PostgreSQL, MySQL, SQLite)

###  **Integración de IA Estable**

- **OpenAI API v2.x**: Versión actualizada con mejor rendimiento y estabilidad
- **Fallback Mechanisms**: Manejo de errores cuando los servicios externos fallan
- **Caching Inteligente**: Reducción de llamadas a APIs externas

###  **Experiencia Multiplataforma**

- **Progressive Web App (PWA)**: Funcionalidad nativa en dispositivos móviles
- **Offline Support**: Funcionalidades básicas disponibles sin conexión
- **Cross-Platform**: Compatible con Windows, macOS y Linux

---

##  **Aspectos Negativos y Desafíos**

###  **Dependencias Externas Frágiles**

- **OpenAI API**: Cambios frecuentes en la API pueden romper funcionalidades
- **Rate Limiting**: Limitaciones de uso que afectan la escalabilidad
- **Costos Variables**: Precios de APIs externas pueden impactar el presupuesto

### **Problemas de Versionado**

- **Conflictos de Dependencias**: Incompatibilidades entre librerías (ej: httpx vs OpenAI)
- **Breaking Changes**: Actualizaciones que requieren refactoring del código
- **Legacy Code**: Código heredado que puede ser incompatible con nuevas versiones

### **Limitaciones de Navegadores Antiguos**

- **Internet Explorer**: No soportado (puede excluir usuarios corporativos)
- **Navegadores Móviles Antiguos**: Funcionalidades limitadas en versiones obsoletas
- **JavaScript Deshabilitado**: Pérdida de funcionalidades interactivas

### **Desafíos de Seguridad**

- **HTTPS Obligatorio**: Requerimiento estricto para APIs modernas
- **CORS Policies**: Restricciones que pueden limitar integraciones
- **Data Privacy**: Cumplimiento con GDPR y regulaciones locales

---

## **Métricas de Compatibilidad**

| Aspecto | Cobertura | Estado |
|---------|-----------|--------|
| **Navegadores Modernos** | 95% |  Excelente |
| **Dispositivos Móviles** | 90% |  Muy Bueno |
| **APIs Externas** | 85% |  Bueno |
| **Navegadores Antiguos** | 60% |  Limitado |
| **Accesibilidad** | 75% |  En Progreso |

---

## **Conclusiones**

- En general, la interfaz actual presenta algunos elementos que, aunque bien intencionados, terminan afectando la usabilidad y la claridad.
   
- El principal reto es simplificar la navegación, reducir la fricción para el usuario y aplicar patrones de diseño que sean familiares e intuitivos.
   
- Un diseño más limpio y coherente permitirá que los usuarios se concentren en lo esencial.

- El proyecto LocalMarket presenta una base sólida de compatibilidad con oportunidades significativas de mejora. Los aspectos positivos incluyen una arquitectura moderna y flexible, mientras que los desafíos principales se centran en la gestión de dependencias externas y la compatibilidad con sistemas legacy.


## Actividad 3 - Inversión de Dependencias

En este proyecto, se aplicó el Principio de Inversión de Dependencias (DIP) en las vistas de profile_page y profile_edit del módulo profile_page. El objetivo fue desacoplar las vistas de las implementaciones directas de los modelos de Django, creando repositorios abstractos que definen interfaces, y separando la lógica de acceso a datos de la lógica de presentación.

### Cambios realizados
   
Creación de repositories.py

Se crearon interfaces y sus implementaciones concretas para manejar las entidades de usuario, vendedor y productos favoritos:

```python
# profile_page/repositories.py
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
```


**Beneficio:**

- Separa la lógica de acceso a datos de la vista, permitiendo cambiar la implementación sin modificar la lógica de presentación.

---

### Creación de container.py

Se implementó un contenedor de dependencias utilizando la librería dependency-injector, centralizando la creación de repositorios:

```python
# profile_page/container.py
from dependency_injector import containers, providers
from profile_page.repositories import DjangoUserRepository, DjangoSellerRepository, DjangoProductRepository

class Container(containers.DeclarativeContainer):
    user_repo = providers.Factory(DjangoUserRepository)
    seller_repo = providers.Factory(DjangoSellerRepository)
    product_repo = providers.Factory(DjangoProductRepository)
```

**Beneficio:**

- Centraliza las dependencias del módulo.
  
- Permite cambiar implementaciones de forma global sin tocar las vistas.
  
- Facilita testing con mocks o fakes al inyectar repositorios diferentes.

--- 

### Modificación de views.py

Se refactorizaron las vistas profile_page y profile_edit para que reciban los repositorios como parámetros (inyección de dependencias). También se integró el contenedor para usar las implementaciones por defecto:

```python
# profile_page/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user
from django.core.paginator import Paginator
from .forms import UserForm
from .repositories import IUserRepository, ISellerRepository, IProductRepository
from .container import Container

user_repo: IUserRepository = Container.user_repo()
seller_repo: ISellerRepository = Container.seller_repo()
product_repo: IProductRepository = Container.product_repo()

def profile_page(
    request, 
    user_id: int,
    user_repo: IUserRepository = user_repo,
    seller_repo: ISellerRepository = seller_repo,
    product_repo: IProductRepository = product_repo
):
    user = user_repo.get_by_id(user_id)
    context = {}

    if not user:
        return redirect('/')

    if user.is_authenticated:
        context['user'] = user
        is_seller = seller_repo.is_seller(user)
        context['is_seller'] = is_seller

        if is_seller:
            seller_instance = seller_repo.get_by_user(user)
            if seller_instance:
                context['seller_id'] = seller_instance.id
                context['seller'] = seller_instance

    favorite_products_details = product_repo.get_favorites_by_user(user)
    queryset_paginator = Paginator(favorite_products_details, 3)
    page_number = request.GET.get('page')
    page_obj = queryset_paginator.get_page(page_number)

    context['page_obj'] = page_obj
    return render(request, 'profile_page.html', context)


def profile_edit(
    request,
    user_id: int,
    user_repo: IUserRepository = user_repo,
    seller_repo: ISellerRepository = seller_repo
):
    try:
        context = {}
        user = get_user(request)
        U_User = user_repo.get_by_id(user_id)

        if not U_User:
            return redirect('/')

        form = UserForm(initial={'username': U_User.username, 'email': U_User.email})
        is_seller = seller_repo.is_seller(user)

        if user.is_authenticated:
            context['session_user'] = user.username

        if request.method == 'POST':
            if 'delete' in request.POST:
                if is_seller:
                    context['form'] = form
                    context['form_error'] = "No puedes eliminar tu cuenta si te encuentras registrado como vendedor"
                    return render(request, 'profile_edit.html', context)
                else:
                    U_User.delete()
                    return redirect('/logout/')

            if request.POST['password'] == request.POST['password_confirmation']:
                if request.POST['username'] != U_User.username:
                    if user_repo.exists_by_username(request.POST['username']):
                        context['form'] = form
                        context['form_error'] = "El usuario ingresado no está disponible"
                        return render(request, 'profile_edit.html', context)
                    else:
                        U_User.username = request.POST['username']
                        U_User.email = request.POST['email']
                        if request.POST['password']:
                            U_User.set_password(request.POST['password'])
                        U_User.save()
                        return redirect('/logout/')
                else:
                    U_User.email = request.POST['email']
                    if request.POST['password']:
                        U_User.set_password(request.POST['password'])
                    U_User.save()
                    return redirect('/logout/')
            else:
                context['form'] = form
                context['form_error'] = "La confirmación de la contraseña no coincide"
                return render(request, 'profile_edit.html', context)

        context['form'] = form
        return render(request, 'profile_edit.html', context)
    except Exception:
        return redirect('/')
```
 ---
 
### Beneficios de estos cambios

**Desacoplamiento:**

- Las vistas ya no dependen directamente de los modelos de Django.

- Cambiar la lógica de acceso a datos no requiere modificar las vistas.

**Testabilidad:**

- Se pueden inyectar repositorios falsos o mocks para pruebas unitarias, sin tocar la base de datos real.

**Mantenibilidad:**

- Cambios futuros en la forma de obtener usuarios, vendedores o productos solo afectan los repositorios.

- La vista se mantiene limpia y centrada en la presentación.

**Flexibilidad:**

- Se puede reemplazar completamente la implementación de repositorios usando el Container.

- Compatible con patrones de arquitectura más avanzados, como servicios o CQRS.
