import gspread
from functions import *

print('Log: Importing API...')

print('Log: Accessing credentials...')
gc = gspread.service_account(filename='credentials.json')

key = input("Insert the id of Google sheets (Remember of activated the permission of sharing): ")
print('Opening by key...')
sh = gc.open_by_key(key)

# Key for "Desafio Engenharia de Software Roger Henrique": 1xxeSlOAtpVdna-dxAGQUCJ-ame3eEfKhiM7C3H9ppcU

print('Log: Selecting the sheet...')
worksheet = sh.sheet1
print('Log: Getting the values...')
students = worksheet.get_all_values()

maximum = len(students)
print('Catch', maximum - 3, 'Students')

for x in range(3, maximum):
    # Important convert the string in INT to do the calculations
    avg = ((int(students[x][3]) + int(students[x][4]) + int(students[x][5])) / 3) / 10
    # My function to round UP
    if int(students[x][2]) <= 15:
        if avg < 5:
            worksheet.update_cell(x + 1, 7, 'Reprovado')
        elif avg < 7:
            worksheet.update_cell(x + 1, 7, 'Exame Final')
            # Generating NAF
            naf = generate_naf(avg)
            naf = round_roger(naf)
            worksheet.update_cell(x + 1, 8, naf)

        elif avg >= 7:
            worksheet.update_cell(x + 1, 7, 'Aprovado')
    else:
        worksheet.update_cell(x + 1, 7, 'Reprovado por Falta')

    # Now will verify the situation of the students to put the NAF
    if worksheet.cell(x + 1, 7).value != 'Exame Final':
        worksheet.update_cell(x + 1, 8, 0)

    print('Evaluating Student: ', x-2, '/', maximum-3,)

print('Log: Done! Closing the program...')
