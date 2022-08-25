# Lifo : last input first output


# imagine dropping or placing books on top of a table on each other, thats a stack/Queue
# the last book placed is the first book on top
#  we use stack/Queue in python in list,array

table = []
table.append("Book1")
table.append("Book2")
table.append("Book3")
table.append("Book4")
print(f"these are the books on the table \n {table}")
# to get the last book we use the pop() method because we want to take it out and return it also
taken = table.pop()

print(f"i took the last book {taken} from the table \n now we are left with {table}")