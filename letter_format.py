letter = '''Dear <|NAME|>
    Greeting from ABC coding hourse
You are Selected
Date. <|DATE|>'''

name=input("Enter your name :")
date=input("Enter today Date:")
letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)

print(letter)