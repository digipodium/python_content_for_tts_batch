from example1 import Movie

m1 = Movie("IRON MAN",2005,"blah blah")
m2 = Movie("INCEPTION",2014,"Christophar Nolan",['Leonardo Dicaprio'],"movie about dreaming")
m3 = Movie("GUARDIANS OF GALAXY",2016,"James Gunn",['Chris Pratt','Vin Diesel'])

print(m1.view_details())
print(m1.director)

movies =[m1,m2,m3]
for m in movies:
    print(m)