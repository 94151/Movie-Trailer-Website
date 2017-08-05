import fresh_tomatoes
import media
# first movie trailer
toy_story = media.Movie(
                        "Toy Story",
                        "A story of a boy",
                        "http://bit.ly/2tcNMeM",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# second movie trailer
print(toy_story.storyline)


avatar = media.Movie(
                     "Avatar",
                     "A marine on an alien planet",
                     "http://bit.ly/2hqw9Re",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

print(avatar.storyline)
avatar.show_trailer()

# third movie trailer
promethius = media.Movie(
                     "promethius",
                     "A Space story",
                     "http://bit.ly/2tpSFMY",
                     "https://www.youtube.com/watch?v=nmJOO6D5RvA")
print(promethius.storyline)
promethius.show_trailer()

# fourth movie trailer
Radha = media.Movie(
                     "Radha",
                     "A story of a Punjabi and Modern Girl",
                     "http://bit.ly/2uoGEvi",
                     "https://www.youtube.com/watch?v=U5Gyw-nGf1I")
print(Radha.storyline)
Radha.show_trailer()

# fivth movie trailer
tubelight = media.Movie(
                     "tubelight",
                     "A story of orphan innocent man",
                     "http://bit.ly/2rrOCQ2",
                     "https://www.youtube.com/watch?v=UKlkIzD-Yj8")
print(tubelight.storyline)
tubelight.show_trailer()

# six movie trailer
jagga_jasus = media.Movie(
                     "jagga_jasus",
                     "Two cartoons always dancing everywhere",
                     "http://bit.ly/2uoIjB5",
                     "https://www.youtube.com/watch?v=xtm48kJwL1I")
print(jagga_jasus.storyline)
jagga_jasus.show_trailer()
# movies variable holds all the movie trailer variables
movies = [toy_story, avatar, promethius, Radha, tubelight, jagga_jasus]
# fresh_tomatoes is html page. open function open this page in to the browser
fresh_tomatoes.open_movies_page(movies)
