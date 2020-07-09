# Map Creator Defaults
column_check = 'address', 'city', 'state', 'longitude', 'latitude'
default_icons = ('explore', 'done', 'privacy_tip', 'turned_in', 'sentiment_satisfied_alt')
default_colors = ('purple', 'red', 'gray', 'orange', 'blue',
                  'green', 'black')

# Status messages
process_stopped = 'Stopped and saved progress in cache'
time_out_title = 'Connection timed out'
time_out_message = 'The connection to the geo location service' \
                   'was terminated. The progress was saved in cache'
generating_geo = 'Converting address to geo location...'
using_geo = 'Mapping from available geo locations.'

# Main window settings
ttk_theme = 'breeze'
window_icon = 'images/icon.ico'
main_window_title = 'Python Map Creator'
main_win_width = 750
main_win_height = 520

# Map window settings
map_window_title = 'Map Styler'
map_win_width = 400
map_win_height = 440

# Images
left_banner = 'images/mapsnip.jpg'
color_picker_image = "images/dropper.png"

# Error messages
data_set_error = 'This Data Set does not contain the required data.\n\n' \
                 'Please make sure your file contains ' \
                 'Address, City, State columns\n' \
                 'or Longitude and Latitude columns.'
data_set_error_title = 'Data Set Error'
file_error = 'You have not selected a file to process. Please select a file.'
file_error_title = 'Select a File'
layer_empty_error = 'You have not entered a name for the layer.' \
                    ' Please enter a layer name.'
layer_empty_title = 'Layer Name'
existing_layer_error = "Another layer already exists with this layer name" \
                       "Please enter a new name for the current layer"
existing_layer_title = "Existing Layer Name"

# Input messages
default_values_message = 'Empty fields will be set to default values. Do you want to continue?'
default_values_title = 'Default Values'
edit_continue_message = 'You have not saved your current Layer. Do you want to ' \
                        'disregard the changes?'
create_map_continue_m = 'You have not saved your current Layer. Do you want to ' \
                        'continue and create the map?'
incomplete_layer_title = 'Incomplete Layer'

# Info messages
icon_style_info = 'Please choose an icon from the website, and\n' \
                  'enter the name. You can also leave the entry field\n' \
                  'empty to select a random one.'
icon_info_title = "Choose an Icon"
about_link = 'https://www.crisfilio.com/projects/pymaps'
about_message = 'Thank you for using the program.\n' \
                'For information about the project and the code \n' \
                'please refer to the project web page.'
about_title = "About Pymaps"
info_message = 'Welcome to Pymaps.\n\n' \
               'With this program you can plot coordinates into a map \n' \
               'using any number of data sets containing addresses or \n' \
               'geo locations.\n\n' \
               'Each data set will be plotted into its own layer which \n' \
               'you can turn on and off on the live map.\n\n' \
               'You can also add custom labels and markers to the map\n' \
               'and edit the map layers at any point of your progress.\n\n' \
               'A selection of fifteen different map tile styles are \n' \
               'also available for you to use.\n\n' \
               'In order to generate the geo locations an internet \n' \
               'connection is needed.\n\n' \
               'Start by opening a csv, json, or excel file.'
info_title = 'How to use this program'

# Defaults
label_default = 'Use Location as Label'
map_style_default = 'Open Street Map Mapnik'
icon_style_link = 'https://material.io/resources/icons/?icon=account_balance&style=baseline'

map_style_dict = {'Default': 'images/maps/OSMMappink.jpg',
                  'Open Street Map Mapnik': 'images/maps/OSMMappink.jpg',
                  'Jawg Matrix': 'images/maps/JawgMatrix.jpg',
                  'Thunderforest Spinal Map': 'images/maps/ThunderSpinal.jpg',
                  'Open Street Map DE': 'images/maps/OSMDE.jpg',
                  'Open Street Map France': 'images/maps/OSMFR.jpg',
                  'Open Street Map HOT': 'images/maps/OSMHot.jpg',
                  'Open Topo Map': 'images/maps/OSMTopo.jpg',
                  'Stadia Alidade Smooth': 'images/maps/StadiaAlide.jpg',
                  'Stadia Alidade Smooth Dark': 'images/maps/StadiaAlideD.jpg',
                  'Thunderforest Open CycleMap': 'images/maps/ThunderOCM.jpg',
                  'Thunderforest Transport': 'images/maps/ThunderTrans.jpg',
                  'Thunderforest Transport Dark': 'images/maps/ThunderTransD.jpg',
                  'Thunderforest Pioneer': 'images/maps/ThunderPioneer.jpg',
                  'Thunderforest MobileAtlas': 'images/maps/ThunderAtlas.jpg',
                  'Esri World Imagery': 'images/maps/ErisWorld.jpg'
                  }


def tile_styler(style):
    if style == 'Open Street Map Mapnik':
        tiles = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
        attr = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

    if style == 'Open Street Map DE':
        tiles = 'https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png'
        attr = '& copy; < a href="https://www.openstreetmap.org/copyright" > OpenStreetMap < / a > contributors'

    if style == 'Open Street Map France':
        tiles = 'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png'
        attr = '&copy; Openstreetmap France | &copy; <a ' \
               'href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors '

    if style == 'Open Street Map HOT':
        tiles = 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png'
        attr = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style ' \
               'by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a ' \
               'href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a> '

    if style == 'Open Topo Map':
        tiles = 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png'
        attr = 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' \
               '<a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a ' \
               'href="https://opentopomap.org">OpenTopoMap</a> (<a ' \
               'href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>) '

    if style == 'Stadia Alidade Smooth':
        tiles = 'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png'
        attr = '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a ' \
               'href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a ' \
               'href="http://openstreetmap.org">OpenStreetMap</a> contributors '

    if style == 'Stadia Alidade Smooth Dark':
        tiles = 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'
        attr = '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a ' \
               'href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a ' \
               'href="http://openstreetmap.org">OpenStreetMap</a> contributors '

    if style == 'Thunderforest Open CycleMap':
        tiles = 'https://{s}.tile.thunderforest.com/cycle/{z}/{x}/{y}.png?apikey=02259430e6b04e76b6c6b982e6e8e71b'
        attr = '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a ' \
               'href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors '

    if style == 'Thunderforest Transport':
        tiles = 'https://{s}.tile.thunderforest.com/transport/{z}/{x}/{y}.png?apikey=02259430e6b04e76b6c6b982e6e8e71b'
        attr = '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a ' \
               'href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors '

    if style == 'Thunderforest Transport Dark':
        tiles = 'https://{s}.tile.thunderforest.com/transport-dark/{z}/{x}/{' \
                'y}.png?apikey=02259430e6b04e76b6c6b982e6e8e71b'
        attr = '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a ' \
               'href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors '

    if style == 'Thunderforest Spinal Map':
        tiles = 'https://{s}.tile.thunderforest.com/spinal-map/{z}/{x}/{y}.png?apikey=02259430e6b04e76b6c6b982e6e8e71b'
        attr = '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a ' \
               'href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors '

    if style == 'Thunderforest Pioneer':
        tiles = 'https://{s}.tile.thunderforest.com/pioneer/{z}/{x}/{y}.png?apikey=02259430e6b04e76b6c6b982e6e8e71b'
        attr = '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a ' \
               'href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors '

    if style == 'Thunderforest MobileAtlas':
        tiles = 'https://{s}.tile.thunderforest.com/mobile-atlas/{z}/{x}/{' \
                'y}.png?apikey=02259430e6b04e76b6c6b982e6e8e71b'
        attr = '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a ' \
               'href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors '

    if style == 'Jawg Matrix':
        tiles = 'https://{s}.tile.jawg.io/jawg-matrix/{z}/{x}/{y}{' \
                'r}.png?access-token=Skaxv5rNPOUYjksrB9l3j2UmNhrgPIJDGbPu3neUo7ZtACvU520hIrddfu335FJc'
        attr = '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; ' \
               '<b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> ' \
               'contributors '

    if style == 'Esri World Imagery':
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
        attr = 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, ' \
               'IGP, UPR-EGP, and the GIS User Community '

    return tiles, attr


js_code = """
/**
 * Lefalet.IconMaterial uses code from
 * 1- Leaflet.AwesomeMarkers (c) 2012-2013, Lennard Voogdt <https://github.com/lvoogdt>
 * 2- and Wesley Van De Voorde's SVG magic <https://github.com/wesleyvandevoorde>
 * to create fully colorable SVG markers with Material icons in them.
 *
 * Author: Ilya Ilyankou <https://github.com/ilyankou>
 * License: MIT
 * Version: 1.0
*/

/*global L*/

(function (window, document, undefined) {
    "use strict";

    L.IconMaterial = {};

    L.IconMaterial.version = '1.0.0';

    L.IconMaterial.Icon = L.Icon.extend({
        options: {
            className: 'l-icon-material',
            icon: 'radio_button_checked',
            markerColor: 'white',
            iconColor: 'white',
            outlineColor: 'white',
            outlineWidth: '1',
        },

        initialize: function (options) {
            options = L.Util.setOptions(this, options);
        },

        createIcon: function () {
            var options = L.Util.setOptions(this);
            var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
            var path = document.createElementNS('http://www.w3.org/2000/svg', "path");
            var backgroundCircle = document.createElementNS('http://www.w3.org/2000/svg', "circle");
            var icongroup = document.createElementNS('http://www.w3.org/2000/svg', "g");
            var icon = document.createElementNS('http://www.w3.org/2000/svg', "text");

            svg.setAttribute('width', '31');
            svg.setAttribute('height', '42');
            svg.setAttribute('class', 'l-icon-material');
            svg.setAttributeNS("http://www.w3.org/2000/xmlns/", "xmlns:xlink", "http://www.w3.org/1999/xlink");

            backgroundCircle.setAttribute('cx', '15.5');
            backgroundCircle.setAttribute('cy', '15');
            backgroundCircle.setAttribute('r', '11');
            backgroundCircle.setAttribute('fill', options.markerColor);

            path.setAttributeNS(null, "d", "M15.6,1c-7.7,0-14,6.3-14,14c0,10.5,14,26,14,26s14-15.5,14-26C29.6,7.3,23.3,1,15.6,1z");
            path.setAttribute('fill', options.markerColor);
            path.setAttribute('stroke', options.outlineColor);
            path.setAttribute('stroke-width', options.outlineWidth);

            icon.textContent = options.icon;
            icon.setAttribute('x', '7');
            icon.setAttribute('y', '23');
            icon.setAttribute('class', 'material-icons');
            icon.setAttribute('fill', options.iconColor);
            icon.setAttribute('font-family', 'Material Icons');

            svg.appendChild(path);
            svg.appendChild(backgroundCircle);
            icongroup.appendChild(icon);
            svg.appendChild(icongroup);

            return svg;
        }
    });

    L.IconMaterial.icon = function (options) {
        return new L.IconMaterial.Icon(options);
    };

}(this, document));"""

css_code = """
/**
 * Author: Ilya Ilyankou <https://github.com/ilyankou>
 * License: MIT
 * Version: 1.0
 */ 

.l-icon-material {
    margin-top: -42px;
    margin-left: -17px;
    position: absolute;
    left: 0;
    top: 0;
    display: block;
    text-align: center;
}

.l-icon-material .material-icons {
    font-size: 17px;
}
"""