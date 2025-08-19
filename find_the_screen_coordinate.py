import pyautogui
import time


def get_screen_coordinate():

    print("Move your mouse to the TOP-LEFT corner of the game window and stay up to 7 seconds...")
    time.sleep(7)
    top_left = pyautogui.position()
    print(f"Top-left corner: {top_left}")

    print("Move your mouse to the BOTTOM-RIGHT corner of the game window and stay up to 7 seconds...")
    time.sleep(7)
    bottom_right = pyautogui.position()
    print(f"Bottom-right corner: {bottom_right}")

    game_x = top_left.x
    game_y = top_left.y
    game_width = bottom_right.x - top_left.x
    game_height = bottom_right.y - top_left.y

    print(f"Coordinates for your code:\n"
        f"game_x = {game_x}\n"
        f"game_y = {game_y}\n"
        f"game_width = {game_width}\n"
        f"game_height = {game_height}")
    
    return game_x , game_y , game_width , game_height
