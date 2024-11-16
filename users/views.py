from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.core.mail import send_mail

# Create your views here.

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:main_page')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш онлайн-магазин!'
        messsage = """Спасибо, что зарегистрировались в нашем онлайн-магазине!
        Удачных покупок!"""
        from_email = "lysenkodjangoapp@yandex.ru"
        recipient_list = [user_email, ]
        send_mail(subject, messsage, from_email, recipient_list)