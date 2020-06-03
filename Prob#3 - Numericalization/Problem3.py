#Set the shape of each number. The shape of each number is stored in an array of 5 by 5
shape={'0':[['0','0','0','0','0'],['0',' ',' ',' ','0'],['0',' ',' ',' ','0'],['0',' ',' ',' ','0'],['0','0','0','0','0']],'1':[[' ',' ',' ',' ','1'],[' ',' ',' ',' ','1'],[' ',' ',' ',' ','1'],[' ',' ',' ',' ','1'],[' ',' ',' ',' ','1']],'2':[['2','2','2','2','2'],[' ',' ',' ',' ','2'],['2','2','2','2','2'],['2',' ',' ',' ',' '],['2','2','2','2','2']],'3':[['3','3','3','3','3'],[' ',' ',' ',' ','3'],['3','3','3','3','3'],[' ',' ',' ',' ','3'],['3','3','3','3','3']],'4':[['4',' ',' ',' ','4'],['4',' ',' ',' ','4'],['4','4','4','4','4'],[' ',' ',' ',' ','4'],[' ',' ',' ',' ','4']],'5':[['5','5','5','5','5'],['5',' ',' ',' ',' '],['5','5','5','5','5'],[' ',' ',' ',' ','5'],['5','5','5','5','5']],'6':[['6','6','6','6','6'],['6',' ',' ',' ',' '],['6','6','6','6','6'],['6',' ',' ',' ','6'],['6','6','6','6','6']],'7':[['7','7','7','7','7'],[' ',' ',' ',' ','7'],[' ',' ',' ',' ','7'],[' ',' ',' ',' ','7'],[' ',' ',' ',' ','7']],'8':[['8','8','8','8','8'],['8',' ',' ',' ','8'],['8','8','8','8','8'],['8',' ',' ',' ','8'],['8','8','8','8','8']],'9':[['9','9','9','9','9'],['9',' ',' ',' ','9'],['9','9','9','9','9'],[' ',' ',' ',' ','9'],['9','9','9','9','9']]}

#Function to numericalize
def numericalize(n,m1,m2):

    #Set space between each number
    space=1*m2
    #Change input n to string for easier handling 
    num=str(n)
    #Empty string to store result
    result=""

    #1st Line: Repeat the process of creating first line for m1 times to achieve the desired height 
    for height_n in range(m1):
        #Loop through each digit in the input n
        for n in num:
            #Get the num shape of the digit and iterate to get the desired width
            for char in shape[n][0]:
                for x in range(m2):
                    result+=char
            for x in range(space):
                result+=' '
        result+='\n'

    #2nd Line: Repeat the process of creating second line for m1 times to achieve the desired height 
    for height_n in range(m1):
        for n in num:
            for char in shape[n][1]:
                for x in range(m2):
                    result+=char
            for x in range(space):
                result+=' '
        result+='\n'

    #3rd Line: Repeat the process of creating third line for m1 times to achieve the desired height 
    for height_n in range(m1):
        for n in num:
            for char in shape[n][2]:
                for x in range(m2):
                    result+=char
            for x in range(space):
                result+=' '
        result+='\n'

    #4th Line: Repeat the process of creating fourth line for m1 times to achieve the desired height 
    for height_n in range(m1):
        for n in num:
            for char in shape[n][3]:
                for x in range(m2):
                    result+=char
            for x in range(space):
                result+=' '
        result+='\n'

    #5th Line: Repeat the process of creating fifth line for m1 times to achieve the desired height 
    for height_n in range(m1):
        for n in num:
            for char in shape[n][4]:
                for x in range(m2):
                    result+=char
            for x in range(space):
                result+=' '
        result+='\n'
    print(result)

#Set variable to generate numericalization
n=141016
m1=2
m2=4

#Run nemericalization
numericalize(n,m1,m2)
    