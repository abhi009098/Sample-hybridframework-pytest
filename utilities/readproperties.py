import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\abhi0\\PycharmProjects\\hybridframework\\configurations\\config.ini")


class readconfig:

    @staticmethod
    def getapplicationURL():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getuserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
