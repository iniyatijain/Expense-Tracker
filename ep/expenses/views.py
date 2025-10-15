from django.shortcuts import render, redirect
from .models import budget, expense, category
from .form import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Your account has been created. Please login to proceed CUTIE!')
            return redirect('homepage')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            messages.success(request, f'You have now logged in CUTIE')
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def homepage(request):
    curr_month = request.GET.get('month')
    if not curr_month:
        curr_month = timezone.now().strftime("%b").upper()

    budgetvalue = budget.objects.filter(user=request.user, month=curr_month).first()
    print(budgetvalue)
    
    month_number = datetime.strptime(curr_month, "%b").month
    viewexpense = expense.objects.filter(user=request.user, expense_date__month=month_number)
    
    getexpenseval = expense.objects.filter(user=request.user, expense_date__month=month_number)
    total_spent = sum(e.expense_amount for e in getexpenseval)

    month_list = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    
    
   
    context = {
        'budgetvalue':budgetvalue,
        'viewexpense' :viewexpense,
        'curuserexp' : getexpenseval,
        'total_spent': total_spent,
        'month_list' : month_list,
        'curr_month' : curr_month
    }
    return render(request, 'homepage.html',context)

@login_required
def budget_view(request):
    if request.method == "POST":
        print("POST DATA:", request.POST)
        curr_month = request.POST.get('month')
        print(curr_month)
        if not curr_month:
            curr_month = timezone.now().strftime("%b").upper()
        budget_amount = request.POST['budget_amount']
        planned_amount = request.POST['planned_amount']
        
        budget.objects.update_or_create(
        user=request.user,
        month=curr_month,
        defaults={
            'budget_amount': budget_amount,
            'planned_amount': planned_amount
        }
        )
        return redirect(f'/?month={curr_month}')
    
    return render(request, 'homepage.html')

@login_required
def addexpensepage(request):
    categories = category.objects.all()
    return render(request, 'addexpense.html', {'categories': categories})

@login_required
def addexpense_view(request):
    #categories = category.objects.all()
    if request.method == "POST":
        datevalue = request.POST['date']
        amountvalue = request.POST['amount']
        categoryvalue = request.POST['category']
        descvalue = request.POST['description']
        
        categoryid = category.objects.get(id=categoryvalue)
        expense.objects.create(
        user=request.user,
        expense_amount=amountvalue,
        expense_date= datevalue,
        expense_description=descvalue,
        category=categoryid
        )
        return redirect('addexpense')

    return render(request, 'homepage.html')

@login_required
def editexpense_view(request, id):
    categories = category.objects.all()
    rowid = expense.objects.get(id=id)
    
    if request.method == "POST":
        datevalue = request.POST['date']
        amountvalue = request.POST['amount']
        categoryvalue = request.POST['category']
        descvalue = request.POST['description']

        categoryid = category.objects.get(id=categoryvalue)
        
        rowid.expense_amount=amountvalue
        rowid.expense_date= datevalue
        rowid.expense_description=descvalue
        rowid.category=categoryid
        rowid.save()
        return redirect('homepage')
    context = {
        'categories': categories,
        'rowid': rowid
    }
    return render(request, 'editexpense.html', context)

@login_required
def deleteexpense_view(request, id):
    rowid = expense.objects.get(id=id)
    rowid.delete()
    return redirect('homepage')