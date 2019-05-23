from django import forms
 
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())

class ItemBlockView:
    def __init__(self,item, score,img):
        self.item = item
        self.score = score
        self.img = img

        if int(self.item.item_id) < 100:
            self.img = 'login/images/c1.jpg'
        elif int(self.item.item_id) < 200:
            self.img = 'login/images/c2.jpg'
        elif int(self.item.item_id) < 300:
            self.img = 'login/images/c3.jpg'
        elif int(self.item.item_id) < 400:
            self.img = 'login/images/c4.jpg'
        elif int(self.item.item_id) < 500:
            self.img = 'login/images/c5.jpg'
        elif int(self.item.item_id) < 600:
            self.img = 'login/images/c6.jpg'
        elif int(self.item.item_id) < 700:
            self.img = 'login/images/c7.jpg'
        elif int(self.item.item_id) < 800:
            self.img = 'login/images/c8.jpg'
        elif int(self.item.item_id) < 900:
            self.img = 'login/images/c9.jpg'
        elif int(self.item.item_id) < 1000:
            self.img = 'login/images/c10.jpg'
        elif int(self.item.item_id) < 1100:
            self.img = 'login/images/c11.jpg'
        elif int(self.item.item_id) < 1200:
            self.img = 'login/images/h4.jpg'
        elif int(self.item.item_id) < 1300:
            self.img = 'login/images/h5.jpg'
        elif int(self.item.item_id) < 1400:
            self.img = 'login/images/h6.jpg'
        elif int(self.item.item_id) < 1500:
            self.img = 'login/images/h7.jpg'
        elif int(self.item.item_id) < 1600:
            self.img = 'login/images/h8.jpg'
        elif int(self.item.item_id) < 1700:
            self.img = 'login/images/h9.jpg'
        elif int(self.item.item_id) < 1800:
            self.img = 'login/images/h10.jpg'
        elif int(self.item.item_id) < 1900:
            self.img = 'login/images/h11.jpg'
        elif int(self.item.item_id) < 2000:
            self.img = 'login/images/h12.jpg'
        elif int(self.item.item_id) < 2100:
            self.img = 'login/images/m1.jpg'
        elif int(self.item.item_id) < 2200:
            self.img = 'login/images/m2.jpg'
        elif int(self.item.item_id) < 2300:
            self.img = 'login/images/m3.jpg'
        elif int(self.item.item_id) < 2400:
            self.img = 'login/images/m4.jpg'
        elif int(self.item.item_id) < 2500:
            self.img = 'login/images/m5.jpg'
        elif int(self.item.item_id) < 2600:
            self.img = 'login/images/m6.jpg'
        elif int(self.item.item_id) < 2700:
            self.img = 'login/images/m7.jpg'
        elif int(self.item.item_id) < 2800:
            self.img = 'login/images/m8.jpg'
        elif int(self.item.item_id) < 2900:
            self.img = 'login/images/m9.jpg'
        elif int(self.item.item_id) < 3000:
            self.img = 'login/images/m10.jpg'
        elif int(self.item.item_id) < 3100:
            self.img = 'login/images/m11.jpg'
        elif int(self.item.item_id) < 3200:
            self.img = 'login/images/m12.jpg'
        elif int(self.item.item_id) < 3300:
            self.img = 'login/images/m13.jpg'
        elif int(self.item.item_id) < 3400:
            self.img = 'login/images/m14.jpg'
        elif int(self.item.item_id) < 3500:
            self.img = 'login/images/m15.jpg'
        elif int(self.item.item_id) < 3600:
            self.img = 'login/images/m16.jpg'
        elif int(self.item.item_id) < 3700:
            self.img = 'login/images/m17.jpg'
        elif int(self.item.item_id) < 3800:
            self.img = 'login/images/m18.jpg'
        elif int(self.item.item_id) < 3900:
            self.img = 'login/images/m19.jpg'
        elif int(self.item.item_id) < 4000:
            self.img = 'login/images/m20.jpg'
            
class ListMovieRated:
    def __init__(self,item,score,myscore,img):
        self.item = item
        self.score = score
        self.myscore = myscore

        if int(self.item.item_id) < 100:
            self.img = 'login/images/n1.jpg'
        elif int(self.item.item_id) < 200:
            self.img = 'login/images/n2.jpg'
        elif int(self.item.item_id) < 300:
            self.img = 'login/images/n3.jpg'
        elif int(self.item.item_id) < 400:
            self.img = 'login/images/n4.jpg'
        elif int(self.item.item_id) < 500:
            self.img = 'login/images/n5.jpg'
        elif int(self.item.item_id) < 600:
            self.img = 'login/images/n6.jpg'
        elif int(self.item.item_id) < 700:
            self.img = 'login/images/n7.jpg'
        elif int(self.item.item_id) < 800:
            self.img = 'login/images/n8.jpg'
        elif int(self.item.item_id) < 900:
            self.img = 'login/images/n9.jpg'
        elif int(self.item.item_id) < 1000:
            self.img = 'login/images/n10.jpg'
        elif int(self.item.item_id) < 1100:
            self.img = 'login/images/n11.jpg'
        elif int(self.item.item_id) < 1200:
            self.img = 'login/images/h4.jpg'
        elif int(self.item.item_id) < 1300:
            self.img = 'login/images/h5.jpg'
        elif int(self.item.item_id) < 1400:
            self.img = 'login/images/h6.jpg'
        elif int(self.item.item_id) < 1500:
            self.img = 'login/images/h7.jpg'
        elif int(self.item.item_id) < 1600:
            self.img = 'login/images/h8.jpg'
        elif int(self.item.item_id) < 1700:
            self.img = 'login/images/h9.jpg'
        elif int(self.item.item_id) < 1800:
            self.img = 'login/images/h10.jpg'
        elif int(self.item.item_id) < 1900:
            self.img = 'login/images/h11.jpg'
        elif int(self.item.item_id) < 2000:
            self.img = 'login/images/h12.jpg'
        elif int(self.item.item_id) < 2100:
            self.img = 'login/images/m1.jpg'
        elif int(self.item.item_id) < 2200:
            self.img = 'login/images/m2.jpg'
        elif int(self.item.item_id) < 2300:
            self.img = 'login/images/m3.jpg'
        elif int(self.item.item_id) < 2400:
            self.img = 'login/images/m4.jpg'
        elif int(self.item.item_id) < 2500:
            self.img = 'login/images/m5.jpg'
        elif int(self.item.item_id) < 2600:
            self.img = 'login/images/m6.jpg'
        elif int(self.item.item_id) < 2700:
            self.img = 'login/images/m7.jpg'
        elif int(self.item.item_id) < 2800:
            self.img = 'login/images/m8.jpg'
        elif int(self.item.item_id) < 2900:
            self.img = 'login/images/m9.jpg'
        elif int(self.item.item_id) < 3000:
            self.img = 'login/images/m10.jpg'
        elif int(self.item.item_id) < 3100:
            self.img = 'login/images/m11.jpg'
        elif int(self.item.item_id) < 3200:
            self.img = 'login/images/m12.jpg'
        elif int(self.item.item_id) < 3300:
            self.img = 'login/images/m13.jpg'
        elif int(self.item.item_id) < 3400:
            self.img = 'login/images/m14.jpg'
        elif int(self.item.item_id) < 3500:
            self.img = 'login/images/m15.jpg'
        elif int(self.item.item_id) < 3600:
            self.img = 'login/images/m16.jpg'
        elif int(self.item.item_id) < 3700:
            self.img = 'login/images/m17.jpg'
        elif int(self.item.item_id) < 3800:
            self.img = 'login/images/m18.jpg'
        elif int(self.item.item_id) < 3900:
            self.img = 'login/images/m19.jpg'
        elif int(self.item.item_id) < 4000:
            self.img = 'login/images/m20.jpg'
        
        
