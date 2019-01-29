forecasts_url = "http://192.168.99.204:8080/api/forecasts"
advice_url = "https://api.adviceslip.com/advice"
forecasts_url = "http://sf-pyw.mosyag.in/m04/api/forecasts"

$("#main-header").click(function(){

	$.getJSON(forecasts_url, function(data){
		set_content_in_divs(data["prophecies"])	
	});

});


function set_content_in_divs(paragraphs) {
  $.each(paragraphs, function(i, d) {
    p = $("#p-" + i);
    p.html("<p>" + d + "</p>");
})}