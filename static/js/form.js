

$(document).ready(function() {
	 
	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#patient').val(),
				mood : $('#mood option:selected').val(),
				motivation : $('#motivation option:selected').val(),
				attention : $('#attention option:selected').val(),
				irritability : $('#irritability option:selected').val(),
				anxiety : $('#anxiety option:selected').val(),
				sleep_quantity: $('#sleep_quantity option:selected').val(),
				cig : $('#cig').val(),
				caf: $('#caf').val(),
				wake: $('#wake').val(),
				sleep: $('#sleep').val(),
			},
			type : 'POST',
			url : '/process',
			
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.prediction).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});


	

});