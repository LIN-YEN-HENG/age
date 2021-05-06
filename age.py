driving = input('你開過車嗎?: ' )
if driving != '有' and driving != '沒有' :
	print('僅能輸入 有/沒有 喔<3')
	raise SystemExit

age = input('請問你的年齡?: ')
age = int(age)
if driving == '有':
	if age >= 18 :
		print('恭喜您,通過測驗')
	else:
		print('恩?奇怪! 你怎麼會開過車!')
elif driving == '沒有' :
	if age >= 18 :
		print('你可以考駕照了阿,怎麼還不去考')
	else :
		print('很好,再過幾年就可以考駕照了!')