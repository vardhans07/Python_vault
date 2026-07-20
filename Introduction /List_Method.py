players = ["Alice", "Bob", "Charlie"]
print(type(players))


#1. append the kay
players.append("kay")
print(f"append method : {players}")

>> append method : ['Alice', 'Bob', 'Charlie', 'kay']

#2. insert at 2nd posituon post
players.insert (2 , "post")
print(f"insert method : {players}")

>>insert method : ['Alice', 'Bob', 'post', 'Charlie', 'kay']

#3.extend method used 
players.extend(["tim","jerry"])
print(f"extend methd: {players}")
>>extend methd: ['Alice', 'Bob', 'post', 'Charlie', 'kay', 'tim', 'jerry']

#4.append method 
players.append ("ops")
print(f"append method:{players}")

>> append method:['Alice', 'Bob', 'post', 'Charlie', 'kay', 'tim', 'jerry', 'ops']

#5. Remove Method
players.remove("tim")
print(f"remove method: {players}")

>> remove method: ['Alice', 'Bob', 'post', 'Charlie', 'kay', 'jerry', 'ops']

#6. Pop Method 
players.pop(2)
print(f"pop Method: {players}")
>>pop Method: ['Alice', 'Bob', 'Charlie', 'kay', 'jerry', 'ops']

#7.Reverse Method 
players.reverse()
print(f"Reverse Method : {players}")
>>Reverse Method : ['ops', 'jerry', 'kay', 'Charlie', 'Bob', 'Alice']

#8. sort method 
players.sort()
print(f"sort method: {players}")
>>sort method: ['Alice', 'Bob', 'Charlie', 'jerry', 'kay', 'ops']

#9.copy List method
cp_players=players.copy()
print(f"Copy list Method : {cp_players}")
>>Copy list Method : ['Alice', 'Bob', 'Charlie', 'jerry', 'kay', 'ops']

# 10. clear list 
players.clear()
print(f"clear method: {players}")
>>clear method: []

#11. Index Method 
players = ["Alice", "Bob", "Charlie"]
def ind_method(players):
    for i in players :
        for j in i:
         id_g=players.index(i)
        print(id_g, end=" ")

ind_method(players)

>>0 1 2 
    


