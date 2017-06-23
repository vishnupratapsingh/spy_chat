from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Vishnu Pratap Singh', 'Mr.', 21, 5.0)

friend_one = Spy('Thakur Sahab', 'Mr.', 4.9, 27)
friend_two = Spy('Thakurani Sahiba', 'Mrs.', 4.39, 21)
friend_three = Spy('Ram Lal', 'Dr.', 4.95, 37)


friends = [friend_one, friend_two, friend_three]