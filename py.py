
'''-------------------------------------------------
 it a method that takes the name form the user and 
check the gender if it male it choose the welcome
that will show to the user
------------------------------------------------- '''

name = input("please enter your first name : ").strip().capitalize()

last_name = input("please enter your last name : ").strip().capitalize()

your_gender = input("please enter your gender : ").strip().capitalize()



class member:

    def __init__(self,fname,lname,gender):

        self.first_name = fname
        
        self.last_name = lname

        self.gender = gender

    def user_name(self):

        return f"hello your name is : {self.first_name} {self.last_name}"

    def welcome(self):

        if self.gender == "Male" :

            return f"welcome mr {self.first_name}"

        elif self.gender == "Female":
            
            return f"welcome miss {self.first_name}"

        else :

            return f"welcome {self.first_name}"

    def collect_all(self):

        return f"- {self.user_name()} , {self.welcome()} -"
    
member_one = member( name, last_name, your_gender)


print(member_one.collect_all())



