var map;

function initialize(){
    var latlng = new google.maps.LatLng(35.67722222, 139.74777777);

    var myOptions = {
	             zoom: 12,
	             center: latlng,
	             mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map_canvas"),
			      myOptions);
}

function addMarker(lat, lng){
    var latlng = new google.maps.LatLng(lat, lng);
    var marker = new google.maps.Marker({
	                                  position: latlng,
	                                  map: map
    });
}

function setPosition(lat, lng){
    map.panTo(new google.maps.LatLng(lat, lng))
}
