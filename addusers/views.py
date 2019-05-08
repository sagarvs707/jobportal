import jwt
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from addusers.serializers import AddusersSerializer
from .models import AddUsers
# Create your views here.

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        mobile_number = request.data.get('mobile_number')
        password = request.data.get('password')
        create_applications = request.data.get('create_applications')
        try:
            data = AddUsers.objects.filter(mobile_number=mobile_number)
            if data.exists():
                return Response({'status':'Fail', 'code':'400', 'message':'User Mobile number already exists'})
            else:
                payload = {
                        'first_name':first_name,
                        'last_name':last_name,
                        'email':email,
                        'mobile_number':mobile_number,
                        'password':password,
                        'create_applications': create_applications,
                }
                reg = AddUsers(**payload)
                reg.save()

                token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
                return Response({'status': 'success', 'statuscode': '200', 'message': 'token generated successfully', 'token': token})
        except Exception as e:
            return Response({'status': 'fail', 'code': '400', 'message': 'Invalide entry'})

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            validate = AddUsers.objects.get(email=email)
            if validate.password == password:
                payload = {
                    'id':validate.id,
                    'first_name': validate.first_name,
                    'last_name': validate.last_name,
                    'email': validate.email,
                    'mobile_number': validate.mobile_number,
                    'password': validate.password,
                    'create_applications': validate.create_applications,
                }
                token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
                return Response({'status': 'success', 'statuscode': '200',
                                 'message': 'token generated successfully', 'token': token})
            else:
                return Response({'status':'Fail', 'code':'400', 'message':'Invalid Mail id and Password'})
        except Exception as e:
            return Response({'status': 'Fail', 'code': '400', 'message': 'Invalid Mail id and Password'})
    else:
        return Response({'status':'Fail', 'code':'404', 'message':'Invalid cradentials'})


class AddUser(APIView):

    def get_object(self, id):
        try:
            return AddUsers.objects.get(id=id)
        except Exception as e:
            return Response({'status': 'error', 'statuscode':'404', 'Message':'detile not found'})


    def get(self, request, id):
        try:
            if id is not None:
                user = self.get_object(id)
                serializer = AddusersSerializer(user)
                return Response(serializer.data)
            else:
                return Response({'status': 'error', 'statuscode':'404', 'Message':'Id not found'})
        except Exception as e:
            return Response({'status': 'error', 'statuscode':'404', 'Message':'Id not found'})

    def put(self, request, id, format=None):
        update = self.get_object(id)
        serializer = AddusersSerializer(update, data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({'status':'success', 'statuscode':'200', 'message':'Updated successfully'})
            return Response(serializer.errors,)
        except Exception as e:
            return Response({'status': 'fail', 'statuscode': '404', 'message': str(e)})


    def delete(self, request, id, format=None):
        try:
            deleteuser = self.get_object(id)
            deleteuser.delete()
            return Response({'status': 'success', 'statuscode': '204', 'messages': 'Deleted successfully'})
        except Exception as e:
            return Response({'status':str(e), 'statuscode':'400', 'message':'User doesnot exist'})


@api_view(['POST'])
def change_password(request):
    if request.method == 'POST':
        user_id = request.data.get('user_id')
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')
        try:
            user = AddUsers.objects.get(id=user_id)
            if user.password == current_password:
                try:
                    user.password = new_password
                    user.save()
                    return Response({'status': 'success', 'code': '200', 'message': 'Password is reset successfully'})
                except Exception as e:
                    return Response({'status': 'error', 'code': '400', 'message': 'old password is invalide'})
            else:
                return Response({'status': 'error', 'code': '400', 'message': 'Password are does not matching'})
        except Exception as e:
            return Response({'status': 'error', 'code': '400', 'message': 'Invalid credential'})



@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        view_all = AddUsers.objects.all()
        view_list = []
        for view in view_all:
            payload = {
                'id': view.id,
                'first_name': view.first_name,
                'last_name': view.last_name,
                'email': view.email,
                'mobile_number': view.mobile_number,
                'password': view.password,
                'create_applications': view.create_applications,
            }
            view_list.append(payload)
        return Response({'status':'success', 'code': '200', 'all_candidate': view_list})
    else:
        return Response({'status':'fail', 'code': '404', 'message': 'Inavalid cradentials'})
