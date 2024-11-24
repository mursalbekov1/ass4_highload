from django.shortcuts import render, redirect
from rest_framework import serializers, viewsets, permissions

from .forms import RegisterForm
from django.contrib import messages
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
from django_otp.plugins.otp_totp.models import TOTPDevice

from .models import SecureData


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def setup_2fa(request):
    user = request.user
    device, created = TOTPDevice.objects.get_or_create(user=user, name="default")
    if created:
        qr = qrcode.make(device.config_url)
        buffer = BytesIO()
        qr.save(buffer)
        buffer.seek(0)
        qr_code = buffer.getvalue()
        return HttpResponse(qr_code, content_type="image/png")
    return render(request, '2fa/setup.html', {'device': device})

class SecureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureData
        fields = '__all__'

class SecureDataViewSet(viewsets.ModelViewSet):
    queryset = SecureData.objects.all()
    serializer_class = SecureDataSerializer

    def get_permissions(self):
        if self.request.user.is_superuser:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]