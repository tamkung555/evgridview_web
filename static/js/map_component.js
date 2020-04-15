const markerSourceGreen = new ol.source.Vector();
const markerSourceYellow = new ol.source.Vector();
const markerSourceRed = new ol.source.Vector();
    

var markerStyleRed = new ol.style.Style({
    image: new ol.style.Icon(({
        opacity: 1,
        scale: 1,
        src: "{% static 'icons/red.png' %}"
    }))
});

var markerStyleYellow = new ol.style.Style({
  image: new ol.style.Icon(({
      opacity: 1,
      scale: 1,
      src: "{% static 'icons/yellow.png' %}"
  }))
});

var markerStyleGreen = new ol.style.Style({
  image: new ol.style.Icon(({
      opacity: 1,
      scale: 1,
      src: "{% static 'icons/green.png' %}"
  }))
});


var vectorLayerGreen = new ol.layer.Vector({
    source: markerSourceGreen,
    style: markerStyleGreen,
});

var vectorLayerYellow = new ol.layer.Vector({
  source: markerSourceYellow,
  style: markerStyleYellow,
});

var vectorLayerRed = new ol.layer.Vector({
source: markerSourceRed,
style: markerStyleRed,
});

var map_layer = new ol.layer.Tile({
  source: new ol.source.OSM(),
});

var map_view = new ol.View({
  center: ol.proj.fromLonLat([parseFloat(99.007198), parseFloat(18.773642)]), 
  zoom: 15,
});

//Declare Map Object
var map = new ol.Map({
  target: 'map',
  layers: [map_layer, vectorLayerGreen, vectorLayerYellow, vectorLayerRed],
  view: map_view,
  
});  //End of map Object

function plotMarker(lat, lon, pea, color){
    
    var iconFeature = new ol.Feature({
      geometry: new ol.geom.Point(ol.proj.transform([parseFloat(lon), parseFloat(lat)], 'EPSG:4326', 'EPSG:3857')),
      pea: pea,
    });

    if(color == 'green'){

      markerSourceGreen.addFeature(iconFeature);

    } else if (color == 'yellow'){

      markerSourceYellow.addFeature(iconFeature);

    } else if (color == 'red'){
      
      markerSourceRed.addFeature(iconFeature);

    }
    
};

function handleCallback(){
  var x = document.getElementById("year").value;
  markerSourceGreen.clear()
  markerSourceYellow.clear()
  markerSourceRed.clear()

    //   {% for i in data %}

    //       var data = '{{i|escapejs}}'
    //       var lat = '{{i.lat|escapejs}}'
    //       var lon = '{{i.lon|escapejs}}'
    //       var pea = '{{i.peano|escapejs}}'
    //       var risk = '{{i.risk|escapejs}}'
    //       var color = JSON.parse(risk)
    //       plotMarker(lat, lon, pea, color[x])

    //   {% endfor %}

};

var alltr = []
  
//   {% for i in data %}

//       alltr.push('{{i|escapejs}}')
//       var data = '{{i|escapejs}}'
//       var lat = '{{i.lat|escapejs}}'
//       var lon = '{{i.lon|escapejs}}'
//       var pea = '{{i.peano|escapejs}}'
//       var risk = '{{i.risk|escapejs}}'
//       var color = JSON.parse(risk)
//       var x = document.getElementById("year").value;
//       plotMarker(lat, lon, pea, color[x])

//   {% endfor %}

var element = document.getElementById('popup');
var popup = new ol.Overlay({
    element: element,
    positioning: 'bottom-center',
    stopEvent: false,
    offset: [0, -10]
});
map.addOverlay(popup);
map.on('click', function(evt) {

var feature = map.forEachFeatureAtPixel(evt.pixel,
    function(feature) {
    return feature;
    });
if (feature) {
    var coordinates = feature.getGeometry().getCoordinates();
    popup.setPosition(coordinates);
    console.log(coordinates)
    //console.log(typeof(feature.get('pea')))
    console.log( document.getElementById("popup").innerText)

    //document.getElementById("popup").innerText = feature.get('pea')
    $(element).popover({
    placement: 'top',
    html: true,
    content: feature.get('pea')
    });
    $(element).popover('show');
} else {
    $(element).popover('destroy');
}

});
