from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from addcandidates_app.forms import DocumentForm
from .models import AddCandidate
from .serializers import AddCandidateSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
import jwt

# Create your views here.


@api_view(['POST'])
def addcondidate_view(request):
    try:
        if request.method == 'POST':
            phone_number = request.data.get('phone_number')
            alternate_phone_number = request.data.get('alternate_phone_number')
            name = request.data.get('name')
            sureame = request.data.get('sureame')
            email = request.data.get('email')
            candidate_location = request.data.get('candidate_location')
            date_of_birth = request.data.get('date_of_birth')
            gender = request.data.get('gender')
            job_interest = request.data.get('job_interest')
            candidates_edu = request.data.get('candidates_edu')
            college_name = request.data.get('college_name')
            name_of_degree = request.data.get('name_of_degree')
            passing_year = request.data.get('passing_year')
            candidate_experience = request.data.get('candidate_experience')
            expected_salary = request.data.get('expected_salary')
            notice_period = request.data.get('notice_period')
            candidate_job_role = request.data.get('candidate_job_role')
            add_skills = request.data.get('add_skills')
            sms_notification = request.data.get('sms_notification')
            email_notification = request.data.get('email_notification')
            valid = request.data.get('valid')
            resume_upload = request.data.get('resume_upload')
            try:
                validate = AddCandidate.objects.get(email=email)
                if validate is not None:
                    return Response({'status':'error', 'code':'400', 'message':'Email Id is already Exists'})

            except Exception as e:
                session_otp= requests.post('https://2factor.in/API/V1/77dad3c3-67e9-11e9-90e4-0200cd936042/SMS/+91'+phone_number+'/AUTOGEN', params=request.POST)
                session = session_otp.content
                session1 = session.decode("utf-8")
                x = json.loads(session1)
                session_id = x['Details']

                payload = {
                    'phone_number': phone_number,
                    'alternate_phone_number': alternate_phone_number,
                    'name': name,
                    'sureame': sureame,
                    'email': email,
                    'candidate_location': candidate_location,
                    'date_of_birth': date_of_birth,
                    'gender': gender,
                    'job_interest': job_interest,
                    'candidates_edu': candidates_edu,
                    'college_name': college_name,
                    'name_of_degree': name_of_degree,
                    'passing_year': passing_year,
                    'candidate_experience': candidate_experience,
                    'expected_salary': expected_salary,
                    'notice_period': notice_period,
                    'candidate_job_role': candidate_job_role,
                    'add_skills': add_skills,
                    'sms_notification': sms_notification,
                    'email_notification': email_notification,
                    'resume_upload': resume_upload,
                    'sessionid': str(session_id),
                    'valid': valid


                }

                reg = AddCandidate(**payload)
                reg.save()
                token = jwt.encode(payload, 'secret', algorithm='HS256')
            return Response({'status': 'success', 'statuscode': '200', 'message': 'token generated successfully, OTP sent to your given number', 'token': token})
    except Exception as e:
        return Response({'status': 'fail', 'code': '400', 'message': 'Invalide entry'})


@api_view(['GET', 'POST'])
def validate_registration_otp(request):
    if request.method == 'POST':
        get_otp = request.data.get('otp')
        get_token = request.data.get('token')

        token1 = jwt.decode(get_token, 'secret', algorithms=['HS256'])
        session_id = token1.get("sessionid")

        verified = requests.post('https://2factor.in/API/V1/77dad3c3-67e9-11e9-90e4-0200cd936042/SMS/VERIFY/'+session_id+'/'+str(get_otp), params=request.POST)
        a = verified.content
        session_otp = a.decode("utf-8")
        y = json.loads(session_otp)
        Status = y['Status']

        try:
            if Status == 'Success':
                get_valid = AddCandidate.objects.get(sessionid=session_id)
                get_valid.valid = True
                get_valid.save()
                return Response({'status': 'Success', 'status_code': '200', 'message': 'Registered Successfully'})
        except Exception as e:
            return Response({'status': 'error', 'statuscode': '400', 'Message': 'OTP matching failed'})
    else:
        return Response({'status': 'error', 'statuscode': '400', 'Message': 'OTP matching failed'})


class AddCondidate(APIView):

    def get_object(self, id):
        try:
            return AddCandidate.objects.get(id=id)
        except Exception as e:
            return Response({'status': 'error', 'statuscode':'404', 'Message':'detile not found'})


    def get(self, request, id):
        try:
            if id is not None:
                user = self.get_object(id)
                serializer = AddCandidateSerializer(user)
                return Response(serializer.data)
            else:
                return Response({'status': 'error', 'statuscode':'404', 'Message':'Id not found'})
        except Exception as e:
            return Response({'status': 'error', 'statuscode':'404', 'Message':'Id not found'})

    def put(self, request, id, format=None):
        update = self.get_object(id)
        serializer = AddCandidateSerializer(update, data=request.data)
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


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return Response({'status': 'success', 'statuscode': '200', 'message': 'Resume uploaded successfully'})
    else:
        form = DocumentForm()
    return render(request, 'addcondidates_app/model_form_upload.html', {
        'form': form
    })