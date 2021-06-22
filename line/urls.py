
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include
from app import views
from app.views import PublisherListView , userDetailView , ProfileUpdateView , ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('timeline/',views.post_list),
    path('profile/<int:id>/',views.profile),
    path('userlist/',PublisherListView.as_view()),
    path('userlist/<int:pk>',userDetailView.as_view()),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),

        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

