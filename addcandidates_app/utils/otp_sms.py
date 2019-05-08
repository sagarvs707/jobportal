import json
import http.client

def otp_validate(phone_number):
    url = "/api/sendotp.php?authkey=273205Ax8ophJB65cbaae80&message=your verification code is %23%23OTP%23%23&sender=TROJOB&mobile=+91"
    conn = http.client.HTTPConnection("control.msg91.com")
    conn.request("POST", url + str(phone_number))
    res = conn.getresponse()
    data = res.read()
    data_respond = data.decode("utf-8")
    message1 = json.loads(data_respond)
    message = message1['message']
    return message