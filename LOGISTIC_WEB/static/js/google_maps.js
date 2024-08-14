// Insert map datas from django
const location_data = JSON.parse(document.getElementById('map-data').textContent);
const location_lat = location_data[0]['lat'];
const location_lng = location_data[0]['lng'];
var start_btn = document.getElementById("start-btn");
var end_btn = document.getElementById("end-btn");
var reset_btn = document.getElementById("reset-btn");
var search_address;
var search_start_address;
var search_end_address;

// Initialize and add the map
let map;
let marker;
let infoWindow;

start_btn.addEventListener("click", function(){setSelectedLocationAddress("start");},false);//
end_btn.addEventListener("click", function(){setSelectedLocationAddress("stop");},false);//
reset_btn.addEventListener("click",btnReset);

async function initMap() {
  // Request needed libraries.
  //@ts-ignore
  
  const [{ Map }, { AdvancedMarkerElement }] = await Promise.all([
    google.maps.importLibrary("marker"),
    google.maps.importLibrary("places"),
  ]);
  const directionsService = new google.maps.DirectionsService(); //
  const directionsRenderer = new google.maps.DirectionsRenderer(); //

  // Initialize the map.
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 38.963745, lng: 35.243322 },
    zoom: 6,
    mapId: "4504f8b37365c3d0",
    mapTypeControl: false,
  });

  directionsRenderer.setMap(map); //

  const onChangeHandler = function () {  //
    calculateAndDisplayRoute(directionsService, directionsRenderer);//
  };//

  document.getElementById("confirm-btn").addEventListener("click", onChangeHandler);//

  //@ts-ignore
  const placeAutocomplete = new google.maps.places.PlaceAutocompleteElement();

  //@ts-ignore
  placeAutocomplete.id = "place-autocomplete-input";

  const card = document.getElementById("place-autocomplete-card");

  //@ts-ignore
  card.appendChild(placeAutocomplete);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(card);
  // Create the marker and infowindow
  marker = new google.maps.marker.AdvancedMarkerElement({
    map,
  });
  infoWindow = new google.maps.InfoWindow({});
  // Add the gmp-placeselect listener, and display the results on the map.
  //@ts-ignore
  placeAutocomplete.addEventListener("gmp-placeselect", async ({ place }) => {
    await place.fetchFields({
      fields: ["displayName", "formattedAddress", "location"],
    });
    search_address = place.formattedAddress;
    // If the place has a geometry, then present it on a map.
    if (place.viewport) {
      map.fitBounds(place.viewport);
    } else {
      map.setCenter(place.location);           ////////////////////
      map.setZoom(17);
    }

    let content =
      '<div id="infowindow-content">' +
      '<span id="place-displayname" class="title">' +
      place.displayName +
      "</span><br />" +
      '<span id="place-address">' +
      place.formattedAddress +
      "</span>" +
      "</div>";
    updateInfoWindow(content, place.location);
    marker.position = place.location;
  });
}

// Helper function to create an info window.
function updateInfoWindow(content, center) {
  infoWindow.setContent(content);
  infoWindow.setPosition(center);
  infoWindow.open({
    map,
    anchor: marker,
    shouldFocus: false,
  });
}

function calculateAndDisplayRoute(directionsService, directionsRenderer) {//
  directionsService
    .route({
      origin: {
        query: search_start_address,
      },
      destination: {
        query: search_end_address,
      },
      travelMode: google.maps.TravelMode.DRIVING,
      avoidHighways: true,
    })
    .then((response) => {
      directionsRenderer.setDirections(response);
    })
    .catch((e) => window.alert("Directions request failed due to " + status));
}//

initMap();

function setSelectedLocationAddress(x){
  if(x=='start'){
    search_start_address=search_address;
    start_btn.innerHTML=search_address;
    start_btn.style.backgroundColor="gray";
  }
  else{
    search_end_address=search_address;
    end_btn.innerHTML=search_address;
    end_btn.style.backgroundColor="gray";
  }
}

function btnReset(){
  start_btn.style="background-color=gainsboro;";
  start_btn.innerHTML="Start";
  search_start_address="";
  end_btn.style="background-color=gainsboro;";
  end_btn.innerHTML="End";
  search_end_address="";
}
/* ********* Simple Render for Selected Location *********
  // The location of Selected on map.py
  const position = { lat: location_lat, lng: location_lng };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map"), {
    zoom: 15,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Uluru
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Selected_location",
  });
  
initMap();
  
********* Simple Render for Selected Location ********* */