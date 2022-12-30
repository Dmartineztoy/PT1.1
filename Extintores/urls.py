from django.urls import path
from .views import CustomLoginView
from .forms import loginForm
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='app/base.html',authentication_form=loginForm), name='login')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 