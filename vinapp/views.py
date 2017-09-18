from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from vinapp.models import User,UserProfile
from vinapp.forms import UserForm 
from vinapp.forms import UserProfileForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def index(request):
    request.session.set_test_cookie()
    return render(request,"vinapp/index.html")


def home(request):
    return render(request,"vinapp/index.html")

from vinapp.forms import UserForm
from vinapp.forms import UserProfileForm

def register(request):


    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Note that we make use of both UserForm and UserProfileForm
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user


            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']


            profile.save()

            registered = True
            email=user.email
            username=request.POST.get('username')

            from django.core.mail import EmailMessage

            email = EmailMessage('Vineel Saying Thank you ', 'You are registered with Vineel\'s site as ' + username,
                                 to=[email])
            email.send()


        else:
            print (user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'vinapp/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )




from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

@never_cache
def login(request):
    global username
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                auth_login(request,user)
                email=user.email
                #print (email)
                from django.core.mail import EmailMessage

                email = EmailMessage('Vineel Welcomes you ', 'You are logged into Vineel\'s site as '+username, to=[email])
                email.send()

                return render(request,'vinapp/loggedin.html')
                
            else:
                 return HttpResponse('Your account is disabled')
        else:

             print('Invalid login details:{0},{1}'.format(username,password))
             return render(request,'vinapp/invalid.html')
    else:

        return render(request,"vinapp/login.html",{})



@login_required(login_url='/vineel/login')
def logout(request):
    # Since we know the user is logged in, we can now just log them out.

    auth_logout(request)


    return HttpResponseRedirect("/vineel/login")
