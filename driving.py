#你是哪國人 
#你幾歲
#在台灣 滿18可以考駕照
#在美國 滿16可以考駕照

place = input ('請問你是"美國人"還是"台灣人"呢?')
age = input ('請問你今年幾歲?')
age = float (age)

if place == '台灣人' or '台灣' or '台' :
	if age >= 18 :
		print ('恭喜你已滿', age, ',考到駕照就可以開車了!')
	else :
		print ('抱歉', age, '歲,還不能開車喔')
elif  place == '美國人' or '美國' or '美' :
	if age >= 16 :
		print ('恭喜你已滿', age, ',考到駕照就可以開車了!')
	else :
		print ('抱歉', age, '歲,還不能開車喔')
elif place != '台灣人' or '台灣' or '台' or '美國人' or '美國' or '美' :
	print('糟了,我不知道', place, '幾歲才能夠開車，請你網路google喔')