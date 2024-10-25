from graphics import*
from buttonclass import*
def binarySearch(my_list,item):
    size =len(my_list)#lenghth of the list
    middle = size//2
    if my_list ==[]:#base case
        return False
    else:
        if my_list[middle]==item:#if target found in the middle
            return True
        elif item> my_list[middle]:#t larger than middle
            #binary search for t in the upper halgf of my_list
            return binarySearch(my_list[middle+1:size],item)#don't need to start from mid since we checked for it lready in the lines above
        else:#if i reach this line ,it means t is lower than the middle value
            #binary serach for t in the lower half of my_list
            return binarySearch (my_list[0:middle],item)


def anagrams(s):
    if  s=="":#base case as an empty string
        return[s]
    else:
        ans =[]#list to accumulate the final results
        for word in anagrams(s[1:]):#iterates through ecah anagram of the tail of s
            for pos in range(len(word)+1):#goes through each position in the anagram
                                          #and creates anew string with the original first
                                          #character inserted into that position
                ans.append(word[:pos]+s[0]+word[pos:])
        return ans
def wordSolver(anagramInput):
    file = open("2of12.txt", "r")
    words =[]#creates an empty list
    for word in file.readlines():
        words.append(word.split('\n')[0])
    anagList = anagrams(anagramInput)
    solution = []#creates an empty list
    for element in anagList:
        if binarySearch(words,element):
            
            solution.append(element)
            
    return solution

if __name__ == "__main__":
    main()

    
