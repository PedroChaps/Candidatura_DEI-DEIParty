from django.urls import path
from . import views

# URL configuration module
urlpatterns = [
    path("teste/", views.request_handler_teste),
    path("outro_teste/", views.request_handler_2o_teste),
    path("mais_um_teste/", views.html_bonito),
    path("beverages/<int:limit>/<int:offset>/", views.show_all_beverages),
    path("beverage/<int:id>/", views.show_beverage),
    path("remove_beverage/<int:id>/", views.warn_user),
    path("remove_beverage/<int:id>/confirm_removal", views.confirm_removal),
    path("update_beverage/<int:id>/<int:new_quantity>", views.update_beverage),
    path("error/", views.process_error)
    # path(path, view_function)
]

# map URLs to view functions
