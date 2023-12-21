from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView, DetailView, FormView, ListView, DeleteView
from customer import forms
from owner.models import Products, Carts
from django.urls import reverse_lazy


class Registration(CreateView):
    form_class = forms.RegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_products = Products.objects.all()
        context["products"] = all_products
        return context


class ProductDetailsView(DetailView):
    template_name = "product.html"
    model = Products
    context_object_name = "product"
    pk_url_kwarg: "id"


class AddToCartView(FormView):
    template_name = 'addto-cart.html'
    form_class = forms.CartForm

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        product = Products.objects.get(id=id)
        return render(request, self.template_name, {"form": forms.CartForm(), "product": product})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        product = Products.objects.get(id=id)
        qty = request.POST.get("qty")
        user = request.user
        Carts.objects.create(product=product, qty=qty, user=user)
        return redirect("home")


class CartListView(ListView):
    model = Carts
    template_name = "cart.html"
    context_object_name = "carts"

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user).exclude(status="cancelled")


class CartRemoveView(DeleteView):
    model = Carts
    success_url = reverse_lazy('home')

    def get(selfrequest, *args, **kwargs):
        id = kwargs.get("pk")
        cart = Carts.objects.get(id=id)
        cart.delete()
        cart.status = "cancelled"
        return redirect("home")
