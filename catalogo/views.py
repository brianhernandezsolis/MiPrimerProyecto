from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Municipio, Pais, Departamento
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

#Pais
class PaisListView(ListView):
    model = Pais
    template_name = 'catalogo/pais/list.html'
    context_object_name = 'paises'
    paginate_by = 10  
    def get_queryset(self):
        query = self.request.GET.get('pais')
        if query:
            return Pais.objects.filter(Q(nombre__icontains=query))
        else:
            return Pais.objects.all()
    
    
class PaisDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'catalogo.view_pais'
    model = Pais
    template_name = 'catalogo/pais/detalles.html'
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('paislist'))

class PaisCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'catalogo.add_pais'
    model = Pais
    template_name = 'catalogo/pais/form.html'
    fields = ['nombre']
    success_url = reverse_lazy('paislist')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('paislist'))

class PaisUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'catalogo.change_pais'
    model = Pais
    template_name = 'catalogo/pais/form.html'
    fields = ['nombre']
    success_url = reverse_lazy('paislist')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('paislist'))

class PaisDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'catalogo.delete_pais'
    model = Pais
    template_name = 'catalogo/pais/eliminar.html'
    success_url = reverse_lazy('paislist')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('paislist'))
    
    

#Departamento
class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'catalogo/departamento/list.html'
    context_object_name = 'departamentos'
    paginate_by = 10  
    def get_queryset(self):
        query = self.request.GET.get('departamento')
        if query:
            return Departamento.objects.filter(Q(nombre__icontains=query)) 
        else:
            return Departamento.objects.all()
        
class DepartamentoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'catalogo.view_departamento'
    model = Departamento
    template_name = 'catalogo/departamento/detalles.html'
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('departamentolist'))

class DepartamentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'catalogo.add_departamento'
    model = Departamento
    template_name = 'catalogo/departamento/form.html'
    fields = ['nombre', 'pais']
    success_url = reverse_lazy('departamentolist')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('departamentolist'))

class DepartamentoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'catalogo.change_departamento'
    model = Departamento
    template_name = 'catalogo/departamento/form.html'
    fields = ['nombre', 'pais']
    success_url = reverse_lazy('departamentolist')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('departamentolist'))

class DepartamentoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'catalogo.delete_departamento'
    model = Departamento
    template_name = 'catalogo/departamento/eliminar.html'
    success_url = reverse_lazy('departamento_list')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('departamentolist'))
    

#Municipios
class MunicipioListView(ListView):
    model = Municipio
    template_name = 'catalogo/municipio/list.html'
    context_object_name = 'municipios'
    paginate_by = 10  
    def get_queryset(self):
        query = self.request.GET.get('municipio')
        if query:
            return Municipio.objects.filter(Q(nombre__icontains=query)) 
        else:
            return Municipio.objects.all()

class MunicipioDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'catalogo.view_municipio'
    model = Municipio
    template_name = 'catalogo/municipio/detalles.html'
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('municipiolist'))

class MunicipioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'catalogo.add_municipio'
    model = Municipio
    template_name = 'catalogo/municipio/form.html'
    fields = ['nombre', 'departamento']
    success_url = reverse_lazy('municipiolist')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('municipiolist'))

class MunicipioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'catalogo.change_municipio'
    model = Municipio
    template_name = 'catalogo/municipio/form.html'
    fields = ['nombre', 'departamento']
    success_url = reverse_lazy('municipiolist')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('municipiolist'))

class MunicipioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'catalogo.delete_municipio'
    model = Municipio
    template_name = 'catalogo/municipio/eliminar.html'
    success_url = reverse_lazy('municipiolist')
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('municipiolist'))


def home_view(request):
    return render(request, 'base.html')

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('paislist')
    template_name = 'registro/registro.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response