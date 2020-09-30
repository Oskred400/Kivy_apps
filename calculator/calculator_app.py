##boiler plate code

from kivy.app import App 

from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.gridlayout import GridLayout 


symbols = ['+','-','*','/', '%', '=']
##class
##choose grid layout
class CalcApp(App):
	def build(self):

		box = BoxLayout(orientation = "vertical")
		text_box = TextInput(font_size = 50, 
                      size_hint_y = None, 
                      height = 100) 
		box.add_widget(text_box)

		layout = GridLayout(cols = 3)
		##create a text box here fppr text input 

		 
		#layout.add_widget(text_box)
		for i in range(0,10,1):
			button = Button(text = str(i), background_color = [0,1,0,1])
			layout.add_widget(button)
		
		for i in symbols:
			symbol_button = Button(text = i, background_color = [0,1,0,1])
			layout.add_widget(symbol_button)

		box.add_widget(layout)
		return box

	
	def on_click_button(self, instance):
		pass	
		##set the text_box to have whatever we have here



def main():
	calcapp = CalcApp() 
	calcapp.run() 

if __name__ == "__main__":
	main()