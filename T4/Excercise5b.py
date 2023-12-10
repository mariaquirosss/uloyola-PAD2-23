class Terminal:
    def __init__(self, phone_number:str):

        if not self._validate_phone_number(phone_number):
            raise ValueError("Invalid phone number. Please enter a valid 9-digit number starting with 9, 6, or 7.")
        
        self._phone_number = phone_number
        self._conversation_time = 0

    # Method validate PhoneNumber
    def _validate_phone_number(self, phone_number:str)->bool:
        result = False
        # Review the conditions - (only digits, starting with 9, 6, or 7, and their lengthis nine digit
        if(phone_number.isdigit() and phone_number[0] in ('9', '6', '7') and len(phone_number) == 9):
            result = True
        return result

    # Method Call with other_terminal
    def call(self, other_terminal, duration:int):

        #Validate that other Terminal is an Terminal object.
        if not isinstance(other_terminal, Terminal):
            raise ValueError("Invalid argument. Please provide a valid Terminal object.")
        
        self._conversation_time += duration
        other_terminal._conversation_time += duration

    # Method String
    def __str__(self):
        phoneNumberSpliter = ' '.join([str(self._phone_number)[:3], str(self._phone_number)[3:5], str(self._phone_number)[5:7], str(self._phone_number)[7:]])
        return f"{phoneNumberSpliter} - Conversation time: {self._conversation_time}s"

'''' Resolution for the Second Step'''


class Mobile(Terminal):

    # The cost per minute is 5, 15, and 30 cents,
    TariffRates = {"rat": 0.05, "monkey": 0.15, "elephant": 0.30}

    #Constructor
    def __init__(self, phone_number:Terminal, rate:str):
        super().__init__(phone_number)
        self._rate = rate
        self._cost = 0

    #Call Metohd for Mobile phones
    def call(self, other_terminal:Terminal, duration:float):

        # Verify if the input is a Terminal
        if not isinstance(other_terminal, Mobile):
            raise ValueError("Invalid argument. Please provide a valid Mobile object.")
        
        # Get the Tafif crom TariffRates
        cost_per_minute = self.TariffRates[self._rate]

        cost = (duration / 60) * cost_per_minute
        self._conversation_time += duration
        self._cost += cost

    # Change Rate Metof
    def change_rate(self, new_rate:str):
        if new_rate not in self.TariffRates:
            raise ValueError("Invalid rate. Please choose 'rat', 'monkey', or 'elephant'.")
        
        self._rate = new_rate

    # Redefition of String, adding the charged cost with 2 digits
    def __str__(self):
        return f"{super().__str__()} - charged {self._cost:.2f}€"

# Test program
if __name__ == "__main__":

    m1 = Mobile("666112233", "rat")
    m2 = Mobile("666744459", "monkey")
    m3 = Mobile("632128919", "elephant")
    print(m1)
    print(m2)
    m1.call(m2, 210)
    m1.call(m3, 320)
    m2.call(m3, 450)
    print(m1)
    print(m2)
    print(m3)
