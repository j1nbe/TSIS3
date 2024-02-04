#1
def toOunces(grams):
    return grams * 28.3495231

weight = 100
print(toOunces(weight))


#2
def toC(F):
    return (5 / 9) * (F - 32)

Far = 451
print(toC(Far))


#3
def solve(numheads, numlegs):
    for ch in range(numheads + 1):
        r = numheads - ch
        if 2 * ch + 4 * r == numlegs:
            return ch, r
    else:
        return "There is no solution"

legs = 94
heads = 35
print(solve(heads, legs))


#4
import math

def isPrime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return 0
        else:
            return 1
    else:
        return 0

def onlyPrimes(list):
    for i in list:
        if not isPrime(i):
            list.remove(i)
            onlyPrimes(list)

list1 = list(map(int, input().split()))

onlyPrimes(list1)
print(list1)


#5
def perms(strg, find, lind):
    if find == lind:
        print(str(strg))
    else:
        for i in range(find, lind):
            strg[find], strg[i] = strg[i], strg[find]
            perms(strg, find + 1, lind)
            strg[find], strg[i] = strg[i], strg[find]

def str(list):
    return ''.join(list)

string1 = "Ilu"
list1 = list(string1)
perms(list1, 0, len(string1))


#6
def rev(str1):
    words = []
    word = ""
    for i in str1:
        if i != " " and i != "\n":
            word += i
        else:
            words.append(word)
            word = ""
    else:
        words.append(word)
        word = ""
    newstr = ""
    u = len(words) - 1
    while u >= 0:
        newstr += words[u]
        u -= 1
        newstr += " "
    return newstr

strg = "I love sleeping very much"
print(rev(strg))


#7
def has_33(nums):
    before = -999
    for i in nums:
        if before == i:
            return True
        else:
            before = i
    else:
        return False

lst = [1, 4, 3, 3, 3, 5]
print(has_33(lst))
lst2 = [1, 3, 4, 3]
print(has_33(lst2))


#8
def spy_game(nums):
    one = 1
    two = 1
    for i in nums:
        if one == 1 and i == 0:
            one = 0
        elif one == 0 and two == 1 and i == 0:
            two = 0
        elif one == 0 and two == 0 and i == 7:
            return True
    else:
        return False

list1 = [1,2,4,0,0,7,5]
print(spy_game(list1))
list2 = [1,0,2,4,0,5,7]
print(spy_game(list2))
list3 = [1,7,2,0,4,5,0]
print(spy_game(list3))


#9
def volume(r):
    return 3.14 * (4 / 3) * pow(r, 3)

r = 3
print(volume(r))


#10
def uniq(list):
    newlist = []
    for i in list:
        if not (i in newlist):
            newlist.append(i)
    return newlist

list1 = [1, 1, 2, 3, 4, 2, 5, 6, 7, 7, 7, 8, 9, 0, 1]
print(uniq(list1))


#11
def pal(word):
    backs = ""
    i = len(word) - 1
    while i >= 0:
        backs += word[i]
        i -= 1
    if backs == word:
        return True
    else:
        return False

word1 = "madam"
print(pal(word1))
w2 = "madame"
print(pal(w2))


#12
def hist(list):
    for i in list:
        while i > 0:
            print("*", end="")
            i -= 1
        print()

list = [4, 9, 7]
hist(list)


#13
import random

def guess(n, true, count):
    if n == true:
        print("Good job, KBTU! You guessed my number in", count, "guesses!")
        return
    elif n < true:
        n = int(input("Your guess is too low.\nTake a guess.\n"))
        guess(n, true, count + 1)
    elif n > true:
        n = int(input("Your guess is too high.\nTake a guess.\n"))
        guess(n, true, count + 1)

name = input("Hello! What is your name?\n")
n = int(input("Well, " + name + ", I am thinking of a number between 1 and 20.\nTake a guess.\n"))
true = random.randint(1, 20)
count = 1
guess(n, true, count)




# Dictionary of movies
#1
def isIMDB55(movie):
    if movie["imdb"] > 5.5:
        return True


#2
def sublistIMDB55(movies):
    newMovies = []
    for i in movies:
        if isIMDB55(i):
            newMovies.append(i)
    return newMovies


#3
def category(movies, cat):
    catMovies = []
    for i in movies:
        if i["category"] == cat:
            catMovies.append(i)
    return catMovies


#4
def avIMDB(movies):
    IMDBsum = count = 0
    for i in movies:
        IMDBsum += i["imdb"]
        count += 1
    return IMDBsum / count


#5
def IMDBofCategory(movies, cat):
    catMovies = category(movies, cat)
    return avIMDB(catMovies)


movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print(movies[3]["name"], "movie has IMDB is above 5.5: ", isIMDB55(movies[3]), "\n")
print("These movies have IMDB above 5.5:\n", sublistIMDB55(movies), "\n")
print("These movies are of Romance category:\n", category(movies, "Romance"), "\n")
print("The average IMDB of movies is: ", avIMDB(movies), "\n")
print("The average IMDB of movies with category Action is: ", IMDBofCategory(movies, "Action"))
