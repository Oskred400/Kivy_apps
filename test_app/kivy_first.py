#my forst app in kivy 
#for android install buildozer on linux 

from kivy.app import App 
from kivy.uix.button import Button 

class MainApp(App):
	def build(self):
		#define button properties
		button = Button(text='Hello World',
		                        size_hint=(.3, .3),
		                        pos_hint={'center_x': .5, 'center_y': .5})

		button.bind(on_press=self.onButtonClick)
		# return button 
		return button

	def onButtonClick(self, instance):
		print("button is pressed") 


class ButtonkvApp(App):
	def build(self):
		##define button properties in .kv file 

		button = Button() 
		return button 

	def onbclick(self):
		print("button pressed") 





def main():
	#newapp = MainApp()
	newapp = ButtonkvApp()
	newapp.run() 

if __name__ == "__main__":
	main()


