# GRAAFISEN KÄYTTÖLIITTYMÄN PÄÄOHJELMA

# Kirjastojen lataukset
import kivy

# Alustukset: Kivy-kirjaston luokkien käyttöönotto
from kivy.app import App  # Varsinainen sovellusikkuna
from kivy.uix.gridlayout import GridLayout  # Sijoitteluruudukko
from kivy.uix.label import Label  # Tekstielementti
from kivy.uix.textinput import TextInput  # Tekstikenttä (syöttökenttä)
from kivy.uix.button import Button  # Painike

# Muodostetaan 2:n sarakkeen sijoitteluruudukko ja siihen tarvittavat käyttöliittymäelementit


class App_grid(GridLayout):
    """Grid layout definition and UI elements"""

    def __init__(self, **kwargs):  # **kwargs -> keyword arguments
        super().__init__(**kwargs)

        # Sarakkeiden määrä
        self.cols = 2

        # Käyttöliittymän elementit kentän nimi ja itse kenttä
        self.add_widget(Label(text='Etunimi'))  # Kentän nimen lisäys
        self.first_name = TextInput()  # Syöttökentän määritys
        self.add_widget(self.first_name)  # Kentän lisäys
        self.add_widget(Label(text='Sukunimi'))
        self.last_name = TextInput()
        self.add_widget(self.last_name)
        self.add_widget(Label(text='Pituus'))
        self.person_height = TextInput()  # height on varattu sana
        self.add_widget(self.person_height)
        self.add_widget(Label(text='Paino'))
        self.weight = TextInput()
        self.add_widget(self.weight)

        # Painike painoindeksin laskemiseksi
        self.submit = Button(text=' Laske')
        self.submit.font_size = 24
        # Tapahtuma on_press käynnistää pressed-metodin
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        # Tekstikenttä, johon lasketaan painoindeksi Laske-painikkeella, kenttä ei ole syöttökäytössä
        self.bmi = TextInput()
        self.add_widget(self.bmi)
        self.bmi.font_size = 24
        self.bmi.disabled = True

    # Laske-painikkeen toiminnot määrittelevä metodi

    def pressed(self, instance):
        p_height = float(self.person_height.text)
        p_weight = float(self.weight.text)
        p_bmi = p_weight / (p_height / 100)**2
        self.bmi.text = 'Painoindeksi on ' + str(round(p_bmi, 1))
        print('Ja taas laskettiin painoindeksi, joka oli tällä kertaa', p_bmi)


# Sovelluksen alustaminen: uusi luokka, joka perii App-luokan metodit, ei tarvita muodostinta
class Weight_app(App):
    """GUI for weight control application"""

    def build(self):
        return App_grid()


# Sovelluksen testaaminen
if __name__ == "__main__":
    # Sovelluksen käynnistäminen
    Weight_app().run()
