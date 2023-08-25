from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
from win10toast_click import ToastNotifier
from time import sleep
import ott

class NetflixChecker(ott.OTT):
    
    def __init__(self,browser,dict):
        self.browser = browser
        self.dict = dict
        self.root = Tk()
        self.root.geometry("720x480")
        self.root.config(bg='linen')
        self.root.title("Netflix Billing Date Checker")

        self.titleFrame=Frame(self.root)
        # self.titleFrame.grid(row=0,column=0)
        self.titleFrame.pack(side="left", pady=0,padx=0) #(row=0,column=0)
        self.logoImage=PhotoImage(file="netflix_final.png")
        self.titleLabel=Label(self.titleFrame,bg='linen',fg='black') #image=self.logoImage,          
        self.titleLabel.pack(side="left",pady=0,padx=0) #grid(row=0,column=0)
        # self.titleLabel.grid(row=0,column=0)

        self.create_widgets()
        
    def create_widgets(self):
        # Create a label and entry for the email input
        email_label = Label(self.root, text="Email:",font=("Ubuntu",14))
        email_label.pack()
        self.email_entry = Entry(self.root,font=("Ubuntu",15), bg="white")
        self.email_entry.pack()

        # Create a label and entry for the password input
        password_label = Label(self.root, text="Password:",font=("Ubuntu",14))
        password_label.pack()
        self.password_entry = Entry(self.root, show="*",font=("Ubuntu",15),bg="white")
        self.password_entry.pack()

        # Create a button to check the billing date
        check_button = Button(self.root, text="Check Billing Date",bg="linen" ,font=("Ubuntu",13),height=2,width=20, command=self.check_billing_date)
        check_button.pack()
        

        # Create a label to display the billing date
        self.billing_date_label = Label(self.root)
        self.billing_date_label.pack()

    def show_the_payment_options(self):
        self.browser.get("https://www.netflix.com/YourAccount")

    def display_notifications(self):
        notification_title ="NETFLIX ALERT- FaadiNepali"
        notification_message = self.billing_date_label.cget("text")

        toaster = ToastNotifier()
        toaster.show_toast(
            notification_title,
            notification_message,
            duration=5,
            threaded=True,
            callback_on_click=self.show_the_payment_options
        )

    def login(self, email, password):
        try:
            if email == "prakash.sapkota17@gmail.com":
                for key, values in dicty.items():
                        # create a label for the key
                        key_label = Label(self.root, text=f"User Details for {key}:",font=("Ubuntu",13),bg="Old Lace")
                        key_label.pack(anchor="w")
            # loop through the values and create a label for each one
                for i, value in enumerate(values):
                    value_label = Label(self.root, text=f"{value}", pady=10,font=("Ubuntu",13),bg="Old Lace")
                    value_label.pack(anchor="w")
            username_input = self.browser.find_element(By.NAME,"userLoginId")
            password_input = self.browser.find_element(By.NAME,"password")
            submit=self.browser.find_element(By.CLASS_NAME,"login-button")
            username_input.send_keys(email)
            password_input.send_keys(password)
            submit.click()
            acc=self.browser.find_element(By.CLASS_NAME,"profile-link")
            acc.click()
            return True
        except:
            return False

    def check_billing_date(self):
        # Get the email and password from the input fields
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Use Selenium to log in to Netflix and get the billing date
        self.browser.implicitly_wait(1)
        self.browser.get("https://www.netflix.com/in/login")
        sleep(1)
        if self.login(email, password):
            try:
                self.browser.get('https://www.netflix.com/YourAccount')
                billingDate=self.browser.find_elements(By.CLASS_NAME,"account-section-item")[8]
                billingDateHTML = billingDate.get_attribute("innerHTML")
                self.billing_date_label.config(text=billingDateHTML,bg="linen" ,font=("Ubuntu",13))
                self.display_notifications()
            except Exception:
                self.billing_date_label.config(text="An error occurred while getting your billing date.",bg="linen" ,font=("Ubuntu",13))

    def run(self):
        self.root.mainloop()
        self.browser.quit()

if __name__ == "__main__":
    browser = webdriver.Chrome("D:\old pc\Softwares\chromedriver_win32\chromedriver")
    dicty = {"prakash.sapkota17@gmail.com":["Name: Prakash Sapkota","Service Platform: Netflix","Subscription Package: Premium UltraHD: One-Month","Subscription Price: USD:9.99","Last Purchased Date: 17 April 2023"]}
    app = NetflixChecker(browser,dicty)
    app.run()