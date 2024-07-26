from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
  message = ''
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    # check password integrity
    if password == confirm_password:
      if User.objects.filter(email=email).exists():
        messages.info(request, 'Email Already Used')
        message = 'email already used'
        # return redirect('register')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'Username Already Used')
        message = 'username already used'
        # return redirect('register')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
      
    else:
      messages.info(request, 'password not the same')
      message = "password not the same"
      # return redirect('register')
    return render(request, 'register.html', {'message':  message})
  else:
    return render(request, 'register.html')
  
def login(request):
  return render(request, 'login.html')