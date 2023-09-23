from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # URLs para Municipio
    path('municipio/', views.MunicipioListView.as_view(), name='municipiolist'),
    path('municipio/<int:pk>/', views.MunicipioDetailView.as_view(), name='municipiodetail'),
    path('municipio/create/', views.MunicipioCreateView.as_view(), name='municipiocreate'),
    path('municipio/<int:pk>/update/',views. MunicipioUpdateView.as_view(), name='municipioupdate'),
    path('municipio/<int:pk>/delete/', views.MunicipioDeleteView.as_view(), name='municipiodelete'),

    # URLs para Departamento
    path('departamento/', views.DepartamentoListView.as_view(), name='departamentolist'),
    path('departamento/<int:pk>/', views.DepartamentoDetailView.as_view(), name='departamentodetail'),
    path('departamento/create/', views.DepartamentoCreateView.as_view(), name='departamentocreate'),
    path('departamento/<int:pk>/update/', views.DepartamentoUpdateView.as_view(), name='departamentoupdate'),
    path('departamento/<int:pk>/delete/', views.DepartamentoDeleteView.as_view(), name='departamentodelete'),

    # URLs para Pais
    path('pais/', views.PaisListView.as_view(), name='paislist'),
    path('pais/<int:pk>/', views.PaisDetailView.as_view(), name='paisdetail'),
    path('pais/create/', views.PaisCreateView.as_view(), name='paiscreate'),
    path('pais/<int:pk>/update/', views.PaisUpdateView.as_view(), name='paisupdate'),
    path('pais/<int:pk>/delete/', views.PaisDeleteView.as_view(), name='paisdelete'),
    
    path('login/', LoginView.as_view(template_name='registro/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='paislist'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    
    path('',views.home_view, name='base'),
    
    path('api/', include('catalogo.apiurls')),
]
