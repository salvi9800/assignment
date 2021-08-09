from django.db.models.fields import PositiveBigIntegerField
from django.forms import widgets
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from . form import ProfileCreateForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import CreateView
from . models import Profile

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import ProfileSerializer

# Create your views here.

def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Your have been registered. You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'user/register.html', {'form':form})


@login_required
def profile(request):
    if request.method=="POST":
        u_form= UserUpdateForm(request.POST, instance=request.user)
        p_form= ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('profile')


    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.profile)

    context= {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/profile.html', context)

class InfoCreateView(LoginRequiredMixin, CreateView):
    template_name= 'user/info_form.html'
    model= Profile
    form_class= ProfileCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CheckView(APIView):

    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        qs = Profile.objects.all()
        serializer = ProfileSerializer(qs, many= True)
        return Response(serializer.data)
        


