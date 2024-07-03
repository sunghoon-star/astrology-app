import random

class AstrologyApp:
    def __init__(self):
        self.zodiac_signs = ["양자리", "황소자리", "쌍둥이자리", "게자리", "사자자리", "처녀자리", 
                             "천칭자리", "전갈자리", "사수자리", "염소자리", "물병자리", "물고기자리"]
        self.fortunes = ["행운이 찾아올 것입니다", "새로운 기회가 올 것입니다", "조심해야 할 때입니다", 
                         "긍정적인 변화가 있을 것입니다", "어려움을 극복할 것입니다"]

    def get_zodiac_sign(self, month, day):
        # 이 부분에 실제 별자리 계산 로직을 구현해야 합니다
        return random.choice(self.zodiac_signs)

    def get_daily_horoscope(self, zodiac_sign):
        return f"{zodiac_sign}의 오늘의 운세: {random.choice(self.fortunes)}"

    def run(self):
        print("점성술 어플에 오신 것을 환영합니다!")
        month = int(input("태어난 달을 입력하세요 (1-12): "))
        day = int(input("태어난 날짜를 입력하세요 (1-31): "))
        
        zodiac_sign = self.get_zodiac_sign(month, day)
        horoscope = self.get_daily_horoscope(zodiac_sign)
        
        print(horoscope)

if __name__ == "__main__":
    app = AstrologyApp()
    app.run()
  
