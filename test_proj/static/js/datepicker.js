$( document ).ready(function() {
   $(function() {
	  	$.datepicker.setDefaults(
	  		$.extend($.datepicker.regional["ru"])
	  		);
	    $( ".datepicker" ).datepicker({
	            inline: true,
	            showOtherMonths: true,
	            monthNames: ['Январь', 'Февраль', 'Март', 'Апрель',
				'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
				'Октябрь', 'Ноябрь', 'Декабрь'],
	            dayNamesMin: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
	            firstDay: 1,
	        });
	  });
});