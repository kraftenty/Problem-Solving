men = 26
men += 24
zazang = 5500
zambong = 6500
bok = 7000
yesan = men * 8000
print(f'예산:{yesan}')
menusum = zazang*7 + zambong*13 + bok*6
menusum += zazang*13 + zambong*7 + bok*4
print(f'총액:{menusum}')
print(f'남은금액:{yesan - menusum}')
print(f'군만두:{(yesan-menusum)/5000}개')
