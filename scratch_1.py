Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... import time
... import random
... 
... def slow(text, delay= 0.09):
...     for ch in text:
...         print(ch, end="", flush = True)
...         time.sleep(delay)
...     print()
... 
... def intro():
...     slow("The Lost Signal")
...     slow("------------------------------")
...     slow("You are Alex Carter, a young engineer on a remote research station.")
...     slow("One night, you receive a strange signal from an unknown source...")
...     slow("Your mission: Decode it - or survive trying.")
...     slow("")
...     input("Press ENTER to begin your story...")
... 
... def decode_signal():
...     slow("\nThe signal is full of random pulses.")
...     slow("To decode it, you must guess the correct frequency (1-5).")
... 
...     correct = random.randint(1,5)
...     attempts = 3
... 
...     while attempts > 0:
...         guess = input("Choose a frequency (1,5)")
... 
...         if not guess.isdigit():
...             slow("That doesn't look like a number. Try again.")
...             continue
... 
...         guess =int(guess)
... 
...         if guess == correct:
...             slow("\nTHe signal unlocks! A hidden message appears:")
            slow("WE ARE NOT ALONE.")
            return True
        else:
            attempts -= 1
            slow(f"Incorrect frequency. attempts left: {attempts}")

    slow("\nThe signal overloads the system... sparks fly everywhere!")
    slow("You fall back as the station plunges into darkness.")
    return False
def ending(success):
    if success:
        slow("\n GOOD ENDİNG")
        slow("The signal destroys your station.")
        slow("Your final log  becomes a warning for future explorers")

def main():
    intro()
    result = decode_signal()
    ending(result)

if __name__ == "__main__":
    main()




