import webapp2, random

def makep(string):
    return "<p>" + string + "</p>"
    
def genFortune():
    flist = [
        "You will die tomorrow.",
        "You will fight a bear and lose.",
        "You will fight a bear and win.",
        "You will meet Toilet Hanako.",
        "You will be smooched by a ghost.",
        "You will stop asking the internet to tell your future.",
        "You will go to space.",
        "You will live peacefully in Okinawa and everyone will love you."
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
