function randomColor() {
	var colors = ['#F65B83','#9662ED','#E4D6CD','#C8111D','#D4584C','#B3BEF4','#DAA447','#4D4075','#38D899','#43795F','#33D924','#A207BB','#6578FE'];
	return colors[Math.floor(Math.random()*colors.length)];
}

$(function(){
	// $('.highlight').each(function(){
	// 	$(this).css('background-color', randomColor() ).css('color', '#fff')
	// })
	$('.highlight').mouseenter(function(){
		$(this).css('background-color', randomColor() ).css('color', '#fff');
	}).mouseleave(function(){
		$(this).css('background-color', '#ddd').css('color', '#3C5A76');
	})
})