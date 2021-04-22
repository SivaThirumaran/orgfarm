import configparser

config=configparser.RawConfigParser()
config.read(".\\configuration\\confg.ini")

class Readconfig:
    @staticmethod
    def getapplicationURL():
        url=config.get('login info','baseurl')
        return url

    @staticmethod
    def getemail():
        useremail = config.get('login info', 'email')
        return useremail

    @staticmethod
    def getpassword():
        userpassword = config.get('login info', 'password')
        return userpassword

    @staticmethod
    def getpincode():
        userpincode = config.get('login info', 'pincode')
        return userpincode