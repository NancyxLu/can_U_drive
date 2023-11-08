#你是哪國人 
#你幾歲
#在台灣 滿18可以考駕照
#在美國 滿16可以考駕照

place = input ('請問你是台灣人還是美國人?  請輸入:')
age = input ('請問你今年幾歲?  請輸入:')
age = float (age)

if place in ['台灣', '台', 'taiwan', '台灣人']:
	if age >= 18 :
		print ('恭喜你已滿', age, ',考到駕照就可以開車了!')
	else :
		print ('抱歉', age, '歲,還不能開車喔')
elif  place in ['美國', '美', '美國人', 'USA']:
	if age >= 16 :
		print ('恭喜你已滿', age, ',考到駕照就可以開車了!')
	else :
		print ('抱歉', age, '歲,還不能開車喔')
else :
	print('糟了,我不知道', place, '幾歲才能夠開車，請你網路google喔')