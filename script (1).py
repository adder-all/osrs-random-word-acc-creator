import requests
from time import sleep
import random
from random_word import RandomWords
r = RandomWords() 
import time
NUMBER = 112  #this is not necessary anymore
MADE = 0
AMOUNT_TO_MAKE = 40 #idk what's this for, just make like 1000000 accounts in one go xD
 

PASSWORD = "hammalol";

ALL_DOMAINS=['@pm.me', '@yahoo.com', '@protonmail.com', '@protonmail.ch'] #just add more domains between '' and sperated by , if you want ;)



def getmail():
    wordlist=[]

    while len(wordlist) <2:
        try:
          wordlist= r.get_random_words(limit=2,minLength=3,maxLength=5)
        except:
            print("Unable to get words, waiting patiently for the next words ;)")
            time.sleep(10)
            getmail()
    

    return (wordlist[0]+wordlist[1])
 
#email would be dad+number@gmail.com --------------------- not anymore xD

def saveaccount(account): #save to file
    f = open("accounts.txt", "a")
    f.write(str(account.get_email()) + ":" + str(account.get_password()) + "\n")
    f.close()



class account:
 
     def __init__(self, e,  p, end): #removed the n parameter, not necessary ;)
        self.email = e  + end
        self.password = p
 
     def get_email(self):
        return self.email
 
     def get_password(self):
        return self.password
 
class create:
 
    def create(account):
        a = account
 
        APIKEY = "c31e886e6da074043f6f3036deadf57e";
        SITEKEY = "6Lcsv3oUAAAAAGFhlKrkRb029OHio098bbeyi_Hv";
        URL = "https://secure.runescape.com/m=account-creation/create_account?theme=oldschool"
        print("\n")
        print(a.get_email())

        print(a.get_password())
 
        s = requests.Session()
 
        global NUMBER
        global MADE
        time.sleep(10)
       
        
        #2captcha api shit
        captcha_id = s.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageURL={}".format(
            APIKEY, SITEKEY, URL)).text.split('|')[1]
 
        recaptcha_answer = s.get(
            "http://2captcha.com/res.php?key={}&action=get&id={}".format(APIKEY, captcha_id)).text
        print("Getting captcha...")
        while 'CAPCHA_NOT_READY' in recaptcha_answer:
            sleep(5)
            recaptcha_answer = s.get(
                "http://2captcha.com/res.php?key={}&action=get&id={}".format(APIKEY, captcha_id)).text
        if ('ERROR_CAPTCHA_UNSOLVABLE' not in recaptcha_answer):
            recaptcha_answer = recaptcha_answer.split('|')[1]
            #end of 2captcha api shit
 
            data = {'theme':'oldschool',
                    'email1':a.get_email(),
                    'onlyOneEmail':1,
                    'password1':a.get_password(),
                    'onlyOnePassword':1,
                    'day':'01',
                    'month':'01',
                    'year':'1990pip3 ',
                    'create-submit':'create',
                    'g-recaptcha-response':recaptcha_answer}
 
            headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
 
            session = requests.Session()
            r = session.post(url = URL, headers = headers, data = data)
            #print(r.text)
            if ('You can now begin your adventure with your new account.' not in r.text):
                print("Failed to create account.")
                NUMBER += 1
                
            else:
                saveaccount(a)
                print("Account created!")
                NUMBER += 1
                print("Made so far: "+str(MADE))
                
                MADE += 1
   
    while (MADE <= AMOUNT_TO_MAKE):

       
        email_start = getmail()
        number = random.randint(1,9)
        email_domain = ALL_DOMAINS[(random.randint(0,len(ALL_DOMAINS)-1))]
        


        create(account(email_start+str(number), PASSWORD, email_domain));

