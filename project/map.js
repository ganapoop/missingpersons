
var initMap = function() {
    var global_counter = 0;

    var url_list = [];
    var address = 'San Diego, CA';
    var geocoder = new google.maps.Geocoder();
    var myOptions = {
        zoom: 4,
        center: {lat: 34.397, lng: -100.644},
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapTypeControl: true
    };
    var map = new google.maps.Map(document.getElementById('map'), myOptions);

    $.get(
        'http://localhost/~SaranyaGanapathy/bytehacks/locations.json?version=' + Math.random(),
        function( data ) {
            console.log(data);

            for (i in data.Points) {
                var point = data.Points[i];
                console.log(point.Location);
                console.log(point.URL);
                url_list[i] = point.URL;
                //d[point.Location] = url_link;
                geocoder.geocode(
                    {'address': point.Location},
                    function(results, status) {
                        if(status == google.maps.GeocoderStatus.OK) {
                            if(status != google.maps.GeocoderStatus.ZERO_RESULTS) {
                                console.log(global_counter);
                                global_counter++;
                                //console.log(results[0]);
                                var latitude = results[0].geometry.location.lat();
                                var longitude = results[0].geometry.location.lng();
                                //var place_name = results[0].formatted_address;
                                console.log(results[0]);
                                console.log('got here');
                                initialize(latitude, longitude, url_list[global_counter]);
                            } else {
                                alert("No results found");
                            }
                        } else {
                            alert("Geocode was not successful for the following reason: " + status);
                        }
                    }
                );
            }
        }
    );

    function initialize(latitude, longitude, place) {
        var latlng = new google.maps.LatLng(latitude, longitude);

        var marker = new google.maps.Marker({
            position: latlng,
            map: map,
            title: 'Location, property name',
            url: place
        });
    //     map.addListener('center_changed', function() {
    //      // 3 seconds after the center of the map has changed, pan back to the
    //      // marker.
    //      window.setTimeout(function() {
    //        map.panTo(marker.getPosition());
    //      }, 3000);
    //    });

       marker.addListener('click', function() {
        //  map.setZoom(8);
        //  map.setCenter(marker.getPosition());
         window.open(marker.url, "_blank");
       });
    }
};
