$(document).ready(function() {

	// toggle recommend box result page
	$('.input-container .input-form input').focus(function () {
		$('.recom-toggle').css({
			'display' : 'block'
		})
	});

	$('.input-container .input-form input').focusout(function () {
		$('.recom-toggle').css({
			'display' : 'none'
		})
	});


	// toogle recommend box index page

	$('.input-google .item-input input').focus(function () {
		$('.recom-toggle-index').css({
			'display' : 'block'
		})
	});

	$('.input-google .item-input input').focusout(function () {
		$('.recom-toggle-index').css({
			'display' : 'none'
		})
	});
});