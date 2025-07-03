movies = ["GOAT","Avengers","Alita Battle Angel","Endgame","kutty"]
print(movies)
print("First index : ",movies[0])
print("Last index : ",movies[(len(movies)-1)])

movies[1]="Tourist Family"
print("Updated the second movie : ",movies)

removed_movie_1 = movies.pop()
print(movies)
movies.remove("Endgame")
print(movies)
print("Length of the movies :  ",len(movies) )
print("GOAT" in movies)

for movie in movies : {
    print(movie)
}
movies.sort()
print(movies)
movies.reverse()
print(movies)

squares = [x**2 for x in range(10)]
print(squares)
even = [x for x in squares if x %2==0]
print(even)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])
movies.extend(["Ghili","Asuran","GOAT"])
print(movies)
no = movies.count("GOAT")
print(no)
second = movies.index("Ghili")
print(second)