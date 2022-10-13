from django.shortcuts import render,redirect
import folium
from folium import plugins
from djangopostgis.models import Indstates, country
from django.core.serializers import serialize
import json
import os
from django.core.files.storage import FileSystemStorage
import shapefile
import geopandas as gpd




global geometry_coordinate, states_data
# Create your views here.
def map_name(request):
    state_name = request.POST.get('state_name')
    # print(state_name)
    ind = states_data.index(state_name)
    # data_1 = {}
    # data_1['name'] = 'EPSG:4326'
    # state_name = geometry_coordinate[ind]
    # data_1['name'] = 'EPSG:4326'
    data_1 = {
        "type":"FeatureCollection",
        "crs":{
            "type":"name",
            "properties":{
                "name":"EPSG:4326"
            }
        },
        "features":[
            {
                "type":"Feature",
                "properties":{
                    "name_1":state_name,
                    "name_0":"India",
                    "id_0":105,
                    "iso":"IND",
                    "id_1":1,
                    "type_1":"Union Territor",
                    "engtype_1":"Union Territory",
                    "pk":"3"
                },
                "geometry":{
                    "type":"MultiPolygon",
                    "coordinates":geometry_coordinate[ind]
                }
            }
        ]
        }
    print(data_1)
    # json_data =json.dumps(data_1)
    # print(json_data)
    # print(type(json_data))
    # print(data_to_json.crs )
    # data_f =serialize('geojson', data_to_json)
    # print(type(data_to_json))
    # print(type( data_f ))
    
    m= folium.Map(location=(3, -0.219), zoom_start =2)
   
    draw = plugins.Draw(export=True)
    draw.add_to(m)
    # folium.Marker(
    # [21.493963918393746, 81.51855520970668]).add_to(m)
    folium.GeoJson(data_1).add_to(m)
    # folium.GeoJson(data_to_json).add_to(m)
  
    m =m._repr_html_()
    context= {
        'm':m
    }
    return render(request, 'djangopostgis/final_map.html', context)

def home(request):
    context ={}
    m= folium.Map(location=(3, -0.219), zoom_start =2)
    # folium.GeoJson(states).add_to(m)
    draw = plugins.Draw(export=True)
    draw.add_to(m)
    m =m._repr_html_()
    context= {
        'm':m
    }
    return render(request, 'djangopostgis/home.html', context)
# from django.db.models import Q
def country_states(request):
    global data_to_json
    # id_tuple = (3,4,5)
    # states =serialize('geojson',country.objects.filter(id__in=id_tuple))
    states =serialize('geojson',country.objects.all())
    states =json.loads(states)
    global states_data
    states_data = []
    global geometry_coordinate
    geometry_coordinate = []
    
    for x in states['features']:
        # print(x['properties']['name_1'])
        states_data.append(x['properties']['name_1'])
        geometry_coordinate.append(x['geometry']['coordinates'])
        
    print(states_data)
    # # print(geometry_coordinate)
    my_dict = {}
    for i in range(len(states_data)):
        # print(i)
        # temp = {states_data[i]: geometry_coordinate[i]}
        # if(i==0):
        my_dict[states_data[i]]=geometry_coordinate[i]

        # else:
        #     break    
        # my_dict[states_data[0]].append(geometry_coordinate[0])
    
    # all_data =[my_dict]
    # print(type())
    #var = (states['features'][0]['properties']['name_1'][0])
    # var = states['features']
    # print(type(var))
    # for x in var:
    # print(var)

    # geojson= states["type"]
    # for x in geojson:
    #     keys =x.keys()
    #     print(keys)
    # lyr =states[0]
    # temp = {
    #     "type":"FeatureCollection",
    #     "crs":{
    #         "type":"name",
    #         "properties":{
    #             "name":"EPSG:4326"
    #         }
    #     },
    #     "features":[
    #         {
    #             "type":"Feature",
    #             "properties":{
    #                 "name_1":"Andaman and Nicobar",
    #                 "name_0":"India",
    #                 "id_0":105,
    #                 "iso":"IND",
    #                 "id_1":1,
    #                 "type_1":"Union Territor",
    #                 "engtype_1":"Union Territory",
    #                 "pk":"3"
    #             },
    #             "geometry":{
    #                 "type":"MultiPolygon",
    #                 "coordinates":[]
    #             }
    #         }
    #     ]
    #     }
    # objctdata = json.loads(temp)
    # print(objctdata)    
    # print(temp['features'])    


    # print(my_dict.keys())
    # final_data=json.dumps(my_dict)
    m= folium.Map(location=(3, -0.219), zoom_start =2)
    folium.GeoJson(states).add_to(m)
    draw = plugins.Draw(export=True)
    draw.add_to(m)
    m =m._repr_html_()
    context1= {
        # 'm':m
    }
    # context2= {
    #     'lyr':lyr
    # }
    # print(states)
    # return render(request, 'djangopostgis/success.html', {'states':states,  'states_data': states_data, 'm':m})
    return render(request, 'djangopostgis/success.html',{'m':m,'data':my_dict})
    # return render(request, 'djangopostgis/success.html',{'m':my_dict})

def upload_shapefile(request):
     
   
    if request.method =='POST':
        uploaded_file =request.FILES['docfile']
        print(os.path.realpath(os.path.join(os.path.dirname(__file__))))
        
        # if uploaded_file.name.endswith('.xlsx'):
        if uploaded_file.name.endswith('.shp'):
            #save thre file in medisa storage
            savefile = FileSystemStorage()
            d = os.getcwd()
            # this is the name of your csv file
            file_directory = savefile.save(d+'/data2//'+uploaded_file.name, uploaded_file)

           
            # print(d)
            # file_directory =   name
            # print(file_directory)
            # readfile(file_directory)
            # return redirect(show_onmap(file_directory))
    # m= folium.Map(location=(3, -0.219), zoom_start =2)
    # m =m._repr_html_()
    # return render(request,'djangopostgis/uload.html',{'m':m})
    return render(request,'djangopostgis/uload.html')
            # readfile(file_directory)
            # return redirect(data_view_onmap)
            
def show_onmap(request, shape):
    # states1 = serialize('geojson', shape)
    m= folium.Map(location=(3, -0.219), zoom_start =2)
    # folium.GeoJson(states1).add_to(m)
    draw = plugins.Draw(export=True)
    draw.add_to(m)
    m =m._repr_html_()
    context1= {
        # 'm':m
    }
    return render(request,'djangopostgis/uload.html',{'m':m})
def readfile(filename):

    # shapefile = gpd.read_file(filename)
    # print(shapefile)
    shape = shapefile.Reader(filename)
#first feature of the shapefile
    feature = shape.shapeRecords()[0]
    first = feature.shape.__geo_interface__  
    print(first)

def india_district(request):
    district =serialize('geojson',Indstates.objects.all())
    m= folium.Map(location=(3, -0.219), zoom_start =2)
    folium.GeoJson(district).add_to(m)
    draw = plugins.Draw(export=True)
    draw.add_to(m)
    m =m._repr_html_()
    return render(request,'djangopostgis/distric.html',{'m':m})

