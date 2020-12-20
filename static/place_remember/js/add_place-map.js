let map = L.map('mapid', {zoomControl: false}).setView([51.505, -0.09], 12);
L.tileLayer(`https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${MAP_KEY}`, {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: MAP_KEY
}).addTo(map);
let marker = L.marker()
L.control.zoom({
    position: 'topright'
}).addTo(map);

function onMapClick(e) {
    marker.setLatLng(e.latlng).addTo(map);
    document.getElementById(lat_id).value=e.latlng.lat
    document.getElementById(lng_id).value=e.latlng.lng
}

map.on('click', onMapClick);
