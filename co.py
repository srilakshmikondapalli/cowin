import requests
from requests.exceptions import ConnectionError, ConnectTimeout
import json
import hashlib
from tabulate import tabulate
from config import sub


class cowin(sub):
    """
    This class contains the different methods through which user lets know about the slots available
    """
    def __init__(self):
        self.res=[]
    def generate_otp(self):
        """
        This method used to generate the otp to the user entered mobile number
        :return:token
        """
        mob=input("enter mobile number:").strip()
        response = requests.post(url=self.read_config("url_1"),
                                 headers={ "user-agent":self.read_config("user_agent"),
                                "accept": self.read_config("accept"), "Content-Type": self.read_config("content_type")},
                                 data=json.dumps({"mobile": mob}))
        if response.status_code == 200:
            result = response.json()
            self.res.append(result["txnId"])
            return self.res[0]


        else:
            print(f'status_code:{response.status_code}|reason:{response.reason}')

    def confirm_otp(self):
        """
        This method confirms the otp given by the user
        :return: none
        """
        otp = input("enter otp:").strip()
        str = otp
        res = hashlib.sha256(str.encode())
        ele = res.hexdigest()
        session = requests.Session()
        response = session.post(url=self.read_config("url_2"),
                                headers={ "user-agent": self.read_config("user_agent")
,"accept": self.read_config("accept"), "Content-Type":self.read_config("content_type")},
                                data=json.dumps({"otp": ele, "txnId": self.res[0]}))

        if response.status_code == 200:
            resl = response.json()
            print(resl)

        else:
            print(f'status_code:{response.status_code}|reason:{response.reason}')

    def state_list(self):
        """
        This method provides the list of states in the country
        :return: none
        """
        response = requests.get(url=self.read_config("url_3"),
                                headers={"accept": self.read_config("accept"), "Accept-Language": "hi_IN",
                                         "user-agent":self.read_config("user_agent")})

        if response.status_code == 200:
            lst=[]

            result = response.json()
            choice=input("enter starting letter of your state:").upper()
            for ele in result["states"]:
                 if ele["state_name"].startswith(choice):
                        lst.append([ele["state_id"],ele["state_name"]])
                #print(f'state_id:{ele["state_id"]}| state_name:{ele["state_name"]}')
            print('\n\n', tabulate(lst, headers=['state_id', 'state_name'], tablefmt='orgtbl'))
        else:
            print(f'status_code:{response.status_code}|reason:{response.reason}')

    def district_list(self):
        """
        This method provides the list of districts in the state
        :return:
        """
        sid = input("enter state_id:")
        response = requests.get(
            url=self.read_config("url_4").replace('{state_id}', sid),
            headers={"accept": self.read_config("accept"), "Accept-Language": "hi_IN",
                     "user-agent":self.read_config("user_agent")})

        if response.status_code == 200:
            result = response.json()
            lst=[]
            choice=input("enter starting letter of your  district:").upper()
            for ele in result["districts"]:
                if ele["district_name"].startswith(choice):
                    lst.append([ele["district_id"],ele["district_name"]])
            print('\n\n', tabulate(lst, headers=['district_id', 'district_name'], tablefmt='orgtbl'))

        else:
            print(f'status_code:{response.status_code}|reason:{response.reason}')

    def findbypin(self):
        """
        This method is used to find the slots available for covid test by taking input as pincode and data from the user
        :return:
        """
        pincode = input("enter pincode:")
        date = input("enter date(dd-mm-yyyy):")
        response = requests.get(url=self.read_config("url_5"),
                                params={"pincode": pincode, "date": date},
                                headers={"user-agent": self.read_config("user_agent")})

        if response.status_code == 200:
            result = response.json()
            if len(result["sessions"]) == 0:
                print("No slots available")
            else:
                print(result["sessions"])

        else:
            print(f'status_code:{response.status_code}|reason:{response.reason}')

    def findbydistrict(self):
        """
        This method provides the slots availble for covid test by taking input as district and date
        from the user console
        :return:none
        """
        did = input("enter district_id:")
        date = input("enter date(dd-mm-yyyy):")
        response = requests.get(url=self.read_config("url_6"),
                                params={"district_id": did, "date": date},
                                headers={"user-agent": self.read_config("user_agent")})

        if response.status_code == 200:
            result = response.json()
            if len(result["sessions"]) == 0:
                print("No slots available")
            else:
                print(result["sessions"])
        else:
            print(f'status_code:{response.status_code}|reason:{response.reason}')

    def calenderbypin(self):
        """
        This method provides the slots available for covid test by taking input as
        pincode and date from user console
        :return:none
        """
        pin = input("enter pincode:")
        date = input("enter date(dd-mm-yyyy):")
        response = requests.get(url=self.read_config("url_7"),
                                params={"pincode": pin, "date": date},
                                headers={"user-agent": self.read_config("user_agent")})

        if response.status_code == 200:
            result = response.json()
            if len(result["centers"]) == 0:
                print("No centers available")
            else:
                print(result["centers"])
        else:
            print(f'status_code:{response.status_code}|reason:{response.reason}')

    def calenderbydistrict(self):
        """
        This method provides slots available for covid test by taking input
        as district and date from user console
        :return: none
        """
        did = input("enter district_id:")
        date = input("enter date(dd-mm-yyyy):")
        response = requests.get(url=self.read_config("url_8"),
                                params={"district_id": did, "date": date},
                                headers={"user-agent": self.read_config("user_agent")})

        if response.status_code == 200:
            result = response.json()
            if len(result["centers"]) == 0:
                print("No centers available")
            else:
                print(result["centers"])
        else:
            print(f'status_code:{response.status_code}|reason:{response.reason}')

    def main(self):
        """
        This method provides the user to select the different ways of finding available slots.They are:
        1.find by pin
        2.find by district
        3.calender by pin
        4.calender by district
        :return:
        """
        while True:
            try:
                print("WELCOME TO COWIN APPLICATION ...!")
                print('1.find by pin', '2.find by district', '3.calendar by pin', '4.calendar by district', sep='\n')
                choice = input('enter our choice:')
                if choice == '1':
                    self.findbypin()
                elif choice == '2':
                    self.findbydistrict()
                elif choice == '3':
                    self.calenderbypin()
                elif choice == '4':
                    self.calenderbydistrict()
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


obj=cowin()
obj.generate_otp()
obj.confirm_otp()
obj.state_list()
obj.district_list()
obj.main()
