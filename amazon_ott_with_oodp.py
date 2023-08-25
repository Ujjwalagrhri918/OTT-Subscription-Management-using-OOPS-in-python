from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from win10toast_click import ToastNotifier
from plyer import notification
import ott

class AmazonBillingDateChecker(ott.OTT):
    def __init__(self, browser,dict):
        self.dict = dict
        self.browser = browser
        self.root = Tk()
        self.root.geometry("720x480")
        self.root.config(bg='linen')
        self.root.title("Amazon Billing Date Checker")
        
        self.titleFrame=Frame(self.root)
        # self.titleFrame.grid(row=0,column=0)
        self.titleFrame.pack(side="left", pady=0,padx=0) #(row=0,column=0)
        self.logoImage=PhotoImage(file="amazon_final.png")
        self.titleLabel=Label(self.titleFrame,bg='linen',fg='black',compound="left")  #image=self.logoImage,        
        self.titleLabel.pack(side="left",pady=0,padx=0) #grid(row=0,column=0)
        # self.titleLabel.grid(row=0,column=0)

        # Create a label and entry for the email input
        email_label = Label(self.root, text="Email:",font=("Ubuntu",14))
        email_label.pack()
        self.email_entry = Entry(self.root,font=("Ubuntu",15), bg="white")
        self.email_entry.pack()
        
        # Create a label and entry for the password input
        password_label = Label(self.root, text="Password:",font=("Ubuntu",14))
        password_label.pack()
        self.password_entry = Entry(self.root, show="*",font=("Ubuntu",15), bg="white")
        self.password_entry.pack()
        
        # Create a button to check the billing date
        check_button = Button(self.root, text="Check Billing Date",bg="linen" ,font=("Ubuntu",13), command=self.check_billing_date)
        check_button.pack()

        
        self.billing_date_label = Label(self.root)
        self.billing_date_label.pack()
        
    def check_billing_date(self):
        # Get the email and password from the input fields
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        # Use Selenium to log in to Amazon Prime and get the billing date
        if self.login(email, password):
            try:
                if email == '9035225406':
                    for key, values in dicty.items():
                        # create a label for the key
                        key_label = Label(self.root, text=f"User Details for {key}:",font=("Ubuntu",13),bg="Old Lace")
                        key_label.pack(anchor="w")
            # loop through the values and create a label for each one
                    for i, value in enumerate(values):
                        value_label = Label(self.root, text=f"{value}", pady=10,font=("Ubuntu",13),bg="Old Lace")
                        value_label.pack(anchor="w")
        # Create a label to display the billing date
                self.browser.get("https://www.amazon.in/")
                profile_button = self.browser.find_elements(By.CLASS_NAME,"nav-line-2")[2]
                profile_button.click()
                
                profile_button = self.browser.find_elements(By.CLASS_NAME,"a-box-inner")[2].click()
                
                billingDate = self.browser.find_elements(By.CLASS_NAME,"mcx-menu-item__heading")[1]
                billingDateHTML = billingDate.get_attribute("innerHTML")
                
                self.billing_date_label.config(text= "Your AmazonPrime will expire on " + billingDateHTML,bg="linen" ,font=("Ubuntu",13)) #last edited this
                self.display_notifications()
                
            except Exception as e:
                print(e)
                self.billing_date_label.config(text="An error occurred while getting your billing date.\n Try checking your credentials",bg="linen" ,font=("Ubuntu",13))
                
    def login(self, email, password):
        try:
            first_click = self.browser.find_element(By.CLASS_NAME,"DVPAWebWidgetsUI_Button__prime")
            first_click.click()
            
            username_input = self.browser.find_element(By.NAME,"email")
            password_input = self.browser.find_element(By.NAME,"password")
            submit=browser.find_element(By.CLASS_NAME,"a-button-input")
            username_input.send_keys(email)
            password_input.send_keys(password)
            submit.click()
            sleep(5)
            
            return True
        except:
            return False
    def show_the_payment_options():
        root = Tk()
        root.title("Notification Center")
        root.geometry("720x480")
        check_button = Button(root, text="Pay the bills!", command=None,height=400,width=400)
        check_button.grid(row=0,column=0)
        check_button.pack(pady=25)
        root.mainloop()

    def display_notifications(self):
        # Implement notification feature
        notification_title ="AMAZON ALERT- FAADINEPALI"
        notification_message = self.billing_date_label.cget("text")
        toaster = ToastNotifier()
        toaster.show_toast(
            notification_title,
            notification_message,
            duration=5,
            threaded=True,
            callback_on_click = self.show_the_payment_options
        )
        
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    dicty = {"9035225406":["Name: Madan Raj Upadhyay","Service Platform: Amazon Prime Video","Subscription Package: One-Month","Subscription Price: Rs.299","Last Purchased Date: 27 April 2023"]}
    browser = webdriver.Chrome("D:\old pc\Softwares\chromedriver_win32\chromedriver")
    browser.implicitly_wait(1)
    browser.get("https://www.primevideo.com/region/in/offers/nonprimehomepage/ref=atv_auth_pre")
    sleep(1)
    amazon_billing_date_checker = AmazonBillingDateChecker(browser,dicty)
    amazon_billing_date_checker.run()
    browser.quit()