import media
import fresh_tomatoes

#Create instances for each movie to be displayed.


blade_runner = media.Movie(
    'Blade Runner(1982)',
	'A blade runner must pursue and try to terminate four replicants who stole '
    'a ship in space and have returned to Earth to find their creator.',
    'https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg',
	'https://www.youtube.com/watch?v=eogpIG53Cis'
    )

total_recall = media.Movie(
    'Total Recall(1990)',
    'When a man goes for virtual vacation memories of the planet Mars, an unexp'
    'ected and harrowing series of events forces him to go to the planet for re'
    'al - or does he?',
    'https://upload.wikimedia.org/wikipedia/en/f/f9/Total_recall.jpg',
    'https://www.youtube.com/watch?v=WFMLGEHdIjE'
    )

screamers = media.Movie(
    'Screamers(1995)',
    '(SIRIUS 6B, Year 2078) On a distant mining planet ravaged by a decade of w'
    'ar, scientists have created the perfect weapon: a blade-wielding, self-rep'
    'licating race of killing devices known as...',
    'https://upload.wikimedia.org/wikipedia/en/e/eb/Screamersposter.jpg',
    'https://www.youtube.com/watch?v=WksPMueXkP4'
    )

minority_report = media.Movie(
    'Minority Report(2002)',
    'In a future where a special police unit is able to arrest murderers before'
    ' they commit their crimes, an officer from that unit is himself accused of'
    ' a future murder.',
    'https://upload.wikimedia.org/wikipedia/en/4/44/Minority_Report_Poster.jpg',
    'https://www.youtube.com/watch?v=lG7DGMgfOb8'
    )

a_scanner_darkly = media.Movie(
    'A Scanner Darkly(2006)',
	'An undercover cop in a not-too-distant future becomes involved with a dang'
    'erous new drug and begins to lose his own identity as a result.',
	'https://upload.wikimedia.org/wikipedia/en/7/75/A_Scanner_Darkly_Poster.jpg',  #NOQA
	'https://www.youtube.com/watch?v=lG7DGMgfOb8'
    )

the_adjustment_bureau = media.Movie(
    'The Adjustment Bureau(2011)',
    'The affair between a politician and a contemporary dancer is affected by m'
    'ysterious forces keeping the lovers apart.',
    'https://upload.wikimedia.org/wikipedia/en/1/1c/The_Adjustment_Bureau_Poster.jpg',  #NOQA
    'https://www.youtube.com/watch?v=wZJ0TP4nTaE'
    )

#Set the movies to be passed to the movie_page file
movies = [blade_runner, total_recall, screamers, minority_report,
		  a_scanner_darkly, the_adjustment_bureau]

#Function creates html file with a tile for each movie in the list and opens it
#in a web browser
fresh_tomatoes.open_movies_page(movies)
