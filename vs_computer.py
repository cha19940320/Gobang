'''

@author: redtree

@contact: redtreec@gmail.com

@time: 17-12-28 下午4:09

@desc:  gobang AI base on decision tree method

'''

import tkinter as tk
from tkinter import messagebox
import random


class game_log:
    list_black = []  # Black chess pieces positions
    list_white = []  # White chess pieces positions
    turn = 1  # 1 : Turn to black side / 0 :   Turn to white side
    cursetX = 0  # The current mouse click coordinates
    cursetY = 0  #
    can_down =True


# Whether the rules of victory check
def check_win(check_list):
    # First cross calibration (horizontal) (vertical) (oblique side)
    for slb in check_list:
        horizontal_check = vertical_check = oblique_left = oblique_right = 0
        for x in range(1, 5):
            if ([slb[0] + x, slb[1]] in check_list) or ([slb[0] - x, slb[1]] in check_list):
                horizontal_check = horizontal_check + 1
            if ([slb[0], slb[1] + x] in check_list) or ([slb[0], slb[1] - x] in check_list):
                vertical_check = vertical_check + 1
            if ([slb[0] + x, slb[1] - x] in check_list) or ([slb[0] - x, slb[1] + x] in check_list):
                oblique_right = oblique_right + 1
            if ([slb[0] - x, slb[1] - x] in check_list) or ([slb[0] + x, slb[1] + x] in check_list):
                oblique_left = oblique_left + 1

        # When there are five in a row, you win
        if oblique_left >= 4 or oblique_right >= 4 or horizontal_check >= 4 or vertical_check >= 4:
            if game_log.turn == 1:
                messagebox._show('GameOver', 'Black_Win')
                break
            else:
                messagebox._show('GameOver', 'White_Win')
                break


# Battlefield build
def create_ground():
    # Initialize window and brush
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    # Draw 24 * 24 square checkerboard pen
    for x in range(20, 490, 20):
        canvas.create_line(20, x, 480, x)

    for y in range(20, 490, 20):
        canvas.create_line(y, 20, y, 480)

    def quit(event):
        root.quit()  # exit game

    # Click event callback method
    def callback(event):
         # Get click coordinates to find the approach point



         pointX = int(event.x)
         pointY = int(event.y)

         after_down(pointX, pointY)




         pechX =  pointX+(random.randint(-20,20))
         pechY =  pointY+(random.randint(-20,20))

         after_down(pechX, pechY)

         while game_log.can_down==False:
             pechX = pointX + (random.randint(-20, 20))
             pechY = pointY + (random.randint(-20, 20))

             after_down(pechX, pechY)




    def after_down(pointX,pointY):
        addX = delX = pointX
        addY = delY = pointY

        while (not (addX % 20) == 0) and (not (delX % 20) == 0):
            addX = addX + 1
            delX = delX - 1

        while (not (addY % 20) == 0) and (not (delY % 20) == 0):
            addY = addY + 1
            delY = delY - 1

        # After getting the approach point, input the game parameters
        if (addX % 20) == 0:
            game_log.cursetX = addX
        else:
            game_log.cursetX = delX

        if (addY % 20) == 0:
            game_log.cursetY = addY
        else:
            game_log.cursetY = delY

        '''
        tmp_point [110,110,130,130]  : 
        For the drop brush marker, respectively, 
        said the starting point of the circular coordinates and end coordinates

        Into the array should be converted to:
        tmp_point_2d [6,6] 
        That means the pawn is in the 6th row, 6th row
        '''
        # Through the brush drop and record the location, perform a victory rule check every time an action is performed
        if game_log.turn == 1:
            tmp_point = [game_log.cursetX - 10, game_log.cursetY - 10, game_log.cursetX + 10, game_log.cursetY + 10]
            tmp_point_2d = [(tmp_point[0] + tmp_point[2]) / 40, (tmp_point[1] + tmp_point[3]) / 40]

            if tmp_point_2d[0] < 1 or tmp_point_2d[0] > 24 or tmp_point_2d[1] < 1 or tmp_point_2d[1] > 24:
                print('Lots cross the border')
                game_log.can_down=False

            elif (not (tmp_point_2d in game_log.list_black)) and (not (tmp_point_2d in game_log.list_white)):
                game_log.list_black.append(tmp_point_2d)
                canvas.create_arc(game_log.cursetX - 10, game_log.cursetY - 10, game_log.cursetX + 10,
                                  game_log.cursetY + 10, extent=359, fill='black')
                check_win(game_log.list_black)  # Whether the victory check
                game_log.turn = 0  # Rotation
                game_log.can_down=True
                print('down success')
            else:
                print(' hasbean down')

                game_log.can_down=False



        else:
            tmp_point = [game_log.cursetX - 10, game_log.cursetY - 10, game_log.cursetX + 10, game_log.cursetY + 10]
            tmp_point_2d = [(tmp_point[0] + tmp_point[2]) / 40, (tmp_point[1] + tmp_point[3]) / 40]
            if tmp_point_2d[0] < 1 or tmp_point_2d[0] > 24 or tmp_point_2d[1] < 1 or tmp_point_2d[1] > 24:
                print('Lots cross the border')
                game_log.can_down=False


            elif (not (tmp_point_2d in game_log.list_white)) and (not (tmp_point_2d in game_log.list_black)):

                game_log.list_white.append(tmp_point_2d)
                canvas.create_arc(game_log.cursetX - 10, game_log.cursetY - 10, game_log.cursetX + 10,
                                  game_log.cursetY + 10, extent=359, fill='white')
                check_win(game_log.list_white)
                game_log.turn = 1
                game_log.can_down=True
                print('down success')
            else:
                print(' hasbean down')

                game_log.can_down = False

    # Bind the left mouse button and right
    root.bind("<Button-1>", callback)
    root.bind("<Button-3>", quit)

    # The main window into the performance cycle
    root.mainloop()


create_ground()

