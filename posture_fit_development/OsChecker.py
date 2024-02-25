from dataclasses import dataclass, field
import os
import sys
@dataclass
class Statistic:
    def isWindows() -> bool:
        if os.name == "posix":
            return False
        else:
            return True

    def isExecutable() -> bool:
        if getattr(sys, 'frozen', False):
            return True
        elif __file__:
           return False 
        else:
            print("Neither __file__ or frozen, called in repl?")
            return False
    
    # or True is just incase it errors inside the function but doesn't exit
    windows: bool = isWindows() 
    executable: bool = isExecutable() 

