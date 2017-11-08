import media 
import fresh_tomatoes

#Create instances for each movie to be displayed. 
blade_runner = media.Movie('Blade Runner(1982', 
						   'A blade runner must pursue and try to terminate fou'
						   'r replicants who stole a ship in space and have ret'
						   'urned to Earth to find their creator.',
						   'https://upload.wikimedia.org/wikipedia/en/5/53/'
						   'Blade_Runner_poster.jpg', 
						   'https://www.youtube.com/watch?v=eogpIG53Cis')

total_recall = media.Movie('Total Recall(1990)', 
						   'When a man goes for virtual vacation memories of th'
						   'e planet Mars, an unexpected and harrowing series o'
						   'f events forces him to go to the planet for real - '
						   'or does he?',
						   'https://upload.wikimedia.org/wikipedia/en/f/f9/Tota'
						   'l_recall.jpg', 
						   'https://www.youtube.com/watch?v=WFMLGEHdIjE')

screamers = media.Movie('Screamers(1995)', 
						'(SIRIUS 6B, Year 2078) On a distant mining planet r'
						'avaged by a decade of war, scientists have created '
						'the perfect weapon: a blade-wielding, self-replicat'
						'ing race of killing devices known as...',
						'https://upload.wikimedia.org/wikipedia/en/e/eb/Scre'
						'amersposter.jpg', 
						'https://www.youtube.com/watch?v=WksPMueXkP4')

movies = [blade_runner, total_recall, screamers]
fresh_tomatoes.open_movies_page(movies)