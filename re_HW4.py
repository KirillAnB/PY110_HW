import re


# адресс электронной почты
mail_pattern = re.compile(r'\b[A-Za-z_]+@[A-Za-z-_]+\.(?:ru|com|net|org)\b')
mobile_pattern = re.compile(r'\+?[7|8]\S\d{3}\S\d{3}\S\d{2}\S\d{2}')
bank_card_pattern = re.compile(r'\b\d{4}\s\d{4}\s\d{4}\s\d{4}\b')
ipv4_pattern = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')
url_pattern = re.compile(r'\b(www\.[a-z0-9-_]+\.(?:ru|com|org|net))\b')
str_="""Мой номер +7-950-013-71-60,8-950-013-71-61,моя почта rahya@mail.ru и it-reso@mail.ru
    Номер моей карты ммм-банка 5460 5500 5555 7777. Адрес моего компьютера 8.8.8.8
    Мой сайт www.home-lab.net"""

mobile_match = re.findall(mobile_pattern, str_)
mail_match = re.findall(mail_pattern,str_)
bank_card_match = re.findall(bank_card_pattern, str_)
ipv4_match = re.findall(ipv4_pattern, str_)
url_match = re.findall(url_pattern, str_)[0]

print(mobile_match, mail_match, bank_card_match, ipv4_match, url_match)