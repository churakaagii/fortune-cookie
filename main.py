import webapp2, random

def makep(string):
    return "<p>" + string + "</p>"
    
def genFortune():
    flist = [
        "You will die tomorrow.",
        "Do not fight a bear; you will lose.",
        "Absolutely fight a bear; you will win and it will be super cool.",
        "When next you pee, you will meet Toilet Hanako.",
        "Always smooch ghosts.",
        "Stop asking the internet to tell your future.",
        "The future is in plastics.",
        "You will live peacefully in Okinawa and everyone will love you.",
        "Your true love is in Beirut.",
        "If you steal the Declaration of Independence, you will not find treasure; you will get arrested.",
        "The next time you look for something lost, it will be in the fridge.",
        "You should marry the next person who asks you the time."
    ]

    return flist[random.randrange(len(flist))]

def makeStrong(string):
    return "<strong>" + string + "</strong>"

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"
        
        fortune = makep("Your fortune: " + makeStrong(genFortune()))
        
        luckynum = random.randint(1, 100)
        luckysen = makep("Your lucky number: " + makeStrong(str(luckynum)))
        
        refrbutton = "<a href='.'><button>Try another fortune!</button></a>"
        
        content = header + fortune + luckysen + refrbutton
        self.response.write(content)
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
