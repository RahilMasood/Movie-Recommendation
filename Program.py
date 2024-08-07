# Sample movie dataset (title, description, genres, ratings)
movies = [
    {
        "title": "The Shawshank Redemption",
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "genres": ["Drama"],
        "ratings": 9.3
    },
    {
        "title": "The Godfather",
        "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "genres": ["Crime", "Drama"],
        "ratings": 9.2
    },
    {
        "title": "The Dark Knight",
        "description": "When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
        "genres": ["Action", "Crime", "Drama"],
        "ratings": 9.0
    },
    # Add more movies as needed
]

def print_movie_list(result):
    if len(result)!=0:
        for i in range(len(result)):
            print("\n+------------------------------------------------------------------------------+")
            print("\nTitle: ",result[i]["title"])
            print("\nDescription:\n",result[i]["description"])
            print("\nGenre: ",result[i]["genres"])
            print("\nRating: ",result[i]["ratings"])
            print("\n+------------------------------------------------------------------------------+")
    else:
        print("\nNo Such Movies Found")

#Functtion To Get Similar Strings
def check_similarity(string1,string2):
    words1=string1.lower().split()
    words2=string2.lower().split()
    res=False
    for i in words1:
        if i in words2:
            res=True
    if res:
        return res
    else:
        return False
        

#Function To Search Movies By Title
def search_by_title(string):
    result=[]
    for i in range(len(movies)):
        if check_similarity(string,movies[i]["title"]):
            result.append(movies[i])
    return result

#Function To Search By Description
def search_by_description(string):
    result=[]
    for i in range(len(movies)):
        if check_similarity(string,movies[i]["desrciption"]):
            result.append(movies[i])
    return result

#Function To Search By Rating
def search_by_rating(rList):
    result=[]
    if len(rList)==1:
        for i in range(len(movies)):
            if movies[i]["ratings"]==int(rList[0]):
                result.append(movies[i])
        return result
    elif rList[0] in ["<",">","<=",">="]:
        if rList[0]==">":
            for i in range(len(movies)):
                if movies[i]["ratings"]>int(rList[1]):
                    result.append(movies[i])
            return result
        elif rList[0]=="<":
            for i in range(len(movies)):
                if movies[i]["ratings"]<int(rList[1]):
                    result.append(movies[i])
            return result
        elif rList[0]==">=":
            for i in range(len(movies)):
                if movies[i]["ratings"]>=int(rList[1]):
                    result.append(movies[i])
            return result
        elif rList[0]=="<=":
            for i in range(len(movies)):
                if movies[i]["ratings"]<=int(rList[1]):
                    result.append(movies[i])
            return result
    else:
        print("Incorrect Input")

#Function To Search By Genre
def search_by_genre(genre_list):
    result=[]
    for i in range (len(movies)):
        for j in range(len(movies[i]["genres"])):
            if movies[i]["genres"][j] in genre_list:
                result.append(movies[i])
                continue
    return result
                
        

print("+--------------- MOVIE RECOMMENDATION SYSTEM ---------------+\n")
print("Search Based On:\n--> Title\n--> Description\n--> Genre\n--> Rating\n")
choices=["title","description","genre","rating"]

while True:
    search_result=[]
    user_choice=input("\nEnter Your Choice: ")
    
    if user_choice.lower() in choices:

        #Searching Based On Title
        
        if user_choice.lower()==choices[0]:
            movie_title=input("\nEnter Movie Title: ")
            search_result=search_by_title(movie_title)
            print_movie_list(search_result)
            user_choice=input("Want To Search Again? (Y/N): ")
            if user_choice.lower()=="y":
                continue
            else:
                break

            
        #Searching Based On Description
        
        elif user_choice.lower()==choices[1]:
            movie_desc=input("\nEnter Movie Description: ")
            search_result=search_by_description(movie_desc)
            print_movie_list(search_result)
            user_choice=input("Want To Search Again? (Y/N): ")
            if user_choice.lower()=="y":
                continue
            else:
                break

        #Search Based On Genre
        elif user_choice.lower()==choices[2]:
            movie_genre=input("\nEnter Genres: ").split()
            print(movie_genre)
            search_result=search_by_genre(movie_genre)
            print_movie_list(search_result)
            user_choice=input("Want To Search Again? (Y/N): ")
            if user_choice.lower()=="y":
                continue
            else:
                break

        #Search Based On Rating
        elif user_choice.lower()==choices[3]:
            movie_rating=input("\nEnter Movie Rating(Eg: 8 OR > 8): ").split()
            search_result=search_by_rating(movie_rating)
            print_movie_list(search_result)
            user_choice=input("Want To Search Again? (Y/N): ")
            if user_choice.lower()=="y":
                continue
            else:
                break
print("+--------------- THANK YOU ---------------+\n")
            
