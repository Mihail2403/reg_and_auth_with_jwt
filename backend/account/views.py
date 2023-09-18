from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import views, response

from account.models import Profile
from backend import settings


def send_verification_mail(profile, host):
    subject = 'Hi, please do verification your acc'
    token = profile.uuid
    user_id = profile.user.id
    hrf = f'{host}/verification/{token}/'
    message = f'Передите по ссылке, чтобы активировать почту:\n{hrf}'
    to = [profile.user.email]
    send_mail(subject, message, settings.EMAIL_HOST_USER, to, fail_silently=False)


class RegisterAPIView(views.APIView):

    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
            email = request.data['email']
            user = User.objects.create_user(username=username, password=password, email=email, is_active=False)
            profile = Profile.objects.create(user=user)
            return response.Response({"status": "good", "user_id": user.id})
        except:
            return response.Response({"status": "bad"})


class RequestForSendVerificationEmailAPIView(views.APIView):
    def get(self, request):
        try:
            user = User.objects.get(id=request.data['user_id'])
            profile = Profile.objects.get(user=user)
            send_verification_mail(profile, 'http://127.0.0.1:8000')
            return response.Response({"status": "good"})
        except:
            return response.Response({"status": "bad"})


class VerificationAPIView(views.APIView):

    def get(self, request, uuid):
        try:
            user = Profile.objects.get(uuid=uuid).user if Profile.objects.get(uuid=uuid) else None

            if user:
                user.is_active = True
                user.save()
                return response.Response({"status": "good"})
            return response.Response({"status": "bad"})
        except:
            return response.Response({"status": "bad"})

