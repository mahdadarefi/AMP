from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser





class HomePage(APIView):
    # permission_classes = [IsAuthenticated,]
    def get(self,request):
        data="HomePage"
        return Response(data=data)


