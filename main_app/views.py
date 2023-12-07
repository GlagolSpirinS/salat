# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main_app.forms import ProductForm, CategoryForm
from main_app.models import Product, Category, Tag, Order

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main_app.forms import ProductForm, CategoryForm, TagForm, OrderForm
from main_app.models import Product, Category, Tag, Order


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog_home(request):
    return render(request, "blog-home.html")

def blog_post(request):
    return render(request, "blog-post.html")

def base(request):
    return render(request, "base.html")

def contact(request):
    return render(request, "contact.html")

def faq(request):
    return render(request, "faq.html")

def portfolio_item(request):
    return render(request, "portfolio-item.html")

def portfolio_overview(request):
    return render(request, "portfolio-overview.html")

def pricing(request):
    return render(request, "pricing.html")

def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products': products})

def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product.html', {'product': product})

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'  # Замените на ваш шаблон
    context_object_name = 'orders'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'
    paginate_by = 10  # Укажите желаемое количество элементов на странице


class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'
    context_object_name = 'tag'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag_form.html'
    success_url = reverse_lazy('tag_list')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag_form.html'
    success_url = reverse_lazy('tag_list')

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form.html'  # Замените на ваш шаблон
    success_url = '/success/'

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form.html'  # Замените на ваш шаблон
    success_url = '/success/'

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'  # Замените на ваш шаблон
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'  # Замените на ваш шаблон
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form.html'  # Замените на ваш шаблон
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form.html'  # Замените на ваш шаблон
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'  # Замените на ваш шаблон
    success_url = reverse_lazy('order_list')

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'  # Замените на ваш шаблон
    context_object_name = 'order'


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('tag_list')

# Order views
class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

# Tag views
class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'

class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'
    context_object_name = 'tag'

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag_form.html'
    success_url = reverse_lazy('tag_list')

class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag_form.html'
    success_url = reverse_lazy('tag_list')

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tag_confirm_delete.html'
    success_url = reverse_lazy('tag_list')