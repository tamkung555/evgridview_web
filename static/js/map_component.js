   
        var style_aoj = new ol.style.Style({ //Style Object for AOJ Polygon
          fill: new ol.style.Fill({
          color: 'rgba(0, 8, 2, 0.6)'
          }),
          stroke: new ol.style.Stroke({
          color: '#78DFA7',
          width: 2
          }),
          
      });

      var markerSourceGreen = new ol.source.Vector();
      var markerSourceYellow = new ol.source.Vector();
      var markerSourceRed = new ol.source.Vector();
      var markerSourceDefault = new ol.source.Vector();
      
      var extend;
      var markerStyleRed = new ol.style.Style({
          image: new ol.style.Icon(({
              opacity: 1,
              scale: 0.6,
              src: "/static/icons/red.png"
          }))
      });
      
      var markerStyleYellow = new ol.style.Style({
          image: new ol.style.Icon(({
              opacity: 1,
              scale: 0.6,
              src: "/static/icons/yellow.png"
          }))
      });

      var markerStyleGreen = new ol.style.Style({
          image: new ol.style.Icon(({
              opacity: 1,
              scale: 0.6,
              src: "/static/icons/green.png"
          }))
      });

      var markerStyleDefault = new ol.style.Style({
          image: new ol.style.Icon(({
              opacity: 1,
              scale: 0.6,
              //src: "{% static '/icons/default.png' %}"
              src : "/static/icons/default.png"
          }))
      });

      var vectorLayerGreen = new ol.layer.Vector({
          source: markerSourceGreen,
          style: markerStyleGreen,
          minZoom: 14,
      });

      var vectorLayerYellow = new ol.layer.Vector({
          source: markerSourceYellow,
          style: markerStyleYellow,
          minZoom: 14,
      });

      var vectorLayerRed = new ol.layer.Vector({
          source: markerSourceRed,
          style: markerStyleRed,
          minZoom: 14,
      });

      var vectorLayerDefault = new ol.layer.Vector({
          source: markerSourceDefault,
          style: markerStyleDefault,
          minZoom: 14,
      });

      var map_layer = new ol.layer.Tile({
          source: new ol.source.OSM(),
      });

      var aojSource = new ol.source.Vector();
      var aoj_vector_layer = new ol.layer.Vector({
      });

      var map_view = new ol.View({
      center: ol.proj.fromLonLat([parseFloat(100.558621), parseFloat(13.852020)]),
      zoom: 5,
      });

      //Declare Map Object
      var map = new ol.Map({
      target: 'map',
      layers: [map_layer, vectorLayerGreen, vectorLayerYellow, vectorLayerRed, vectorLayerDefault, aoj_vector_layer],

      view: map_view,
      });  //End of map Object

      var element = document.getElementById('popup');
      var popup = new ol.Overlay({
          element: element,
          positioning: 'bottom-center',
          stopEvent: false,
          offset: [0, -10]
      });
    var point_to_plot;
    function zoom_to_polygon(geo_json){
          //console.log(JSON.parse(geo_json["data"]));
        let geojsonObject = JSON.parse(geo_json["data"]); // Parse AOJ Object to GeoJSON
        let centroid_aoj = geo_json["coordinate_cent"];
        point_to_plot = JSON.parse(geo_json["point"]);
          
          /* Function Below not complete */
        var features = new ol.format.GeoJSON().readFeatures(geojsonObject);
          //console.log(JSON.parse(point_to_plot[0])["coordinates"])

        features.forEach(function(feature){ feature.setId(undefined) });

        map.setView(new ol.View({
              center: ol.proj.fromLonLat([parseFloat(centroid_aoj[0]), parseFloat(centroid_aoj[1])]),
              zoom: 15, 
        }));
          
        let inx;

        //console.log(point_to_plot[0]);
        for(inx =0; inx < Object.keys(point_to_plot).length ; inx++){
              
            let peano_label = point_to_plot[inx]["peano"];
            let ratekva = point_to_plot[inx]["ratekva"];
            let feederid = point_to_plot[inx]["feederid"];
            let latitude = point_to_plot[inx]["coordinate"][0][1];
            let longitude = point_to_plot[inx]["coordinate"][0][0];

            if(point_to_plot[inx]["flag"] == false){

                  plotMarker(latitude, longitude, peano_label , "default");

            } else {
                let year_to_selected = document.getElementById("year_selector").value;
                let impact = point_to_plot[inx]["impact"].replace(/^\[|\]$/g, "").replace(/'/g,'').split(", ");
            
                console.log(impact)
                // let impact = tmp.split(",");
                // console.log(impact)
                plotMarker(latitude, longitude, peano_label ,impact[year_to_selected]);
                
            }
        }

    };
      
      function callback_aoj(){ //Function execute when change dropdown list office
          let aoj = document.getElementById("office_selector").value;
          console.log(aoj)
          if (aoj=="0806101"){ // Condition on AOJ Code 0806101 only
              // Create Request to get AOJ and Zoom to
              var url = "http://localhost:8000/aoj_select/";
              var method = "GET";
              var getData = "code="+JSON.stringify(aoj)
              var shouldBeAsync = true;
              var request = new XMLHttpRequest();
              request.onload = function () {
                  var status = request.status; // HTTP response status, e.g., 200 for "200 OK"
                  var data = request.responseText; // Returned data, e.g., an HTML document.
                  let data_out = JSON.parse(data)
                  //console.log(data_out) //data out is GeoJson
                  zoom_to_polygon(data_out);

              };
              request.open(method, url+"?"+getData, shouldBeAsync);
              request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
              request.send();

          }
      }; // End Function zoom to AOJ Centroid

      function query_peano(){ // Search PEANO from textbox ; Change to click on table view later.
          var peano = document.getElementById("peano");
          //console.log(peano.value)

          var url = "http://localhost:8000/show/";
          var method = "POST";
          var postData = "data="+peano.value;
          var shouldBeAsync = true;
          var request = new XMLHttpRequest();
          request.onload = function () {

              var status = request.status; // HTTP response status, e.g., 200 for "200 OK"
              var data = request.responseText; // Returned data, e.g., an HTML document.
              var data_json = JSON.parse(data);
              var output = data_json["data"][0];
  
              map_redraw(output);

          };
          request.open(method, url, shouldBeAsync);
          request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
          request.send(postData);
          
      };

      function map_redraw(output_ags){ // Redraw Map after get search result.
          console.log(output_ags)
          let coordinate = output_ags["coordinate"];
          let peano = output_ags["peano"];

          map.setView(new ol.View({ // Zoom to and set coordinate to Center of map.
              center: ol.proj.fromLonLat([parseFloat(coordinate[1]), parseFloat(coordinate[0])]),
              zoom: 15,
          }));
          
          extend = map.getView().calculateExtent();
          let box = ol.proj.transformExtent(extend,'EPSG:3857','EPSG:4326');
          filter_feat_req(box); // send Extend of Map

          plotMarker(coordinate[0], coordinate[1], peano, "green");

      };

      function filter_feat_req(box){ // Function Send bbox extend coordinate to Backend for query.
          // request to geoDjango to query point that fit in to bounding
          console.log(box)
          var url = "http://localhost:8000/query/";
          var method = "GET";
          var getData = "extend="+JSON.stringify(box)
          var shouldBeAsync = true;
          var request = new XMLHttpRequest();
          request.onload = function () {

              var status = request.status; // HTTP response status, e.g., 200 for "200 OK"
              var data = request.responseText; // Returned data, e.g., an HTML document.
              let data_out = JSON.parse(data)
              console.log(data_out)

          };
          request.open(method, url+"?"+getData, shouldBeAsync);
          request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
          request.send();
      
      };// End function

      map.addOverlay(popup);
      map.on('click', function(evt) {
      var feature = map.forEachFeatureAtPixel(evt.pixel,
          function(feature) {
              return feature;
          });
          if (feature) {
                      var coordinates = feature.getGeometry().getCoordinates();
                      popup.setPosition(coordinates);
                      $(element).popover({
                          placement: 'top',
                          html: true,
                          content: feature.get('pea')
                      });
                      $(element).popover('show');
          } else {
                      $(element).popover('dispose');
          }
      });
      
    function plotMarker(lat, lon, pea, color){ //Function for plot point feature in vector layer
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

          } else{
              markerSourceDefault.addFeature(iconFeature);
          }
      };

    function handleCallback(){ //Function Call from DropDown list to change year.
        let x = document.getElementById("year_selector").value;
        markerSourceGreen.clear()
        markerSourceYellow.clear()
        markerSourceRed.clear()

        for(inx =0; inx < Object.keys(point_to_plot).length ; inx++){
            if(point_to_plot[inx]["flag"] == true){
                let peano_label = point_to_plot[inx]["peano"];
                let ratekva = point_to_plot[inx]["ratekva"];
                let feederid = point_to_plot[inx]["feederid"];
                let latitude = point_to_plot[inx]["coordinate"][0][1];
                let longitude = point_to_plot[inx]["coordinate"][0][0];
                let impact = point_to_plot[inx]["impact"].replace(/^\[|\]$/g, "").replace(/'/g,'').split(", ");

                plotMarker(latitude, longitude, peano_label ,impact[x]);
            }
        }
        


      }; //End handleCallback Function


