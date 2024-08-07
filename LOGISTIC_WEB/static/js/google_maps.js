// Insert map datas from django
const location_data = JSON.parse(document.getElementById('map-data').textContent);
const location_lat = location_data[0]['lat'];
const location_lng = location_data[0]['lng'];

// Initialize and add the map
let map;

async function initMap() {
  // The location of Uluru
  const position = { lat: location_lat, lng: location_lng };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map"), {
    zoom: 4,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Uluru
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Uluru",
  });
}

initMap();