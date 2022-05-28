from django.contrib import admin
from django.urls import path, include
from main.views import index, add, edit, update, destroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('', include('auth_user.urls')),
    path('add', add, name='add'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', destroy, name='destroy'),
]
