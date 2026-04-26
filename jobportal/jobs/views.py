from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from .permissions import IsEmployer, IsownerorReadOnly

# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-id')
    serializer_class = JobSerializer
    
    def get_permissions(self):
        if self.action == "create":
            return [IsEmployer()]
        elif self.action == ["update", "partial_update", "destroy"]:
            return [IsownerorReadOnly()]
        return [permissions.AllowAny()]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    #Apply to job
    @action(detail=False, methods=['post'])
    def apply(self, request):
        job_id = request.data.get('job')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)
    
    #View applied jobs
    @action(detail=False, methods=['get'])
    def my_applications(self, request):
        apps = Application.objects.filter(user=request.user)
        serializer = self.get_serializer(apps, many=True)
        return Response(serializer.data)
    
    
