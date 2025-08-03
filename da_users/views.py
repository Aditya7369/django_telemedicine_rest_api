
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework import generics, viewsets, permissions

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        
        role = self.request.query_params.get('role')
        if role in [i[0] for i in CustomUser.ROLE_CHOICES]:
            return self.queryset.filter(role=role)
        if role == 'online_doctors':
            return self.queryset.filter(role='doctor', is_online=True)
        else:
            return self.queryset




