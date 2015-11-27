class SMS_store:
     def __init__(self):
         self.messages = []
         self.viewed = False
#     def viewed(self):
#     	 self.viewed = True
     def add_new_arrival(self, from_number, time_arrived, text_sms):
         message = (self.viewed, from_number, time_arrived, text_sms)
         self.messages.append(message)
     def message_count(self):
         return len(self.messages)
     def get_unread_indexes(self):
         result = []
         for i,v in enumerate(self.messages):
             if v[0] == self.viewed:
                result.append(i)
         return result
     def get_message(self, i):
     	 if i < len(self.messages):
     	    pList = list(self.messages[i])
     	    pList[0] = True
     	    self.messages[i] = tuple(pList)
     	    return tuple(pList)
     	 return None
     def delete(self, i):
    	 del self.messages[i]
     def clear(self):
     	 self.messages = []
     	 
     	 
     	 
#inbox = SMS_store()
#inbox.add_new_arrival(998909837130, "17:59:59", '''text messages, textmessage, textm message''')
#inbox.add_new_arrival(998951994383, "19:17:11", '''222222text messages, textmessage, textm message''')
