import random 

def randomColor():
	x = random.randint(0, 16777215)
	return "#%x" % x


project_list = [
	{
		'title': 'Musique',
		'link': 'musique',
		'bgColor': randomColor(),
		'previewImage': '/static/img/musique/mobile.png',
		'images' : ['/static/img/musique/m1.jpeg','/static/img/musique/m2.jpeg','/static/img/musique/m3.jpeg','/static/img/musique/m4.jpeg'],
		'url' : 'musique.herokuapp.com',
		'tech' : 'ode.js, javascript, html5, css3',
		'created': 'Summer 2011',
		'description': 'Musique is a tool to collaboratively generate and enjoy playlists. There is one host computer that plays the actual music, but any connected client can add songs, control the volume, and toggle music play/pause via a web interface.',
		'add' : "Most of the code base was built in one night at Mozilla's World Series of Hack"
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
		'title': 'ReviewNT',
		'link' : 'reviewnt',
		'bgColor': randomColor(),
		'previewImage': '/static/img/reviewnt/rnt4.png',
		'images' : ['/static/img/reviewnt/rnt4.png','/static/img/reviewnt/rnt1.jpeg','/static/img/reviewnt/rnt2.jpeg', '/static/img/reviewnt/rnt3.jpeg'],
		'url' : None,
		'tech' : "javascript, PHP, MySQL, html5, css3",
		'created': 'Fall/Winter 2010',
		'description': 'ReviewNT was a site to provide third-party,constructive reviews for teachers',
		'add' : "My district's superattendent and the teacher union president did not want this site to be released so they blocked it from ever collecting a review"
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
		'images' : ['/static/img/cntrlr/tp1.png','/static/img/cntrlr/tp2.png'],
		'url' : None,
		'tech' : None,
		'created': None,
		'description': None,
		'add' : None
	}
]