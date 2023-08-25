from plyer import notification  
from tkinter import *
from win10toast_click import ToastNotifier



notification_title = 'GREETINGS FROM FAADINEPALI!'  
notification_message = 'Muji, your Netflix subscription ends on' +  " this this this agjsjk hakj akshfkjashg kdasjkhdkajs ja"

def show_the_payment_options():
    root = Tk()
    root.title("Notification Center")
    root.geometry("720x480")
    check_button = Button(root, text="Pay the bills!", command=None)
    # check_button.grid(row=3,column=0)
    check_button.pack(pady=25)
    root.mainloop()
    
toaster = ToastNotifier()
toaster.show_toast(
    notification_title,
    notification_message,
    duration=5,
    threaded=True,
    callback_on_click=show_the_payment_options
) 

# notification.notify(  
#     title = notification_title,  
#     message = notification_message,  
#     app_icon = None,  
#     timeout = 1,  
#     toast = True,
#     callback=on_notification_click
#     )  