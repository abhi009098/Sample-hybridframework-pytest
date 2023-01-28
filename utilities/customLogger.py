import logtest
import logging


class logGen:
    @staticmethod
    def loggen():
        # CREATE LOGGER
        # logger = logging.getLogger()
        logger = logging.getLogger("logGen")  # inside brackets set class/method name from where it is called
        # CREATE CONSOLE OR FILE HANDLER ANS SET LOG LEVEL
        # stHandler = logging.StreamHandler()
        fhandler = logging.FileHandler(filename='C:\\Users\\abhi0\\PycharmProjects\\hybridframework\\logs\\automation.log', mode='a')
        # sthandler = logging.StreamHandler(filename='..\\\\logs\\\\automation.log', mode='a') #CONSOLE
        logger.setLevel(logging.DEBUG)
        # CREATE FORMATTER HOW YOU WANT YOUR LOGS TO BE FORAMTTED
        # formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # ADD FORMATTER TO CONSOLE OR FILE HANDLER
        fhandler.setFormatter(formatter)
        # stHandler.setFormatter(formatter)
        # ADD CONSOLE HANDLER OR FILE HANDLER TO LOGGER
        logger.addHandler(fhandler)
        # logger.addHandler(stHandler)
        return logger

