class EmailNotification():
    def __init__(self, msg:str):
        self.msg = msg 

    def send(self) -> str:
        print(f"Email Notification sobre el coreo electrico...\n{self.msg}")



class SMSNotification():
    def __init__(self, msg:str):
        self.msg = msg

    def send(self) -> None:
        print(f"SMS Notification sibre el telephono...\n{self.msg}") 
