from django.http import HttpResponse, JsonResponse
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

import http.client


# Create your views here.



@csrf_exempt
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
            resume = json.dumps(str(resume_upload))  #converting file to json formate

            try:
                validate = AddCandidate.objects.get(email=email)
                if validate is not None:
                    return JsonResponse({'status':'error', 'code':'400', 'message':'Email Id is already Exists'})

            except Exception as e:
                url = "/api/sendotp.php?authkey=270904AEXxJuXLNsaV5ca5e529&message=your verification code is %23%23OTP%23%23&sender=611332&mobile=+91"
                conn = http.client.HTTPConnection("control.msg91.com")
                conn.request("POST", url + str(phone_number))
                res = conn.getresponse()
                data = res.read()
                data_respond = data.decode("utf-8")
                message1 = json.loads(data_respond)
                message = message1['message']

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
                    'resume_upload': resume,
                    'sessionid': str(message),
                    'valid': valid
                }

                reg = AddCandidate(**payload)
                reg.save()
                token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
                return Response({'status': 'success', 'statuscode': '200', 'message': 'token generated successfully, OTP sent to your given number', 'token': token})
        else:
            return JsonResponse({'status': 'fail', 'code': '400', 'message': 'Invalide entry'})
    except Exception as e:
        return JsonResponse({'status': 'fail', 'code': '400', 'message': str(e)})



@api_view(['GET', 'POST'])
def validate_registration_otp(request):
    if request.method == 'POST':
        get_otp = request.data.get('otp')
        get_token = request.data.get('token')
        phone = request.data.get('phone')


        token1 = jwt.decode(get_token, 'secret', algorithms=['HS256'])
        messageid = token1.get("sessionid")

        url = "/api/verifyRequestOTP.php?authkey=270904AEXxJuXLNsaV5ca5e529&mobile=+91" + phone + "&otp="
        print(url)

        conn = http.client.HTTPSConnection("control.msg91.com")

        payload = messageid
        headers = {'content-type': "application/x-www-form-urlencoded"}

        conn.request("POST", url + get_otp, payload, headers)
        res = conn.getresponse()
        data = res.read()
        verified = data.decode("utf-8")
        y = json.loads(verified)
        Status = y['type']
        msg_status = y['message']

        try:
            if Status == 'success':
                get_valid = AddCandidate.objects.get(sessionid=messageid)
                get_valid.valid = True
                get_valid.save()
                return Response({'status': 'Success', 'status_code': '200', 'message': 'Registered Successfully'})
            elif msg_status == 'already_verified':
                return Response({'status': 'fail', 'status_code': '400', 'message': 'OTP already sent'})
            elif Status == 'error':
                return Response({'status': 'fail', 'status_code': '400', 'message': 'maximum attempt'})

        except Exception as e:
            return Response({'status': 'error', 'statuscode': '400', 'Message': 'OTP matching failed'})
    else:
        return Response({'status': 'error', 'statuscode': '400', 'Message': 'OTP matching failed'})

@api_view(['POST'])
def resend_otp(request):
    if request.method == 'POST':
        try:
            phone = phone = request.data.get('phone')
            url = '/api/retryotp.php?authkey=270904AEXxJuXLNsaV5ca5e529&mobile=+91'+ phone +"&retrytype=text"
            print(url)
            conn = http.client.HTTPConnection("control.msg91.com")
            payload = "39644430445a353133383734"
            headers = {'content-type': "application/x-www-form-urlencoded"}

            conn.request("POST", url, payload, headers)

            res = conn.getresponse()
            data = res.read()
            verified = data.decode("utf-8")
            return JsonResponse({'status': 'success', 'code': '200', 'meassage': 'OTP sent successfully'})
        except Exception as e:
            return JsonResponse({"status": "fail", "code": "404", 'meassage': 'OTP miss match', 'exception':str(e)})
    else:
        return JsonResponse({"status": "fail", "code": "404", 'meassage': 'OTP miss match'})




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

@api_view(['GET'])
def view_all_candidate(request):
    if request.method == 'GET':
        view_all = AddCandidate.objects.all()
        view_list = []
        for view in view_all:
            payload = {
                'id': view.id,
                'phone_number': view.phone_number,
                'alternate_phone_number': view.alternate_phone_number,
                'name': view.name,
                'sureame': view.sureame,
                'email': view.email,
                'candidate_location': view.candidate_location,
                'date_of_birth': view.date_of_birth,
                'gender': view.gender,
                'job_interest': view.job_interest,
                'candidates_edu': view.candidates_edu,
                'college_name': view.college_name,
                'name_of_degree': view.name_of_degree,
                'passing_year': view.passing_year,
                'candidate_experience': view.candidate_experience,
                'expected_salary': view.expected_salary,
                'notice_period': view.notice_period,
                'candidate_job_role': view.candidate_job_role,
                'add_skills': view.add_skills,
                'sms_notification': view.sms_notification,
                'email_notification': view.email_notification,
                'resume_upload': '/media/'+str(view.resume_upload)
            }
            view_list.append(payload)
        return Response({'status':'success', 'code': '200', 'all_candidate': view_list})
    else:
        return Response({'status':'fail', 'code': '404', 'message': 'Inavalid cradentials'})

@api_view(['GET'])
def view_all_candidate_count(request):
    if request.method == 'GET':
        view_all = AddCandidate.objects.all()
        all_cadidates = len(view_all)
        return Response({'status':'success', 'code': '200', 'all_candidate': all_cadidates})
    else:
        return Response({'status':'fail', 'code':'404', 'message':'Inavalid cradentials'})

@api_view(['GET'])
def valid_candidate_count(request):
    if request.method == 'GET':
        view_all = AddCandidate.objects.filter(valid=True)
        valid_cadidates = len(view_all)
        return Response({'status':'success', 'code': '200', 'valid_candidate': valid_cadidates})
    else:
        return Response({'status':'fail', 'code':'404', 'message':'Inavalid cradentials'})


@api_view(['GET', 'POST'])
def not_valid(request):
    if request.method == 'GET':
        not_valid = AddCandidate.objects.filter(valid=False)
        not_valid_cadidates = len(not_valid)
        return Response({'status': 'success', 'code': '200', 'valid_candidate': not_valid_cadidates})
    else:
        return Response({'status': 'fail', 'code': '404', 'message': 'Inavalid cradentials'})