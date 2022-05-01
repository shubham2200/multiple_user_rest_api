from django.http import JsonResponse
from rest_framework import generics ,status
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.permissions import  IsAuthenticated
from rest_framework import  permissions
from rest_framework.decorators import api_view, permission_classes

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import *
# Create your views here.

class managerSignupView(generics.GenericAPIView):
    manage_signup = ManagerSignupSerializer
    def post(self,request, *args, **kwargs):
        seri = self.manage_signup(data= request.data)
        if seri.is_valid(raise_exception=True):
            user = seri.save()
            key = Token.objects.get(user=user).key
            print(Token.objects.get(user=user).key)
            
            # print(token.key)
            return JsonResponse({
            'user':UserSerializer(user , context= self.manage_signup()).data,
            'token':key,
            'massage':'done manager'
            })



class StaffSignupView(generics.GenericAPIView):
    staff_user = StaffSignupSerializer
    def post(self,request,  *args, **kwargs):
        seri = self.staff_user(data= request.data)
        if seri.is_valid(raise_exception=True):
            user = seri.save()
            key = Token.objects.get(user=user).key
            print(Token.objects.get(user=user).key)
            
            # print(token.key)
            return JsonResponse({
            'user':UserSerializer(user , context=self.staff_user()).data,
            'token':key,
            'massage':'done staff'
            })

class CostumAuth(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serialize = self.serializer_class(data = request.data , context = {'request':request})
        serialize.is_valid(raise_exception=True)
        user = serialize.validated_data['user']
        token , created= Token.objects.get_or_create(user=user)
        return JsonResponse({
            'token':token.key,
            'user_id':user.pk,
            'is_staff':user.is_staff
        })


class LogoutView(APIView):
    permission_classes = [IsAuthenticated&IsManagerUser]
    def post(self, request, format=None):
        request.auth.delete()
        return JsonResponse({"status":"user has been logout"})



class OnlyManagerView(APIView):
    permission_classes = [IsAuthenticated&IsManagerUser]
    seri_class = UserSerializer

    def get(self, request, format=None):

        content = {
            'status': 'request was permitted',
            'user':'user is manager'
        }
        return JsonResponse(content)
# generics.RetrieveAPIView
class OnlyStaffView(APIView):
    permission_classes = [IsAuthenticated&IsStaffUser]
    seri_class = UserSerializer

    def get(self, request, format=None):

        content = {
            'status': 'request was permitted',
            'user':'user is staff'
        }
        return JsonResponse(content)

class CreateReadManager(APIView):
    permission_classes = [IsAuthenticated&IsManagerUser]
    # adhar_seri = AdharSerializer
    addres_seri = AddressSerializer
    qouli = BankSerializer
    persnol = PersonalDetailsSerializer

    def post(self, request, *args, **kwargs):
        # adhar = self.adhar_seri(data = request.data)
        addres = self.addres_seri(data = request.data)
        Bank_f = self.qouli(data = request.data)
        detail = self.persnol(data = request.data)
        print(addres,Bank_f,detail)
        if addres.is_valid(raise_exception=True):
            addres.save()
            if Bank_f.is_valid():
                Bank_f.save()
                if detail.is_valid():
                    detail.save()


                return JsonResponse({
                        'addresss':addres.data,
                        'Bank':Bank_f.data,
                        'pernoal':detail.data
                        })
    def get(self, request, *args, **kwargs):
        addr = AddressSerializer(Address.objects.all() , many=True)
        bank = BankSerializer(Bank.objects.all() , many=True)
        return JsonResponse({
            'addree':addr.data,
            'bank':bank.data
        })
    
class CreateReadManagerDetails(APIView):
    permission_classes = [IsAuthenticated&IsManagerUser]
    def  get(self, request, pk):
        id = Address.objects.get(pk=pk)
        data = AddressSerializer(id)
        return JsonResponse({"data":data.data})




    def put(self, request, pk):
        ad_id = Address.objects.get(pk=pk)
        
        print(ad_id,'id')
        addr = AddressSerializer(instance=ad_id , data= request.data)
        print(addr)
        if addr.is_valid():
            addr.save()
            return JsonResponse({'data':addr.data,'adhar':'done'})
        else:
            return JsonResponse({'data':'not'})

    def delete(self, request, pk):
        id = Address.objects.get(pk=pk)
        id.delete()

        return JsonResponse({'delete':'done'})

class StaffOnlySee(APIView):
    permission_classes = [IsAuthenticated&IsStaffUser]
    def get(self, request, *args, **kwargs):
        addr = AddressSerializer(Address.objects.all() , many=True)
        bank = BankSerializer(Bank.objects.all() , many=True)
        return JsonResponse({
            'addree':addr.data,
            'bank':bank.data
        })
        