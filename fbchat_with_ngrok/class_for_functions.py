class Functions:
    def __init__(self, ACCESS_TOKEN):
        self.ACCESS_TOKEN = ACCESS_TOKEN



    def function1(self, user_id):
        import time
        t = time.localtime()
        self.value = time.strftime("%H:%M:%S", t)

    def function2(self, user_id):
        
        from bot import Bot
        import time

        #RICK ASTLEEEEY#

        bot = Bot(self.ACCESS_TOKEN)
        bot.send_text_message(user_id, "We're no strangers to love\nYou know the rules and so do I\nA full commitment's what I'm thinking of\nYou wouldn't get this from any other guy")
        time.sleep(1)
        bot.send_text_message(user_id, "I just wanna tell you how I'm feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down")
        time.sleep(1)
        bot.send_text_message(user_id, 'Never gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you')
        bot.send_image_by_id(user_id, '329441454964466')

    
    def function3(self, user_id):
        #RACOOOON

        from bot import Bot

        bot = Bot(self.ACCESS_TOKEN)
        bot.send_image_by_id(user_id, '4252880948086447')

    def function4(self, user_id):
        from bs4 import BeautifulSoup
        import requests

        r = requests.get('https://www.idokep.hu/30napos/Budapest')


        soup = BeautifulSoup(r.content, 'lxml')

        wrap_homerseklet = soup.find_all('p', class_="zivatar-text")
        wrap_honap = soup.find_all('p', class_="atlag-info")

        kozos = []
        while_loop = 0

        while int(while_loop) <= 10:
            kozos.append(wrap_homerseklet[while_loop].text + "-------")
            kozos.append(wrap_honap[while_loop].text)
            while_loop  = while_loop + 1
        kozos.remove(kozos[0])
        self.value = ('\n'.join(map(str, kozos)))