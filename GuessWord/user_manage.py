import os

def update_user_lose(userName):
    user_file = open("users/" + userName + ".txt", 'r')
    new_file_content = ""
    for row in user_file:
        user_line = row.split(":")
        user_number = int(user_line[1])
        if user_line[0] != "Wins":
            user_number += 1
        user_line[1] = str(user_number) + "\n"
        new_row =  ":".join(user_line)
        new_file_content += new_row
    user_file.close()
    user_file = open("users/" + userName + ".txt", 'w')
    user_file.write(new_file_content)
    user_file.close()

def update_user_win(userName):
    user_file = open("users/" + userName + ".txt", 'r')
    new_file_content = ""
    for row in user_file:
        user_line = row.split(":")
        user_number = int(user_line[1])
        if user_line[0] != "Loses":
            user_number += 1
        user_line[1] = str(user_number) + "\n"
        new_row =  ":".join(user_line)
        new_file_content += new_row
    user_file.close()
    user_file = open("users/" + userName + ".txt", 'w')
    user_file.write(new_file_content)
    user_file.close()

def read_user_data(userName):
    user_int = []
    if os.path.exists( "users/"+ userName + ".txt"):
        file_read = open("users/" + userName + ".txt")
        for row in file_read:
            user_int.append(row.split(":")[1].split("\n")[0])
    else:
        file_read = open("users/" + userName + ".txt", "w")
        file_read.write("Total:0\nWins:0\nLoses:0")
        file_read.close()
        file_read = open("users/" + userName + ".txt")
        for row in file_read:
            user_int.append(row.split(":")[1].split("\n")[0])
    file_read.close()
    return user_int

def delete_user(userName):
    if os.path.exists("users/"+ userName + ".txt"):
        os.remove("users/"+ userName + ".txt")
        return True
    else:
        return False
