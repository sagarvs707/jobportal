from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage

from .forms import UploadFileForm

from .models import It_Jobs, Non_It_Jobs, Delivery_Boy
from .serializers import It_JobsSerializer, Non_It_JobsSerializer, Delivery_BoySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import jwt

import http.client

# Create your views here.
from .utils import otp_sms


@csrf_exempt
@api_view(['POST'])
def job_view(request):
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

            candidates_edu = request.data.get('candidates_edu')
            tenth_passing = request.data.get('tenth_passing')
            puc_passing = request.data.get('puc_passing')
            strem = request.data.get('strem')
            graduation_college_name = request.data.get('graduation_college_name')
            graduation_name_of_degree = request.data.get('graduation_name_of_degree')
            graduation_passing_year = request.data.get('graduation_passing_year')

            post_graduation_college_name = request.data.get('post_graduation_college_name')
            post_graduation_name_of_degree = request.data.get('post_graduation_name_of_degree')
            post_graduation_passing_year = request.data.get('post_graduation_passing_year')

            candidate_experience = request.data.get('candidate_experience')

            fresher_expected_salary_package = request.data.get('fresher_expected_salary_package')
            fresher_expected_salary = request.data.get('fresher_expected_salary')

            current_salary_package = request.data.get('current_salary_package')
            current_salary = request.data.get('current_salary')
            expected_salary_package = request.data.get('expected_salary_package')
            expected_salary = request.data.get('expected_salary')
            work_experience_of_year = request.data.get('work_experience_of_year')
            work_experience_of_month = request.data.get('work_experience_of_month')

            candidate_job_role = request.data.get('candidate_job_role')
            languege_can_speak_well = request.data.get('languege_can_speak_well')
            add_skills = request.data.get('add_skills')

            send_otp = request.data.get('send_otp')
            sms_notification = request.data.get('sms_notification')
            email_notification = request.data.get('email_notification')
            valid = request.data.get('valid')

            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    resume_path = request.FILES['resume_upload']
                    fs = FileSystemStorage()
                    filename = fs.save(resume_path.name, resume_path)
                    uploaded_file_url = filename
                except:
                    uploaded_file_url = request.data.get('resume_upload')

            try:

                validate = It_Jobs.objects.get(email=email)
                if validate.phone_number == phone_number:
                    return JsonResponse({'status': 'error', 'code': '400', 'message': 'Email Id is already Exists'})

            except Exception as e:
                if send_otp == 'True':
                    otp = otp_sms.otp_validate(phone_number)
                elif send_otp == 'False':
                    otp = None

            payload = {
                'phone_number': phone_number,
                'alternate_phone_number': alternate_phone_number,
                'name': name,
                'sureame': sureame,
                'email': email,
                'candidate_location': candidate_location,
                'date_of_birth': date_of_birth,
                'gender': gender,
                'candidates_edu': candidates_edu,
                'tenth_passing': tenth_passing,
                'puc_passing': puc_passing,
                'strem': strem,
                'graduation_college_name': graduation_college_name,
                'graduation_name_of_degree': graduation_name_of_degree,
                'graduation_passing_year': graduation_passing_year,
                'post_graduation_college_name': post_graduation_college_name,
                'post_graduation_name_of_degree': post_graduation_name_of_degree,
                'post_graduation_passing_year': post_graduation_passing_year,
                'candidate_experience': candidate_experience,
                'fresher_expected_salary_package': fresher_expected_salary_package,
                'fresher_expected_salary': fresher_expected_salary,
                'current_salary_package': current_salary_package,
                'current_salary': current_salary,
                'expected_salary_package': expected_salary_package,
                'expected_salary': expected_salary,
                'work_experience_of_year': work_experience_of_year,
                'work_experience_of_month': work_experience_of_month,
                'candidate_job_role': candidate_job_role,
                'languege_can_speak_well': languege_can_speak_well,
                'add_skills': add_skills,

                'sms_notification': sms_notification,
                'email_notification': email_notification,
                'resume_upload': str(uploaded_file_url),
                'sessionid': str(otp),
                'valid': valid,
            }

            reg = It_Jobs(**payload)
            reg.save()
            try:
                if valid == 'True':
                    return Response({'status': 'success', 'statuscode': '200', 'message': 'Register successfully'})
                elif valid == 'False':
                    token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
                    return Response({'status': 'success', 'statuscode': '200',
                                     'message': 'token generated successfully, OTP sent to your given number',
                                     'token': token})
            except:
                return JsonResponse({'status': 'fail', 'code': '400', 'message': 'Invalide entry'})
        else:
            return JsonResponse({'status': 'fail', 'code': '400', 'message': 'Invalide entry'})
    except Exception as e:
        return JsonResponse({'status': 'fail', 'code': '400', 'message': str(e)})


#######################################################################################################################

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
                get_valid = It_Jobs.objects.get(sessionid=messageid)
                get_valid.valid = True
                get_valid.save()
                return Response({'status': 'Success', 'status_code': '200', 'message': 'Registered Successfully'})
            elif msg_status == 'already_verified':
                return Response({'status': 'error', 'status_code': '400', 'message': 'OTP already sent'})
            elif Status == 'error':
                return Response({'status': 'error', 'status_code': '400', 'message': 'maximum attempt'})

        except Exception as e:
            return Response({'status': 'error', 'statuscode': '400', 'Message': 'OTP matching failed'})
    else:
        return Response({'status': 'error', 'statuscode': '400', 'Message': 'OTP matching failed'})


@api_view(['POST'])
def resend_otp(request):
    if request.method == 'POST':
        try:
            phone = phone = request.data.get('phone')
            url = '/api/retryotp.php?authkey=270904AEXxJuXLNsaV5ca5e529&mobile=+91' + phone + "&retrytype=text"
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
            return JsonResponse({"status": "error", "code": "404", 'meassage': 'OTP miss match', 'exception': str(e)})
    else:
        return JsonResponse({"status": "error", "code": "404", 'meassage': 'OTP miss match'})


class AddCondidate(APIView):

    def get_object(self, id):
        try:
            return It_Jobs.objects.get(id=id)
        except Exception as e:
            return Response({'status': 'error', 'statuscode': '404', 'Message': 'detile not found'})

    def get(self, request, id):
        try:
            if id is not None:
                user = self.get_object(id)
                serializer = It_JobsSerializer(user)
                return Response(serializer.data)
            else:
                return Response({'status': 'error', 'statuscode': '404', 'Message': 'Id not found'})
        except Exception as e:
            return Response({'status': 'error', 'statuscode': '404', 'Message': 'Id not found'})

    def put(self, request, id, format=None):
        update = self.get_object(id)
        serializer = It_JobsSerializer(update, data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'statuscode': '200', 'message': 'Updated successfully'})
            return Response(serializer.errors, )
        except Exception as e:
            return Response({'status': 'error', 'statuscode': '404', 'message': str(e)})

    def delete(self, request, id, format=None):
        try:
            deleteuser = self.get_object(id)
            deleteuser.delete()
            return Response({'status': 'success', 'statuscode': '204', 'messages': 'Deleted successfully'})
        except Exception as e:
            return Response({'status': 'error', 'statuscode': '400', 'message': 'User doesnot exist'})


@api_view(['GET'])
def view_all_candidate(request):
    if request.method == 'GET':
        view_all = It_Jobs.objects.all()
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
                'it_interest': view.job_interest,
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
                'resume_upload': view.resume_upload
            }
            view_list.append(payload)
        return Response({'status': 'success', 'code': '200', 'all_candidate': view_list})
    else:
        return Response({'status': 'fail', 'code': '404', 'message': 'Inavalid cradentials'})


@api_view(['GET'])
def view_all_candidate_count(request):
    if request.method == 'GET':
        view_all = It_Jobs.objects.all()
        all_cadidates = len(view_all)
        return Response({'status': 'success', 'code': '200', 'all_candidate': all_cadidates})
    else:
        return Response({'status': 'fail', 'code': '404', 'message': 'Inavalid cradentials'})


@api_view(['GET'])
def valid_candidate_count(request):
    if request.method == 'GET':
        view_all = It_Jobs.objects.filter(valid=True)
        valid_cadidates = len(view_all)
        return Response({'status': 'success', 'code': '200', 'valid_candidate': valid_cadidates})
    else:
        return Response({'status': 'fail', 'code': '404', 'message': 'Inavalid cradentials'})


@api_view(['GET', 'POST'])
def not_valid(request):
    if request.method == 'GET':
        not_valid = It_Jobs.objects.filter(valid=False)
        not_valid_cadidates = len(not_valid)
        return Response({'status': 'success', 'code': '200', 'valid_candidate': not_valid_cadidates})
    else:
        return Response({'status': 'fail', 'code': '404', 'message': 'Inavalid cradentials'})
