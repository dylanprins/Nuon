<?php
 
	$address = '3500 Jean Talon Ouest, Montreal, QC H3R 2E8 Canada';
	$coordinates = file_get_contents('http://maps.googleapis.com/maps/api/geocode/json?address=' . urlencode($address) . '&sensor=true');
	$coordinates = json_decode($coordinates);
 
	echo 'Latitude:' . $coordinates->results[0]->geometry->location->lat;
	echo 'Longitude:' . $coordinates->results[0]->geometry->location->lng;
 
	$lat = $coordinates->results[0]->geometry->location->lat;
	$lng = $coordinates->results[0]->geometry->location->lng;
 
?>
 
<!DOCTYPE html>
<html>
  <head>
    <title>Localizing the Map</title>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&language=en"></script>
    <script>
		function initialize() {
		  var mapOptions = {
			zoom: 15,
			center: new google.maps.LatLng('<?php echo $lat ?>', '<?php echo $lng ?>')
		  };
		  var map = new google.maps.Map(document.getElementById('map-canvas'),
			  mapOptions);
		}
 
		google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>