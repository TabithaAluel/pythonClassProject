class User:
    def __init__(self,name,Email,password,login):
        self.name=name
        self.Email=Email
        self.password=password
        self.login=login
    def login(self) :
        Email=input("Enter Email: ")  
        password=input("Enter password: ")
        if self.Email==Email and self.password==password:
            print('logged in successfully \n', self.name,'\n',self.Email) 
        else:
            print('incorrect password')
# User1=User("Aluel","alueltabitha@gmail.com","aluel@123",False) 
# User2=User("Belyse","belyseintwaza@gmail.com",False) 
# User2.login()



    


