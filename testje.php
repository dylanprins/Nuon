<?php
 
	$address = '3500 Jean Talon Ouest, Montreal, QC H3R 2E8 Canada';
	$coordinates = file_get_contents('http://maps.googleapis.com/maps/api/geocode/json?address=' . urlencode($address) . '&sensor=true');
	$coordinates = json_decode($coordinates);
 
	echo 'Latitude:' . $coordinates->results[0]->geometry->location->lat;
	echo 'Longitude:' . $coordinates->results[0]->geometry->location->lng;
 
?>