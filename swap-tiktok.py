import requests , uuid , time 
uid = uuid.uuid4()
r = requests.session()

print("""
███████ ██     ██
██      ██     ██
███████ ██  █  ██
     ██ ██ ███ ██
███████  ███ ███ ╔╦╗┬ ┬┌─┌┬┐┌─┐ ┬┌─  
                  ║ │ ├┴┐ │ │ │ ├┴┐  
                  ╩ ┴ ┴ ┴ ┴ └─┘ ┴ ┴  
         By JOKER @t.uo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
print('لا تنسى وضع السيشن ايدي بملف باسم sessionid.txt بتوفيق')
print('\t')
user = input("[•] >> Enter Username : ")
print('\n')
def Login():
	def SWAP():
		file = open('sessionid.txt','r')
		ess = file.readline().split('\n')[0]
		while True:
			headers = {
				'Host': 'api16-normal-c-alisg.tiktokv.com',
				'Content-Length': '25',
				'Connection': 'close',
				'Cookie': f'sessionid={ess}',
				'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
				"x-tt-passport-csrf-token": f"{ess}",
				'Content-Type': 'application/x-www-form-urlencoded',
				'passport-sdk-version': '5.12.1',
				'sdk-version': '2'}
			url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'	
			data = {
				'login_name': f'{user}'}		
			GO2 = r.post(url,headers=headers,data=data)
			if '"message":"success"' in GO2.text:
					print(f'\n[+] SWAP user -> {user}')
					print('\n\t By JOKER @t.uo')
					exit()
			elif '"login_name"' in GO2.text:
					print(f'\n[+] SWAP user -> {user}')
					print('\n\t By JOKER @t.uo')
					exit()
			elif '"message":"error"' in GO2.text:
					print(f'[-] Not SWAP user -> {user}')
			else:
				print('\t\t\tERORR !!')
	def myPRV():
		print('what are you looking for ? hhh')
	def tiktok():
		j = 1
		while True:
			urCH = f'https://www.tiktok.com/@{user}?'
			hedCH = {
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'cache-control': 'max - age = 0',
				'sec-ch-ua': '"Google Chrome";v = "89", "Chromium";v = "89", ";Not A Brand";v = "99"',
				'sec-ch-ua-mobile': '?0',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'none',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
			go1 = r.get(urCH,headers=hedCH)
			if go1.status_code == 404:
				print(f'\n[+] Hacked user {user}')
				SWAP()
			elif go1.status_code == 200:
				print(f'[{j}] Not Hacked user {user}')	
			else:
				print('The connection has been blocked !!')
			j += 1
	tiktok()
Login()

"""  الاداة مجانية و لا احلل لمن يبيعها """
"""  بتاخذها ؟ اذكر المصدر لانيجك @vv1ck """
