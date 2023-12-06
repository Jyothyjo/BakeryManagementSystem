from django import forms
from .models import Employee, Product, Customer, Order, InventoryItem, OrderItem

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class OrderItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)

        # Fetch Order IDs and corresponding Customer names
        order_choices = Order.objects.values_list('id', 'customer__name')
        # Assign these choices to the order field
        self.fields['order'].choices = order_choices

        # Fetch Product names
        product_choices = Product.objects.values_list('id', 'name')
        # Assign these choices to the product field
        self.fields['product'].choices = product_choices

    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))
