from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

#Loads the kivy file
Builder.load_file('frontend.kv')

#Creates a class for the first screen, will do one for every screen
class FirstScreen(Screen):
    def get_image_link(self):
        #Get user query from text input
        query = self.manager.current_screen.ids.user_query.text
        #Get wikipedia page and first image url
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link
    
    def download_image(self):
        #Download the image
        headers = {'User-agent': 'Mozilla/5.0'} # Use any browser you want
        req = requests.get(self.get_image_link(), headers=headers)
        image_path = 'files/image.png'
        with open(image_path, 'wb') as file:
            file.write(req.content)
        return image_path
    
    def set_image(self):
        #Set the image in the image qidget
        self.manager.current_screen.ids.img.source = self.download_image()


#Creates the RootWidget, subclass of ScreenManager (neccesary) 
class RootWidget(ScreenManager):
    pass

#Creates the MainApp, subclass of App (neccesary)
class MainApp(App):

    def build(self):
        return RootWidget()

#Runs the MainApp
MainApp().run() 


