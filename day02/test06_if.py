# date : 20240130
# desc : 여러조건 if문

date = input('날짜 입력(예 : 12-31) > ') # '12-31'(문자열)

month = date.split('-')[0] # '12'
day = date.split('-')[1] # '31'

if month == '12' and day == '25': # 12월 25일
    print('메리 크리스마스!!')
elif month == '01' and day == '01': # 1월 1일
    print('해피 뉴이어~!!')
elif month == '04' and day == '14': # 4월 14일
    print('오늘은 블랙데이~ 짜장면 먹는날!!')
else:
    print('보통날입니다')