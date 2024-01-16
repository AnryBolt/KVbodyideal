from kivymd.app import MDApp
from kivy.storage.jsonstore import JsonStore
from kivy.config import Config
from kivy.graphics.svg import Window

#x = 260
#Window.size = (x, 2.2*x)

Config.set('graphics', 'version', '2.1')
data = JsonStore('data.json')

class BodyidealApp(MDApp):
        

        def build (self):
                
                self.icon = 'icon.png'

                # Заполняем виджеты MyTextFieldRect соответствующими значениями
                self.root.ids.rost.text = data.get('rost')['value']
                self.root.ids.golova.text = data.get('golova')['value']
                self.root.ids.sheya.text = data.get('sheya')['value']
                self.root.ids.plechi.text = data.get('plechi')['value']
                self.root.ids.biceps.text = data.get('biceps')['value']
                self.root.ids.grud.text = data.get('grud')['value']
                self.root.ids.talia.text = data.get('talia')['value']
                self.root.ids.bedra.text = data.get('bedra')['value']

        def on_save(self):

                # Создаем словарь со значениями
                sl = {
                'rost': self.root.ids.rost.text,
                'golova': self.root.ids.golova.text,
                'sheya': self.root.ids.sheya.text,
                'plechi': self.root.ids.plechi.text,
                'biceps': self.root.ids.biceps.text,
                'grud': self.root.ids.grud.text,
                'talia': self.root.ids.talia.text,
                'bedra': self.root.ids.bedra.text
                }

                # Сохраняем данные в файл JSON
                for key, value in sl.items():
                        data.put(key,value=value)


        def calculate(self, *args):

                if any(i == '' for i in args):
                        return "Введите значения для всех полей"
                else:

                        sp = rost, golova, sheya, plechi, biceps, grud, talia, bedra = [int(i) for i in args]

                        grud_talia = f'''Соотношение талия/грудь: {round(talia/grud,2)}; \nИдеальное: 0.7; \nРекомендации: {f'меньше грудь {round(talia/0.7,2)} или больше талию {round(grud*0.7,2)}' if round(talia/grud,2) < 0.7 - 0.7 * 0.03 else f'больше грудь {round(talia/0.7,2)} или меньше талию {round(grud*0.7,2)}' if round(talia/grud,2) > 0.7 + 0.7 * 0.03 else 'отлично!'}'''

                        rost_golova =  f'''Соотношение рост/голова: {round(rost/golova,2)}; \nИдеальное: 8 или более; \nРекомендации: {'больше роста! или меньше голову' if rost/golova < 8 - 8 * 0.03 else 'Отлично!'}'''

                        sheya_tolsh = f'''Толщина шеи: {sheya}; \nИдеальная: чем толще, тем лучше'''

                        plechi_bedra = f'''Соотношение плечи/бедра: {round(plechi/bedra,2)}; \nИдеальное: чем шире плечи, тем лучше; \nРекомендации: {'Хорошо' if plechi > bedra + bedra * 0.03 else 'Шире плечи или меньше бедра'}'''

                        bedra_talia = f'''Соотношение бедра/талия:{round(bedra/talia,2)}; \nИдеальное: талия > бедер; \nРекомендации: {'Хорошо' if talia > bedra + bedra * 0.03 else 'Шире талию или меньше бедра'}'''



                        return f'''{grud_talia}\n\n{rost_golova}\n\n{sheya_tolsh}\n\n{plechi_bedra}\n\n{bedra_talia}'''

if __name__=='__main__':
        BodyidealApp().run()
