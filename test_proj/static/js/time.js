$( document ).ready(function() {
   $("#id_time_of_receipt").empty();

   $("#id_date_of_receipt, #id_doctor").change(function() {
   		$("#id_time_of_receipt").empty();
   		var date = $('#id_date_of_receipt').val();
   		var doctor = $('#id_doctor').val();
   		if ( doctor != "" && date != ""){
   			 $.ajax({
		     type: "GET",
		     url: url,
		     data: {'date': date, 'doctor':doctor},
		     success: function(response){
					for(var k in response){
					$('#id_time_of_receipt')
				        .append($("<option></option>")
					    .attr("value",k)
					    .text(response[k]));
					}
					if ($.isEmptyObject(response)) {
						    $("#id_time_of_receipt").append('<option value="" disabled selected>Свободного времени нет </option>');
						}
               }
		   });
		}
    	});	
});
	