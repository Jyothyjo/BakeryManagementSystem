# bakery/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, Customer, Employee, InventoryItem, OrderItem
from .forms import ProductForm, OrderForm, CustomerForm, EmployeeForm, InventoryItemForm, OrderItemForm,LoginForm
from django.http import HttpResponse
# Views for CRUD operations
from django.contrib.auth import authenticate, login,logout


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products,'back_to_dashboard': True})


def product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_view.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})

def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_update.html', {'form': form, 'product': product})

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_view.html', {'product': product})

def order_list(request):
    orders = Order.objects.all()  # Retrieve all orders from the database
    return render(request, 'order_list.html', {'orders': orders,'back_to_dashboard': True})

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)  # Retrieve a specific order using the ID
    return render(request, 'order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        order_date = request.POST.get('order_date')
        customer_name = request.POST.get('customer')
        
        # Retrieve or create the Customer instance based on the name
        customer, created = Customer.objects.get_or_create(name=customer_name)
        
        # Create the order using the retrieved or created Customer instance
        new_order = Order.objects.create(order_date=order_date, customer=customer)
        
        return redirect('order_detail', order_id=new_order.id)
    else:
        return render(request, 'order_create.html')

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    # return render(request, 'order_.html', {'order': order})

# #customer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers,'back_to_dashboard': True})

def customer_view(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'customer_view.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()

    return render(request, 'customer_create.html', {'form': form})

def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect('customer_list')

#employee
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees,'back_to_dashboard': True})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_delete.html', {'employee': employee})

def inventoryitem_list(request):
    inventory_items = InventoryItem.objects.all()

    # Create a list of tuples containing (item, product_name)
    items_with_names = []
    for item in inventory_items:
        if hasattr(item, 'product') and hasattr(item.product, 'name'):
            product_name = item.product.name
        else:
            product_name = "Product Name Unavailable"
        items_with_names.append((item, product_name))

    return render(request, 'inventoryitem_list.html', {'items_with_names': items_with_names,'back_to_dashboard': True})

def inventoryitem_view(request, item_id):
    item = get_object_or_404(InventoryItem, pk=item_id)
    product_name = item.product.name if hasattr(item, 'product') and hasattr(item.product, 'name') else "Product Name Unavailable"
    return render(request, 'inventoryitem_detail.html', {'item': item, 'product_name': product_name})

def inventoryitem_create(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventoryitem_list')
    else:
        form = InventoryItemForm()
    return render(request, 'inventoryitem_create.html', {'form': form})


def inventoryitem_delete(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)
    item.delete()
    return redirect('inventoryitem_list')

def orderitem_list(request):
    order_items = OrderItem.objects.all()
    return render(request, 'orderitem_list.html', {'order_items': order_items,'back_to_dashboard': True})

def orderitem_detail(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    return render(request, 'orderitem_detail.html', {'item': order_item})

def orderitem_create(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orderitem_list')
        else:
            # Print form errors to debug
            print(form.errors)
    else:
        form = OrderItemForm()
    return render(request, 'orderitem_form.html', {'form': form})

def orderitem_confirm_delete(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    order_item.delete()
    return redirect('orderitem_list')
    return render(request, 'orderitem_confirm_delete.html', {'order_item': order_item})

def orderitem_update(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=order_item)
        if form.is_valid():
            form.save()
            return redirect('orderitem_detail', pk=pk)
    else:
        form = OrderItemForm(instance=order_item)
    return render(request, 'orderitem_form.html', {'form': form})

def bakery_home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard/')  # Redirect to dashboard upon successful login
    else:
        form = LoginForm()

    return render(request, 'bakery_home.html', {'form': form})

def dashboard_view(request):
    # Add your logic for the dashboard here
    return render(request, 'dashboard.html') # Replace 'dashboard.html' with your actual template name

def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout or modify as needed
    return redirect('/')