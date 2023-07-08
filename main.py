URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


from bs4 import BeautifulSoup as bs
#Beautiful Soup is a Python library for pulling data out of HTML and XML files.
import requests
# Need to install bs and requsts packages while opening a fresh file.

response = requests.get(URL)
website_html = response.text

soup = bs(website_html,"html.parser")
print(soup.title())

movies_tags = soup.find_all(name="h3",class_="title")
# we find this by inspecting the webpage and all movie title are under h3 tag and class = "title")
print(movies_tags)

movie_names =[]
for movie in movies_tags:
    movie_names.append(movie.getText())
    #we get only the text of the movie instead of the html line

# print(movie_names[::-1])
movie_names.reverse()
print(movie_names)

# Reversing the list obtained from the websiite from (100,99,98,97.. 3,2,1) to (1,2,3,...99,100)

with open("top-100movies.txt",mode="w", encoding="utf-8") as file:
    # create a txt file and write the movies
    # add encoding = "utf-8" to remove UnicodeEncodeError: 'charmap' codec can't encode characters in position 28-29:
    for movie in movie_names:
        file.write(f"{movie}\n")
        # \n to add each movies in different lines
