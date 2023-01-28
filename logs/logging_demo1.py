import logging



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
# logging.debug(f"the addition of numbers is:{sum_result}")
# logging.critical(f"the addition of numbers is:{sum_result}")
logging.error(f"the addition of numbers is:,{sum_result}")
logging.critical(f"the addition of numbers is:{sum_result}")
logging.warning(f"the addition of numbers is:{sum_result}")
# logging.info("add 2 numbers is passed ")

#
multiply_result = dl.multiply_numbers(3,4)
# print(f"the multiplication of nos is:{multiply_result}")
# print("the multiplication of result is:",multiply_result)
logging.warning(f"the multiplication of result is:{multiply_result}")
# logging.info(f"the multiplication of nos is:{multiply_result}")



#