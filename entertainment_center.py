import fresh_tomatoes
import telugu_movies
import hindi_movies
import media

taxiwala = media.Movie("Taxi Wala", "Telugu",
                       "A happy-go-lucky graduate moves to the city in search of a job. When nothing seems to work out for him, he decides to become a taxi driver to make a living. On his hunt for a car, he stumbles upon a vintage car. He gives it a makeover and the car turns his luck around. However, his joy is short-lived as he soon finds out that the car is possessed",
                       "https://www.telugu360.com/wp-content/uploads/2018/11/Taxiwala-Review-Rating-VIJAY-Deverakonda.jpg",
                       "https://youtu.be/9KN3dbZVRwQ")

pplm = media.Movie("Padi Padi Leche Manasu", "Telugu",
                   "It's a Telugu-speaking community in Kolkata where a rebellious youngster Surya falls for a medical student Vaishali. The love story isn't as simple as it appears to be. Surya doesn't let Vaishali realise his true identity. There's an obvious conflict, there's a natural disaster and a possible medical disorder too. How do these threads come together?",
                   "https://www.filmibeat.com/img/220x100x275/popcorn/movie_posters/padi-padi-leche-manasu-20180725104000-16970.jpg",
                   "https://youtu.be/O7oOl5oyTQg")

hgpk = media.Movie("Hello Guru Prema Kosame", "Telugu",
                   "A middle class boy Sanju from Kakinada comes to Hyderabad for his IT job. While he stays in the house of a family friend Vishwanath in the city, Sanju falls for his daughter Anupama soon. Tension prevails in the house. Yet, the rapport between Sanju and Vishwanath promises some fun and here's a predictable terrain that's however enjoyable for a viewer",
                   "https://in.bmscdn.com/iedb/movies/images/website/poster/large/hello-guru-prema-kosame-et00075763-15-05-2018-10-11-23.jpg",
                   "https://youtu.be/8Q4o87KPInY")

zero = media.Movie("Zero", "Hindi",
                   "The story revolves around Bauua Singh, a vertically challenged man, who is full of charm and wit, with a pinch of arrogance. Born to a wealthy family and raised in an environment of affluence and indulgence, Bauua was never failed by Meerut or its people. But when he meets two women, his experiences with these women take him on a journey to broaden his horizons to find a purpose he never knew he had",
                   "https://i.pinimg.com/736x/8f/0d/63/8f0d63751e151f63f77c6e478c219118.jpg",
                   "https://youtu.be/Ru4lEmhHTF4")

simmba = media.Movie("Simmba", "Hindi",
                   "Simmba is an orphan from Shivgadh from where our beloved Singham was born and raised. Contrary to the philosophies of Singham, Simmba believes that a Corrupt Officer's life is an ideal life which inspires him to become one. While Simmba enjoys all the perks of being an immoral and unethical Police Officer, a twist in the tale transforms him and forces him to choose the righteous path",
                   "http://im.rediff.com/movies/2017/dec/07simmba.jpg",
                   "https://youtu.be/PtFY3WHztZc")

kedarnath = media.Movie("Kedarnath", "Hindi",
                   "Kedarnath is a potent combination of love and religion, of passion and spirituality set on a 14-kilometer pilgrimage from Gauri Kund to Kedarnath - the 2000-year-old holy temple of Lord Shiva. Mansoor, a reserved and reticent porter, helps pilgrims make an arduous journey to the temple town. His world turns around when he meets the beautiful and rebellious Mukku, who draws him into a whirlwind of intense love",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/1/19/Kedarnath_film_Poster.jpg/220px-Kedarnath_film_Poster.jpg",
                   "https://youtu.be/03-KVRmd3xo")

movies = [pplm, taxiwala, hgpk, simmba, zero, kedarnath]
fresh_tomatoes.open_movies_page(movies)

movies = [pplm, taxiwala, hgpk]
telugu_movies.open_movies_page(movies)

movies = [simmba, zero, kedarnath]
hindi_movies.open_movies_page(movies)
