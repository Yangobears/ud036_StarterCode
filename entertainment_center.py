import media
from fresh_tomatoes import open_movies_page

#create movie objects
finding_dory = media.Movie("Finding Dory", 
                           "http://img.lum.dolimg.com/v1/images/uk_dory_flexherobg_n_6032b443.jpeg?region=0,0,1500,844&width=1200",  # NOQA
                           "https://www.youtube.com/watch?v=oddWuCHBmzA")

finding_nemo = media.Movie("Finding Nemo",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                           "https://youtu.be/wZdpNglLbt8")

inside_out = media.Movie("Inside Out", 
                         "http://ia.media-imdb.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
                         "https://youtu.be/seMwpP0yeu4")

#put movie objects into a list
movies = [finding_dory, finding_nemo, inside_out]

#call given function to render the page
open_movies_page(movies)
