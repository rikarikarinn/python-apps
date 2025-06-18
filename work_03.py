import random

food = {'鳥刺し':'鹿児島',
        'モツ鍋':'福岡',
        '生牡蠣':'広島',
        'カレー':'石川',
        'カニ':'北海道',
        'もんじゃ':'東京',
        '手羽先':'愛知',
        'たこ焼き':'大阪',
        '海ぶどう':'沖縄',
        'とろろ':'静岡',
        'ほうとう':'山梨',
        'きび団子':'岡山',
        'みかん':'愛媛',
        'うどん':'香川',
        'ふぐ':'山口',
        'たまごパン':'長野'}

print("名産品の名前が表示され、それがどの都道府県の特産かを当てるクイズ")

meisan, prefecture = random.choice(list(food.items()))

print(f"{meisan} はどこの都道府県の名産品？")

answer = input("答え:").strip()

if answer == prefecture:
    print("正解！")
else:
    print(f"不正解 正解は{prefecture}")