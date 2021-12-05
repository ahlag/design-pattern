# Design a call center
class CallCenter:
    
    def __init__(self) -> None:
        pass
        
    def route_respondent():
        pass
    
    def route_call():
        pass
    
class Call:
    
    def __init__(self, issue):
        self.issue = issue
        self.employee = None

    def resolve(self, handled):
        if handled:
            self.issue = None
        self.employee.finish_call(handled)
        
    def apologize_and_handup(self):
        # "Try calling our competitor."
        self.employee = None
        
class Employee(object):
    
    def __init__(self, name, manager):
        self.name, self.manager = name, manager
        self.call = None
        
    def take_call():
        pass
    
    def escalate():
        pass
    
    def finish_call():
        pass

class Respondent(Employee):
    pass

class Manager(Employee):
    pass

class Director(Employee):
    def __init__(self, name):
        super(Director, self).__init__(name, None)

import unittest

class Test(unittest.TestCase):
    def test_call_center(self):
        lashaun = Director('Lashaun')
        juan    = Manager('Juan', lashaun)
        sally   = Manager("Sally", lashaun)
        boris   = Respondent("Boris", juan)
        sam     = Respondent("Sam", juan)
        jordan  = Respondent("Jordan", sally)
        casey   = Respondent("Casey", sally)
        center = CallCenter([boris, sam, jordan, casey], [juan, lashaun], sally)
        call1 = Call("The toilet")
        call2 = Call("The webpage")
        call3 = Call("The email")
        call4 = Call("The lizard")
        call5 = Call("The cloudy weather")
        call6 = Call("The noise")
        
if __name__ == "__main__":
    unittest.main()