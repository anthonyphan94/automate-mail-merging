# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("./Input/Names/invited_names.txt", "r") as names_file:
    name_files_content = names_file.readlines()


# create a name list from the text file
new_name_list = []
for word in range(len(name_files_content)):
    name_files_content[word] = name_files_content[word].strip("\n")
    new_name_list.append(name_files_content[word])



for name in range(len(new_name_list)):
    # copy starting letter to a new temporary one
    temporary_starting_letter = starting_letter
    temporary_starting_letter = temporary_starting_letter.replace("[name]", new_name_list[name])

    # create a new letter with corresponding name and new name
    with open("./Output/ReadyToSend/"+new_name_list[name]+".txt","w") as file:
        file.write(temporary_starting_letter)


