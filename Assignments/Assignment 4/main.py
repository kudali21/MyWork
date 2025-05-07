import modules as m

def display_menu():
    print("\nSelect an option:")
    print("1. Rock Paper Scissors")
    print("2. Area of Cylinder")
    print("3. Average of Array")
    print("4. Simple Calculator")
    print("5. Find Median of Given Array")
    print("6. Move All 0s to Right in an Array")
    print("7. Sum of AP Series")
    print("8. Sum of All Prime Numbers in Given Range")
    print("9. Right to Vote & Greeting")
    print("10. Pounds to Kgs")
    print("11. Simple Interest")
    print("12. Cubes")
    print("13. Display Calendar")
    print("14. Split and Join String")
    print("15. Generate Random Number")
    print("16. Find ASCII Value of Character")
    print("17. Find First Non-Repeating Character")
    print("18. Days Between Two Dates")
    print("19. Print Hello Python")
    print("0. Exit")

while True:
    display_menu()
    option = int(input("\nEnter your choice: "))

    if option == 1:
        print(m.rock_paper_scissors())
    elif option == 2:
        print(m.area_of_cylinder())
    elif option == 3:
        print(m.average_of_array())
    elif option == 4:
        print(m.simple_calculator())
    elif option == 5:
        print(m.find_median_of_array())
    elif option == 6:
        print(m.move_zeros_right())
    elif option == 7:
        print(m.sum_of_ap_series())
    elif option == 8:
        print(m.sum_of_prime_numbers())
    elif option == 9:
        print(m.right_to_vote_greeting())
    elif option == 10:
        print(m.pounds_to_kgs())
    elif option == 11:
        print(m.simple_interest())
    elif option == 12:
        print(m.cubes())
    elif option == 13:
        print(m.display_calendar())
    elif option == 14:
        print(m.split_and_join())
    elif option == 15:
        print(m.generate_random_number())
    elif option == 16:
        print(m.ascii_value())
    elif option == 17:
        print(m.non_repeating_char())
    elif option == 18:
        print(m.days_between_dates())
    elif option == 19:
        print(m.hello_python())
    elif option == 0:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
