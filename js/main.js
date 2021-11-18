//Author Buddy Collins
"use strict"
var geojson;
var map;
var info = L.control();


window.onload = function () {
    createMap();
    createChart();
};


//-------------------------------------------------------------------------------------------------------------------
function createMap(){
// create a leaflet map with a dark basemap
map = L.map('mapid').setView([39.1839102,-95.9745134], 4.45);

// creates the map from mapbox api
L.tileLayer('https://api.mapbox.com/styles/v1/buddytheelf/ckvsqoj1h11xk14oafqc8fdcm/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYnVkZHl0aGVlbGYiLCJhIjoiY2p2czYxbHNlMndjdzN5cGI3ejI4aWJ5dyJ9.5IPoN9dD2-6boYGfX4ondQ', {
  maxZoom:7,
  minZoom:4,
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
}).addTo(map);


// adds the geojson data
$.getJSON("data/MSA.geojson", function(response){
    geojson = L.geoJSON(response, {
          onEachFeature: onEachFeature
    }).addTo(map);

    info.addTo(map);
});
};

//When adding the info
info.onAdd = function (map) {
    //"this" returns to info.
    this._div = L.DomUtil.create('div', 'info');
    //the following line calls info.update(props) function. Again, this refers to 'info' here
    this.update();
    return this._div;
};

//Update the info based on what state user has clicked on
info.update = function (props) {
    this._div.innerHTML = '<h4>Built up area</h4>' + (props ?
        '<b>' + props.NAME10 + '</b><br />' + Math.round(props.F2020_mean * 100) + '% BUA'
        : 'Hover over area');
};

//------------------------------------------------------------------------------------------------------------------


function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
    info.update(layer.feature.properties);

}


function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();

}
function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
    createLine(e.target.feature.properties);
}
function onEachFeature(feature, layer) {
    layer.on({
      mouseover: highlightFeature,
      mouseout: resetHighlight,
      click: zoomToFeature
    });
}
