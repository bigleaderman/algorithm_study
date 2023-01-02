month, day, year, hour, minute = input().replace(',', "").replace(':', " ").split()
month_word = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


# 윤년인지 판단
conf = 1
year = int(year)
if not year % 400:
    conf = 0
elif not year % 4 and year %100:
    conf = 0

if conf:
    month_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_minute = 365 * 24 * 60
else:
    month_count = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_minute = 366 * 24 * 60

count = 0

count += sum(month_count[0:month_word.index(month)]) * 24 * 60
count += (int(day)-1) * 24 * 60
count += int(hour) * 60
count += int(minute)

print(count/total_minute * 100)
