data = {}

def register():
        #Register
        Student_ID = int(input("Enter the Student Number :"))
        Name = input("Enter the name :")
        Name_Full = Name.replace(' ', '_')
        Course = input("Enter the course of {}  :".format(Name))
        Course_Full = Course.replace(' ', '_')
        Prelim = float(input("Enter Prelim Grade: "))
        Midterm = float(input("Enter Midterm Grade: "))
        Final = float(input("Enter Final Grade: "))
        print(('#' * 27 )+ 'DATABASE' + ('#' * 27))
        #Average
        Final_Average = (float(Prelim) + float(Midterm)+float(Final)) / 3
        Final_Average_Round = round(Final_Average, 2)

        #Results
        Happy = ('\U0001F600')
        Laugh =('\U0001F606')
        Sad   =("\U0001F62D")
        if Final_Average > 70:
                result = Happy
        elif Final_Average == 70:
                result = Laugh
        else:
                result = Sad

        #Split and string
        Prelim_str = str(Prelim).split()
        Midterm_str= str(Midterm).split()
        Final_str  = str(Final).split()
        Final_Average_str = str(Final_Average_Round).split()
        Student_ID_str = str(Student_ID).split()
        Name_Full_str = str(Name_Full).split()
        Course_Full_str = str(Course_Full).split()

        #Dict
        Student_ID_key = Student_ID_str[0]
        Name_key = Name_Full_str[0]
        Course_key = Course_Full_str[0]
        Prelim_key = Prelim_str[0]
        Midterm_key = Midterm_str[0]
        Final_key = Final_str[0]
        Final_Average_key = Final_Average_str[0]
        emoji_key = result[0]

        data["1 : Student Number:       " + Student_ID_key] = \
        {

                2:"Name:                 " + Name_key.upper(),
                3:"Course:               " + Course_key.upper(),
                4:"Prelim Grade:         " + Prelim_key,
                5:"Midterm Grade:        " + Midterm_key,
                6:"Final Grade:          " + Final_key,
                7:"Final Average:        " + Final_Average_key,
                8:'Result:               ' + emoji_key,
                0:'#' * 66

        }
        for tab in data:
                print(tab)
                for tabs in data[tab]:
                        print(tabs, ":", data[tab][tabs])
        try_again()

def try_again():
        print('#' * 66)
        answer = input('Do you want to calculate again?:Yes/No ')
        print('#' * 66)
        if answer == 'Yes'or answer == "yes" or answer == "YES":
                register()
        elif answer == "No" or answer == "no" or answer == "NO":
                quit()

register()