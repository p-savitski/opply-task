#       Required for Django monoapp strategy.
#       To import model class, use direct imports from the apps' models.
from .users import models as _users_models
from .orders import models as _orders_models
from .products import models as _products_models
