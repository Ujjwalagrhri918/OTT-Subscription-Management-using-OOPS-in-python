from tkinter import *
import netflix_management
import amazon_ott
import netflix_using_oops
import amazon_ott_with_oodp

#window creation
root = Tk()
root.title("Welcome")
root.geometry("720x520")
root.config(bg='linen')

#choose your platform wala thing
#choose your platform wala thing
titleFrame=Frame(root)
titleFrame.grid(row=0,column=0)
logoImage=PhotoImage(file="logo_wala_image (1).png")
titleLabel=Label(titleFrame,text=' Choose your Platform',image=logoImage,compound=LEFT,font=('Ubuntu',28,'bold'),
                 bg='linen',fg='black')
titleLabel.grid(row=0,column=0)
# button haru ko section
# button haru ko section
button_frame = Frame(root,bg='linen')

netflix_image=PhotoImage(file='netflix_final.png',height=250,width=250)
amazon_image=PhotoImage(file='amazon_final.png',height=250,width=250)



def running_netflix():
    netflix_using_oops.browser = netflix_using_oops.webdriver.Chrome("D:\old pc\Softwares\chromedriver_win32\chromedriver")
    netflix_using_oops.dicty = {"prakash.sapkota17@gmail.com":["Name: Prakash Sapkota","Service Platform: Netflix","Subscription Package: Premium UltraHD: One-Month","Subscription Price: USD:9.99","Last Purchased Date: 17 April 2023"]}
    netflix_using_oops.app = netflix_using_oops.NetflixChecker(netflix_using_oops.browser,netflix_using_oops.dicty)
    netflix_using_oops.app.run()

def running_amazon():
    amazon_ott_with_oodp.dicty = {"9035225406":["Name: Madan Raj Upadhyay","Service Platform: Amazon Prime Video","Subscription Package: One-Month","Subscription Price: Rs.299","Last Purchased Date: 27 April 2023"]}
    amazon_ott_with_oodp.browser = amazon_ott_with_oodp.webdriver.Chrome("D:\old pc\Softwares\chromedriver_win32\chromedriver")
    amazon_ott_with_oodp.browser.implicitly_wait(1)
    amazon_ott_with_oodp.browser.get("https://www.primevideo.com/region/in/offers/nonprimehomepage/ref=atv_auth_pre")
    amazon_ott_with_oodp.sleep(1)
    amazon_ott_with_oodp.amazon_billing_date_checker = amazon_ott_with_oodp.AmazonBillingDateChecker(amazon_ott_with_oodp.browser,amazon_ott_with_oodp.dicty)
    amazon_ott_with_oodp.amazon_billing_date_checker.run()
    amazon_ott_with_oodp.browser.quit()

#insert -> command=running_netflix
#insert -> command=running_amazon

netflix_button = Button(button_frame,image=netflix_image, text="Netflix",bd=0,bg='linen',activebackground="old lace",height=250,width=250,command=running_netflix)
amazon_button = Button(button_frame,image=amazon_image, text="Amazon Prime",bd=0,bg='linen',activebackground="old lace",height=250,width=250,command=running_amazon)

# placement of buttons
button_frame.grid(row=1,column=0,pady=80)
netflix_button.grid(row=4,column=3,padx=60)
amazon_button.grid(row=4,column=6,padx=20)


root.mainloop()