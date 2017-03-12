import random

def randomColor():
	x = random.randint(0, 16777215)
	return "#%x" % x


paper_list = [
	{
		'title' :  'Deep Feature Synthesis: Towards Automating Data Science Endeavors',
		'file'  : 'papers/DSAA_DSM_2015.pdf',
		'note'  : ' appeared in International IEEE/ACM Data Science and Advance Analytics Conference, 2015 (acceptance rate - 10%) '
	},
	{
		'title' :  'Label, Segment, Featurize: a cross domain framework for prediction engineering',
		'file'  : 'papers/DSAA_LSF_2016.pdf',
		'note'  : ' appeared in International IEEE/ACM Data Science and Advance Analytics Conference, 2016'
	},
	{
		'title' :  'CommunityFinder: Software to Analyze Communities that Develop in MOOC Discussion Forums',
		'file'  : 'papers/community_finder.pdf',
	},
	{
		'title' :  'Activity Classification using Smartphone Accelerometer Data',
		'file'  : 'papers/activity_classification.pdf'
	},
	{
		'title' :  'ColorCrack: Identifying Cracks in Glass',
		'file'  : 'papers/color_crack.pdf',
	},
	{
		'title' :  'OK: OAuth 2.0 interface for the Kerberos V5 Authentication Protocol',
		'file'  : 'papers/ok_server.pdf',
		'code'	: 'https://github.com/bfaviero/ok'
	},
]


project_list = [
	{
		'title': 'Relert',
		'link' : 'relert',
		'bgColor': randomColor(),
		'previewImage': '/static/img/relert/re1-thumb.jpg',
		'images' : ['/static/img/relert/re1.jpg','/static/img/relert/re2.jpg'],
		'url' : 'http://relert.me',
		'tech' : 'javascript, html5 audio api',
		'created': 'Fall 2011',
		'description': "A better way to share a link. Get an alert when your link is viewed and read comments from the viewer",
		'add' : "I built this to solve a problem I had when my Dad and brother would send me links and expect that I reply just to say I read it."
	},
	{
		'title': 'KangaCruise',
		'link' : 'kangacruise',
		'bgColor': randomColor(),
		'previewImage': '/static/img/kc/kc1-thumb.jpg',
		'images' : ['/static/img/kc/kc1.jpg','/static/img/kc/kc2.jpg'],
		'url' : None,
		'tech' : 'javascript, python',
		'created': 'Winter 2012',
		'description': "KangaCruise is a vacation discovery engine that helps travelers sift through thousands of cruises to find the best one for them. We built a virtual travel agent artificial intelligence that guides the user to the perfect vaction",
		'add' : "I worked on KangaCruise full time with Colin Sidoti and Louis Sobel during the month of January as part of MIT's Independent Activites Period"
	},
	{
		'title': 'Hungry4',
		'link' : 'hungry4',
		'bgColor': randomColor(),
		'previewImage': '/static/img/hungry4/h41-thumb.jpg',
		'images' : ['/static/img/hungry4/h41.jpg','/static/img/hungry4/h42.jpg','/static/img/hungry4/h43.jpg'],
		'url' : None,
		'tech' : "javascript, jquery, node.js, foodspotting/google API's",
		'created': 'Summer 2012',
		'description': "It's hard to figure out what you're hungry for. Hungry4 guides you to great local food through photos of actual dishes. Tell it what looks tasty and it helps you find exactly what you're Hungry4.",
		'add' : "I love food and I take pictures of everything I eat."
	},
	{
		'title': 'Circle Session',
		'link' : 'circle',
		'bgColor': randomColor(),
		'previewImage': '/static/img/circle/cs2-thumb.jpg',
		'images' : ['/static/img/circle/cs1.jpg','/static/img/circle/cs2.png','/static/img/circle/cs3.png','/static/img/circle/cs4.png','/static/img/circle/cs5.png','/static/img/circle/cs6.png'],
		'url' : None,
		'tech' : 'javascript, node.js, html5',
		'created': 'Fall 2011',
		'description': "Creating music is a difficult endeavor, but creating with others makes the process easier and more fun for everyone involved. Therefore, giving people the tools to create music collaboratively is an enticing prospect. Players use web-connected smart phones, tablets, or laptops to join a \"session\", pick an instrument to play, and finally play music with other session members. All players are connected to central host computer that plays and displays the music.",
		'add' : "I found that many user experience design changes could be made to improve the game. First, the game is best played by 2-4 players. This means I should design that game to limit the number of players in a room to those numbers. Next, the game does not work as well if everyone is playing the same instrument. Thus, it would be a good idea to prevent players from joining a room with an instrument that already exists in that room. Also, I found some instruments work better than others. I could try to create instrument collections that specified instruments that had to be used together. Finally, the timing in which players enter game should not be at will. I found that the best gameplay came from sessions where each user entered spaced out from each other. This gave one user a time to start a beat before the next player joined."
	},
	{
		'title': 'Musique',
		'link': 'musique',
		'bgColor': randomColor(),
		'previewImage': '/static/img/musique/mobile.png',
		'images' : ['/static/img/musique/m1.jpeg','/static/img/musique/m2.jpeg','/static/img/musique/m3.jpeg','/static/img/musique/m4.jpeg'],
		'url' : 'http://musique.herokuapp.com',
		'tech' : 'ode.js, javascript, html5, css3',
		'created': 'Summer 2011',
		'description': 'Musique is a tool to collaboratively generate and enjoy playlists. There is one host computer that plays the actual music, but any connected client can add songs, control the volume, and toggle music play/pause via a web interface.',
		# 'add' : "Most of the code base was built in one night at Mozilla's World Series of Hack"
	},
	{
		'title': 'Cntrlr',
		'link' : 'cntrlr',
		'bgColor': randomColor(),
		'previewImage': '/static/img/cntrlr/ios-1.png',
		'images' : ['/static/img/cntrlr/tp1.png','/static/img/cntrlr/tp2.png'],
		'url' : None,
		'tech' : 'node.js, javascript, html5, css3',
		'created': 'Summer 2011',
		'description': 'Cntrlr gives you  full control of you  desktop browser with any mobile device. After installing a browser extension or bookmarklet, users can connect any  device with a web browser (tablet, smartphone, another computer) and control the host browser. Cntrlr allows users to interially scroll a web page, fill in text inputs, change URL, and draw on screen -- all from a mobile device!',
		'add' : "Made in one night during Linkedin's intern hackday. Made it to final round of top 15 projects."
	},
	{
		'title': 'MIT Web Finger',
		'link' : 'finger',
		'bgColor': randomColor(),
		'previewImage': '/static/img/mwf/mwf1.png',
		'images' : ['/static/img/mwf/mwf1.png','/static/img/mwf/mwf2.png','/static/img/mwf/mwf3.png'],
		'url' : None,
		'tech' : 'javascript, python, flask',
		'created': 'Spring 2012',
		'description': "Finding people in the MIT web directory is hard. All the information is there, but you can only search by last name, full name, and email address. To solve this problem, I scraped all 30,000 people associated with MIT and indexed the ~4,000 undergrads by every possible category. As a result, you are able to effectively find someone with numerous pieces of incomplete information e.g freshmen, in this dorm, majoring in Biology whose name starts with an S.",
		'add' : "This project also spawned another hack where I used the information I had scraped to print out a flyer advertising a party I was hosting to every undergrad at MIT"
	},
	{
		'title': 'WuFi',
		'link' : 'wufi',
		'bgColor': randomColor(),
		'previewImage': '/static/img/wufi/wufi1.png',
		'images' : ['/static/img/wufi/wufi1.png'],
		'url' : 'http://wufi.herokuapp.com',
		'tech' : "javascript, phonegap, python, flask",
		'created': 'Summer 2012',
		'description': "WuFi guesses the word you're thinking of. It's a mobile app that comes to your aid when you can't figure out that word on the tip of your tounge. Give it a definition and it intelligently figures out the word you're describing",
		'add' : "Uses phonegap to work as a native app on mobile."
	},
	{
		'title': 'ReviewNT',
		'link' : 'reviewnt',
		'bgColor': randomColor(),
		'previewImage': '/static/img/reviewnt/homepage.png',
		'images' : ['/static/img/reviewnt/homepage.png','/static/img/reviewnt/rnt4.png','/static/img/reviewnt/rnt1.jpeg','/static/img/reviewnt/rnt2.jpeg', '/static/img/reviewnt/rnt3.jpeg'],
		'url' : None,
		'tech' : "javascript, PHP, MySQL, html5, css3",
		'created': 'Fall/Winter 2010',
		'description': 'ReviewNT was a site to provide third-party, constructive reviews for teachers',
		# 'add' : "My district's superattendent and the teacher union president did not want this site to be released so they blocked it from ever collecting a review"
	},
	{
		'title': 'Digital Poem',
		'link' : 'digital',
		'bgColor': randomColor(),
		'previewImage': '/static/img/poem/dp1.png',
		'images' : ['/static/img/poem/dp1.png','/static/img/poem/dp2.png'],
		'url' : None,
		'tech' : 'javascript, html5 audio api',
		'created': 'Fall 2011',
		'description': "This project aimed to combine two ways to enjoy poetry: reading it yourself and listening to the author speak it in his own words. The site displayed the text of a poem on the screen for the user to hover over words at her own pace and hear the original author speaking.",
		'add' : ""
	},
	{
		'title': 'Groupon',
		'link' : 'groupon',
		'bgColor': randomColor(),
		'previewImage': '/static/img/groupon/screen.png',
		'images' : [],
		'url' : None,
		'tech' : 'webOS Mojo SDK, javascript, html5, css3',
		'created': 'Summer 2010',
		'description': "Groupon is an app I made to feed the daily deal from Groupon to a webOS device. Using the system GPS, the app retrieves deals by location by utilizing the RESTful API provided by Groupon. In addition, it has a built-in timer to alert the user at a set time on a daily basis of a deal.",
		'add' : "I planned to release this program for free in the official App Catalog and use Groupon's affiliate program to generate revenues. Never got around to it..."
	},
	{
		'title': 'Frisbee Launcher',
		'link' : 'fris',
		'bgColor': randomColor(),
		'previewImage': '/static/img/frisbeelauncher/fris1.jpg',
		'images' : ['/static/img/frisbeelauncher/fris1.jpg','/static/img/frisbeelauncher/fris2.jpg','/static/img/frisbeelauncher/fris3.jpg','/static/img/frisbeelauncher/fris4.jpg','/static/img/frisbeelauncher/fris5.jpg','/static/img/frisbeelauncher/fris6.jpg','/static/img/frisbeelauncher/fris7.jpg','/static/img/frisbeelauncher/fris8.jpg','/static/img/frisbeelauncher/fris9.jpg','/static/img/frisbeelauncher/fris10.jpg'],
		'url' : None,
		'tech' : None,
		'created': 'Summer 2010',
		'description': "After doing some research through youtube videos, I figured this would be an easy project -- it was not. A lot of complications came up that I wasn't expecting, such as the lawn edger motor I used being too fast or the difficulty in bending aluminum to a perfect circle. Most of all, I was doing this is my garage which has almost no tools.",
		'add' : None
	},
	{
		'title': 'Trajectory',
		'link' : 'trajectory',
		'bgColor': randomColor(),
		'previewImage': '/static/img/trajectory/traj1.jpg',
		'images' : ['/static/img/trajectory/traj1.jpg','/static/img/trajectory/traj2.jpg','/static/img/trajectory/traj3.jpg','/static/img/trajectory/traj4.jpg','/static/img/trajectory/traj5.jpg','/static/img/trajectory/traj6.jpg'],
		'url' : None,
		'tech' : None,
		'created': '2008-2010',
		'description': 'This is a precision golf ball launching device. It was Science Olympiad event that I competed in for two years. Below are pictures of the device I built with two team members.',
		'add' : None
	}


]

ex = [
	{
		'title': '',
		'link' : '',
		'bgColor': randomColor(),
		'previewImage': '',
		'images' : [],
		'url' : None,
		'tech' : None,
		'created': None,
		'description': None,
		'add' : None
	}
]
