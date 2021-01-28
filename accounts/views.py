from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        signupPhone = request.POST['signupPhone']
        signupName = request.POST['signupName']  
        username = request.POST['username']  
        signupEmail = request.POST['signupEmail']      
        password1= request.POST['signupPassword1']
        password2= request.POST['signupPassword2']

        if signupPassword1 == signupPassword2:
            if User.objects.filter(username = username).exsists():
                massages.info(request, 'Username already exists!')

                return redirect('sign_up')
                elif User.objects.filter(email = email).exists():
                    messages.info(request, 'Email alreaddy exsists!')
                    return redirect('sign_up')
                else:
                    user = User.objects.create_user(username = username, password1 = password2, email = email , signupPhone = signupPhone,signupName = signupName )
                    user.save()
            else:
                messages.info(request, 'Password are not valid')
                return redirect('sign_up')
        else:
            return render(request,'accounts/singUp.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = auth.authenticate(username = username , password1 = password1)

        if user is not None:
            auth.sign_in(request, user)
            return redirect('../' + username)
        
        else:
            messages.info(request, 'Username or password invalid')
            return render('sign_in')
    else:
        return render(request, 'accounts/sign_in.html')

