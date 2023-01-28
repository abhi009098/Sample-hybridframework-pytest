import logging
#creates log files in default directory where .py python file  is created
# logging.basicConfig(level=logging.DEBUG,filename="samplelogs.log",filemode="w") #debug,info other 3 levels also to print we need level=logging.debug
# logging.basicConfig(filename="samplelogs.log",filemode="w") #THIS WILL PRINT ONLY error,warning,critical messages
#file mode "w" is for overwrite msgs in same file
#file mode "a" is to append means adds each time every new msgs in same file only
#file name is name of file should end with .log
#FORMAT AND DATE FORMAT

#create log files in specific directory
logging.basicConfig(level=logging.DEBUG,filename="..\\logs\\automation.log",filemode="a",format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
class Demologging1:
    def add_numbers(self, a, b):
        return a + b

    def multiply_numbers(self, a, b):
        return a * b


dl = Demologging1()
sum_result = dl.add_numbers(3,2)
# print(f"the addition of numbers is:{sum_result}")
# print("the addition of numbers is:",sum_result)
#instead of print disappears after program we are using logging feature to capture permanently the result in form of events
logging.debug(f"the addition of numbers is:{sum_result}")
# logging.critical(f"the addition of numbers is:{sum_result}")
logging.error(f"the addition of numbers is:,{sum_result}")
logging.critical(f"the addition of numbers is:{sum_result}")
logging.warning(f"the addition of numbers is:{sum_result}")
logging.info(f"the addition of numbers is:{sum_result}")
logging.info("add 2 numbers is passed ")

#
multiply_result = dl.multiply_numbers(3,4)
# print(f"the multiplication of nos is:{multiply_result}")
# print("the multiplication of result is:",multiply_result)
logging.warning(f"the multiplication of result is:{multiply_result}")
# logging.info(f"the multiplication of nos is:{multiply_result}")



#