def arithmetic_arranger(problems, show=False):
    
    #dealing with errors
    if len(problems) > 5:
        return "Error: Too many problems."
    
    #lines
    line1 = ""
    line2 = ""
    line3 = ""
    result = ""


    
    for problem in problems:
        value = problem.split()
        if value[1] == "+":
            add = True
        elif value [1] == "-":
            add = False
        else:
            return "Error: Operator must be '+' or '-'."
        
        if not value[0].isdigit() or not value[2].isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(value[0]) > 4 or len(value[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        #["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
        #formating vars
        longest_num = ""
        dif_len_num = 0
        if len(value[0]) > len(value[2]):
            longest_num = value[0]
            dif_len_num = len(value[0]) - len(value[2])
            first = True
        else:
            longest_num = value[2]
            dif_len_num = len(value[2]) - len(value[0])
            first = False

        #formating 
        if len(line1) > 0:
            line1 += "    "
            line2 += "    "
            line3 += "    "
         

        if first is False:
            line1 += ("  " + " "*dif_len_num + str(value[0]))
            line2 += (str(value[1]) + " " + str(value[2]))
        else:
            line1 += ("  " + str(value[0]))
            line2 += (str(value[1]) + " " + " "*dif_len_num + str(value[2]))

        line3 += "-"*(len(longest_num) + 2)

    
        #show results
        if show:

            if len(result) > 0:
                result += "    "

            if add is True:
                res = int(value[0]) + int(value[2])
                result += str(res).rjust(len(line3) - len(result))
            else:
                res = int(value[0]) - int(value[2])
                result += str(res).rjust(len(line3) - len(result))

    return line1 + "\n" + line2 + "\n" + line3 + ("\n" + str(result) if show else "")


#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))