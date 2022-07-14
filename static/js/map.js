var map;
var latlng;
var infowindow;
$(document).ready(function() {
    // get data set from the backend in a json structure
    var data = [];
    // var data = [{
    //         "description": "Location A",
    //         "location": "kurunegala",
    //         "latitude": "7.4818",
    //         "longitude": "80.3609"
    //     },
    //     {
    //         "description": "Location B",
    //         "location": "kandy",
    //         "latitude": "7.2906",
    //         "longitude": "80.6337"
    //     }
    // ]
    //if backend servie ready
    // $.ajax({ //library for JS help front-end to talk back-end, without having to reload the page
    //   url: "http://127.0.0.1:8000/request/locations/",
    //   async: true,
    //   dataType: 'json', // is a language
    //   success: function (data) {
    //     console.log(data);
    //     ViewCustInGoogleMap(data);
    //   }
    // }); 

    const getData = () => {
        fetch('http://127.0.0.1:8000/request/locations')
        .then(response => {
            return response.json();
        })
        .then(responseData => {
            console.log(responseData)
        })
        data = responseData;
    }
    getData();
    console.log(data);
    ViewCustInGoogleMap(data);
});
function ViewCustInGoogleMap(data) {
    var gm = google.maps; //create instance of google map
    //add initial map option
    var mapOptions = {
        center: new google.maps.LatLng(7.2906, 80.6337), 
        zoom: 9,
    };
    //bine html tag to show the google map and bind mapoptions
    map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
    //create instance of google information windown
    infowindow = new google.maps.InfoWindow();
    var marker, i;
    //loop through all the locations and point the mark in the google map
    for (var i = 0; i < data.length; i++) {
        marker = new gm.Marker({
            position: new gm.LatLng(data[i]['latitude'], data[i]['longitude']),
            map: map,
            // icon: MarkerImg
        });
  
        //add info for popup tooltip
        google.maps.event.addListener(
            marker,
            'click',
            (
                function(marker, i) {
                    return function() {
                        infowindow.setContent(data[i]['location'] + data[i]['garbage_type']);
                        infowindow.open(map, marker);
                    };
                }
            )(marker, i)
        );
    }
}