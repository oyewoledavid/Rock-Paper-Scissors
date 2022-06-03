def input_validation(user_choice):
    if user_choice:

        if len(user_choice) == 1:

            try:
                str(user_choice)
                return True
            except ValueError:
                print("Input a valid option")
                return False

        else:
            print("Input can not be more than one character")
            return False
    else:
        print("Option can not be empty")
        return False


def show_choice(user_choice, cpu_choice):
    if user_choice.upper() == "R" and cpu_choice == "P":
        print("Player(Rock):CPU(Paper)")

    elif user_choice.upper() == "R" and cpu_choice == "S":
        print("Player(Rock):CPU(Scissors)")

    elif user_choice.upper() == "P" and cpu_choice == "R":
        print("Player(Paper):CPU(Rock)")

    elif user_choice.upper() == "S" and cpu_choice == "R":
        print("Player(Scissor):CPU(Rock)")

    elif user_choice.upper() == "S" and cpu_choice == "P":
        print("Player(Scissor):CPU(Paper)")

    elif user_choice.upper() == "P" and cpu_choice == "S":
        print("Player(Paper):CPU(Scissor)")

    elif user_choice.upper() == "S" and cpu_choice == "S":
        print("Player(Scissors):CPU(Scissor)")

    elif user_choice.upper() == "P" and cpu_choice == "P":
        print("Player(Paper):CPU(Paper)")

    elif user_choice.upper() == "R" and cpu_choice == "R":
        print("Player(Rock):CPU(Rock)")

    return show_choice