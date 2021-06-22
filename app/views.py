from django.shortcuts import render , redirect
from .forms import PostForms
from .models import *
from django.views.generic import ListView , DetailView , TemplateView
# u = User.objects.get(pk=user)
def profile(request,id):
    user = request.user.id
    print(user)
    all_post = Post.objects.filter(user=user)
    form = PostForms()
    if request.method=='POST':
        form = PostForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect("/profile/<int:id>/")   
    return render(request,'profile.html',{'form':form,'all_post':all_post})
    
def post_list(request):
    all_post = Post.objects.all()
    return render(request,'timeline.html',{'all_post':all_post})

class PublisherListView(ListView):
    model = User

class userDetailView(DetailView):
    model = User



from django.views.generic import ListView , DetailView , TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile

from django.contrib import messages

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'auth/profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'auth/profile-update.html'
    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None
        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)  