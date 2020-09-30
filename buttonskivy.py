"""Multiple buttons"""

#import random
from random import *
from kivy.app import App 
#related to UI
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 

#from random import shuffle
#declare global variabkes
#RGB array
red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 1, 1, 1]
purple = [1, 1, 1, 1] 

#purple adds something to it
#may be You need a totally complete row for color xchange

#padding = padding_left, padding_right, padding_top, padding_bottom
class ButtonsApp(App):
	
	def build(self):
		padding = [50, 40, 20, 30]
		layout = BoxLayout(padding = padding)
		colors = [red, green, blue, purple] 



		for i in range(7):
			#option = random.randint(i, 7)
			#shuffle returns None type
			shuffle(colors)
			button = Button(text="Colored Button #%s" % (i),
                         background_color=choice(colors)
                         )
			button.bind(on_press=self.onButtonClick)
			layout.add_widget(button)
		#add to layout
		return layout	

	def onButtonClick(self, instance):
		colors = [red, blue, green, purple]
		shuffle(colors)
		self.background_color = choice(colors)


def main():
	newapp = ButtonsApp() 
	newapp.run() 

if __name__ == "__main__":
	main()   
