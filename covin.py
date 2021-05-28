import requests
from requests.exceptions import ConnectionError, ConnectTimeout
import json
import hashlib

def generate_otp():
    mob=input("enter mobile number:")
    response=requests.post(url="https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP",
                           headers={"accept":"application/json","Content-Type":"application/json"},
                                    data=json.dumps({"mobile":mob}))
    if response.status_code==200:
        result=response.json()
        print(result)
        return result


    else:
        print(f'status_code:{response.status_code}|reason:{response.reason}')

def confirm_otp():
    otp=input("enter otp:")
    str = otp
    res = hashlib.sha256(str.encode())
    ele=res.hexdigest()
    session = requests.Session()
    response = session.post(url="https://cdn-api.co-vin.in/api/v2/auth/public/confirmOTP",
                             headers={"accept": "application/json", "Content-Type": "application/json"},
                             data=json.dumps({"otp":ele,"txnId":result["txnId"]}))

    if response.status_code == 200:
        resl=response.json()
        print(resl)

    else:
        print(f'status_code:{response.status_code}|reason:{response.reason}')
def state_list():
    response = requests.get(url="https://cdn-api.co-vin.in/api/v2/admin/location/states",
                             headers={"accept": "application/json", "Accept-Language": "hi_IN", "user-agent": self.read_config("user_agent")})

    if response.status_code == 200:
        result=response.json()
        for ele in result["states"]:
            print(f'state_id:{ele["state_id"]}| state_name:{ele["state_name"]}')
    else:
        print(f'status_code:{response.status_code}|reason:{response.reason}')

def district_list():
    sid=input("enter state_id:")
    response = requests.get(url="https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}".replace('{state_id}',sid),
                            headers={"accept": "application/json", "Accept-Language": "hi_IN",
                                     "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})

    if response.status_code == 200:
        result = response.json()
        for ele in result["districts"]:
            print(f'district_id:{ele["district_id"]}| district_name:{ele["district_name"]}')
    else:
        print(f'status_code:{response.status_code}|reason:{response.reason}')

def findbypin():
    pincode=input("enter pincode:")
    date=input("enter date(dd-mm-yyyy):")
    response = requests.get(url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin",params={"pincode":pincode,"date":date},
        headers={"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})

    if response.status_code == 200:
        result = response.json()
        if len(result["sessions"])==0:
            print("No slots available")
        else:
            print(result["sessions"])

    else:
        print(f'status_code:{response.status_code}|reason:{response.reason}')

def findbydistrict():
    did = input("enter district_id:")
    date = input("enter date(dd-mm-yyyy):")
    response = requests.get(url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict",
                            params={"district_id":did, "date": date},
                            headers={
                                "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})

    if response.status_code == 200:
        result = response.json()
        if len(result["sessions"])==0:
            print("No slots available")
        else:
            print(result["sessions"])
    else:
        print(f'status_code:{response.status_code}|reason:{response.reason}')

def calenderbypin():
    pin=input("enter pincode:")
    date=input("enter date(dd-mm-yyyy):")
    response = requests.get(url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin",
                            params={"pincode":pin, "date":date},
                            headers={
                                "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})

    if response.status_code == 200:
        result = response.json()
        if len(result["centers"])==0:
            print("No centers available")
        else:
            print(result["centers"])
    else:
        print(f'status_code:{response.status_code}|reason:{response.reason}')

def calenderbydistrict():
    did=input("enter district_id:")
    date = input("enter date(dd-mm-yyyy):")
    response = requests.get(url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict",
                            params={"district_id":did, "date": date},
                            headers={
                                "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})

    if response.status_code == 200:
        result = response.json()
        if len(result["centers"])==0:
            print("No centers available")
        else:
            print(result["centers"])
    else:
        print(f'status_code:{response.status_code}|reason:{response.reason}')
def main():
    while True:
        try:
            print("WELCOME TO COWIN APPLICATION ...!")
            print('1.find by pin', '2.find by district','3.calendar by pin','4.calendar by district', sep='\n')
            choice = input('enter our choice:')
            if choice == '1':
                findbypin()
            elif choice == '2':
                findbydistrict()
            elif choice == '3':
                calenderbypin()
            elif choice=='4':
                calenderbydistrict()
            else:
                print("invalid choice. enter your choice among above mentioned 4 choices")
        except (ConnectionError, ConnectTimeout):
            print("please check your internet connection")
        while True:
            flag = False
            user_choice = input("do u want to continue cowin application[y/n]")
            if user_choice in ['y' or 'Y']:
                flag = True
                break
            elif user_choice in ['n' or 'N']:
                flag = False
                break
            else:
                print("invalid entry please enter y(yes) or n(no)")
                continue
        if flag is True:
            continue
        elif flag is False:
            break

mob=input("enter mobile number:")
result=generate_otp()
confirm_otp()
state_list()
district_list()
main()