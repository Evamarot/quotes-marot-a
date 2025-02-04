from functions import *

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Add quote")
    print("2. Random quote")
    print("3. All quotes")
    print("4. Exit")

def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()

        choice = input("Choose your an action (1-4): ")

        if choice == "1":
            add_quote(quotes, "quotes.txt")
            
        elif choice == "2":
            count = int(input("Enter the number of quotes to display: "))
            display_quotes(quotes, count)
            
        elif choice == "3":
            view_quotes(quotes)
            
        elif choice == "4":
            print("Good bye...")
            break
            
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
