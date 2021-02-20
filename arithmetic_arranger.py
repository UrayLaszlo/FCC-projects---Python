def arithmetic_arranger(problems):
#turn to list of small lists
    '''
    converted_problems = [list(x) for x in problems]

    first_num = problems[0][0:str(problems).find(' ')-2]
    operand = problems[0][str(problems).find(first_num):str(problems).find(' ')].lstrip()
    second_num = problems[0][str(problems).find(operand):].lstrip() 
    '''
    if len(problems) > 5:
        return "Error: Too many problems."

    for x in problems:
        sep_problems = x.split()
        num_1 = sep_problems[0]
        operator = sep_problems[1]
        num_2 = sep_problems[2]

    if not num_1.isdigit() or not num_2.isdigit():
        return "Error: Numbers must only contain digits."

    if operator != "+" or operator != "-":
      return "Error: Operator must be '+' or '-'."
    
    if len(num_2) > 4 or len(num_1) > 4:
        return "Error: Numbers cannot be more than four digits."

    result = 0
    if operator == "+":
        result = int(num_1) + int(num_2)
    elif operator == "-":
        result = int(num_1) - int(num_2)
    
    arranged_problems = None
    if False:
        arranged_problems = num_1 + '\n' + operator + ' ' + num_2 + '\n' + '---'
    else: 
        arranged_problems = num_1 + '\n' + operator + ' ' + num_2 + '\n' + '---' + '\n' + str(result)

    return arranged_problems

arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
#expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
#expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
#expected = "Error: Too many problems."
arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
#expected = "Error: Operand must be '+' or '-'."
arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
#expected = "Error: Numbers cannot be more than four digits."
arithmetic_arranger(["98 + 3g5"])#, "3801 - 2", "45 + 43", "123 + 49"])
#expected = "Error: Numbers must only contain digits."
arithmetic_arranger(["32 - 698"])#, "1 - 3801", "45 + 43", "123 + 49"], True)
#expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
'''    
    if len(problems) > 5:
        return "Error: Too many problems."

    problems_arr = []

    for x in problems:
        problems_arr.append(x.split())

    row_1 = []
    row_2 = []
    row_4 = []
    row_5 = []

    row_1.append(int(problems_arr[0][0]))
    row_1.append(int(problems_arr[1][0]))
    row_1.append(int(problems_arr[2][0]))
    row_1.append(int(problems_arr[3][0]))

    row_2.append(problems_arr[0][1])
    row_2.append(int(problems_arr[0][2]))
    row_2.append(problems_arr[1][1])
    row_2.append(int(problems_arr[1][2]))
    row_2.append(problems_arr[2][1])
    row_2.append(problems_arr[2][2])

    row_3 = '-' * len(row_2)
    
    num_1 = problems_arr[0][0]
    num_2 = None
    operand = None
    
    print(row_1, '\n' , row_2, '\n', row_3, '\n', end=' ')
    #return arranged_problems
    '''