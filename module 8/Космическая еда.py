buckwheat = 100
expenditure = 4
months = buckwheat // expenditure
for i in range(1, months):
    remains = buckwheat - expenditure * i
    print('В конце', i, 'месяца осталось', remains, 'килограмм')