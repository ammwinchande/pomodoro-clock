import time
import webbrowser


def start_pomodoro(url, pomodoro_number):
    """
    Play the music, and wait for 5 mins
    :param url:
    :param pomodoro_number:
    :return:
    """
    pomodoro_count = 0
    while pomodoro_count < pomodoro_number:
        time.sleep(25*60)
        webbrowser.open(url, new=1, autoraise=1)
        pomodoro_count += 1


def handle_program(execution, url, pomodoro_number):
    """
    Main program execution
    :param execution:
    :param url:
    :param pomodoro_number
    :return:
    """
    if execution == 'q' or execution == 'Q':
        exit()
    elif execution == 'y' or execution == 'Y':
        print("Program will quit after finishing the number of pomodoros\n"
              "or you cancel the program by pressing ctrl+c")
        print("Pomodoro Clock was started at: " + time.ctime())
        start_pomodoro(url, pomodoro_number)
    else:
        print("Sorry, I couldn't understand one of your options"
              "Run the program again")
        exit()


def get_inputs():
    """
    Get user inputs
    :return:
    """
    fav_music_url = input("Enter your favourite music URL: ")
    pomodoro_number = int(input("Enter number of pomodoro cycles: "))
    start_clock = input("Enter 'Y' or 'y' to start the clock \n"
                        "OR Enter 'Q' or 'q' to quit the program: ")
    if fav_music_url == "":
        fav_music_url = "https://www.youtube.com/watch?v=XTNl5WxklgE"

    handle_program(start_clock, fav_music_url, pomodoro_number)


def display():
    """
    Display style for the program
    :return:
    """
    print("\n*****************************************")
    print("*\t\t\t Pomodoro Clock \t\t\t*")
    print("*\t\t author: m.a. mwinchande \t\t*")
    print("*****************************************")
    print("\n")


# execute the program
display()
get_inputs()
