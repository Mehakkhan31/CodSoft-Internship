# creating a rock paper scissors game using python
from tkinter import *
from PIL import Image,ImageTk
from random import choice

root = Tk()
root.title("Rock_paper_scissors_BY mehak Khan")
root.geometry("1000x420")
root.configure(background="#9b59b6")


# Function to resize image
def resize_image(image_path, size):
    image = Image.open(image_path)
    resized_image = image.resize(size)
    return ImageTk.PhotoImage(resized_image)

# Desired size for images
image_size = (210,220)

# Resized pictures
Rock_img_user = resize_image("rock.png", image_size)
paper_img_user = resize_image("paper.png", image_size)
scissors_img_user = resize_image("scissors.png", image_size)
Rock_img_computer = resize_image("rock.png", image_size)
paper_img_computer = resize_image("paper.png", image_size)
scissors_img_computer = resize_image("scissors.png", image_size)

# insert pictures
user_image_label = Label(root,image=Rock_img_user,background="#9b59b6")
user_image_label.grid(row=1,column=0)
computer_image_label = Label(root, image=Rock_img_computer,background="#9b59b6")
computer_image_label.grid(row=1,column=4)

#scores
player_score = Label(root, text=0, font=100,background="#9b59b6",fg="white")
player_score.grid(row=1,column=1)
computer_score = Label(root, text=0, font=100,background="#9b59b6",fg="white")
computer_score.grid(row=1,column=3)

# indicators 
user_indicator = Label(root, text="USER", font=50,background="#9b59b6",fg="white")
user_indicator.grid(row=0,column=1)
computer_indicator = Label(root, text="COMPUTER", font=50,background="#9b59b6",fg="white")
computer_indicator.grid(row=0,column=3)

# message
messagge = Label(root,font=50,background="#9b59b6",fg="white")
messagge.grid(row=3,column=2)

#update message
def updateMessage(x):
    messagge['text'] = x

# update user score
def updateUserscore():
    score = int(player_score["text"])
    score  = score + 1
    player_score["text"] = str(score)

#update computer score
def updateComputerscore():
    score = int(computer_score["text"])
    score  = score + 1
    computer_score['text'] = str(score)

# checking winner
def checking(player,computer):
    if(player == computer):
        updateMessage("It's a Tie!!")
    elif(player == "rock_button"):
        if(computer == "paper+button"):
            updateMessage("you loose!!")
            updateComputerscore()
        else:
            updateMessage("you win!!")
            updateUserscore()
    elif(player == "paper_button"):
        if(computer == "rock_button"):
            updateMessage("you  win!!")
            updateUserscore()
        else:
            updateMessage("you loose!")
            updateComputerscore()
    elif(player == "scissors_button"):
        if(computer == "rock_button"):
            updateMessage("you loose!!")
            updateComputerscore()
        else:
            updateMessage("You win !!")
            updateUserscore()
    else:
        pass

#choices
choices = ["rock_button","paper_button","scissors_button"]
def updateChoice(x):
    #computer choices
    computer_choice = choice(choices)
    if(computer_choice =="rock_button"):
        computer_image_label.config(image=Rock_img_computer)
    elif(computer_choice =="paper_button"):
        computer_image_label.config(image=paper_img_computer)
    else:
        computer_image_label.config(image=scissors_img_computer)

    #user choice
    if(x == "rock_button"):
        user_image_label.config(image=Rock_img_user)
    elif(x =="paper_button"):
        user_image_label.configure(image=paper_img_user)
    else:
        user_image_label.configure(image=scissors_img_user)
    checking(x,computer_choice)

# button
rock_button = Button(root,command=lambda:updateChoice("rock_button"),font="comicsensms 10 bold", width=20,height=2,text="ROCK",background="#FF3E4D", fg="white")
rock_button.grid(row=2,column=1,padx=3)
paper_button = Button(root,command=lambda:updateChoice("paper_button"),font="comicsensms 10 bold",width=20,height=2,text="PAPER",background="#FAD02E", fg="white")
paper_button.grid(row=2,column=2,padx=3)
scissors_button = Button(root, command=lambda:updateChoice("scissors_button"),width=20,height=2,font="comicsensms 10 bold",text="SCISSORS",background="#0ABDE3", fg="white")
scissors_button.grid(row=2,column=3,padx=3)


root.mainloop()