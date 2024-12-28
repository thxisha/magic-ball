import random
print("ask a question...any question")
question = input()
result = random.randint(1,10)
if result <= 5:
    print("for sureee")
elif result > 5:
    print("no way.")
elif result == 10:
    print("possibly...")
    



