from django.shortcuts import render,redirect,HttpResponse
import folium
from folium import plugins
from djangopostgis.models import Indstates, country,India,Indblocks
from django.core.serializers import serialize
import json
import os
from django.core.files.storage import FileSystemStorage
import shapefile
import geopandas as gpd
import pandas as pd
from .models import Indstates
from collections import OrderedDict
import csv




global geometry_coordinate, states_data
global dist_data, district_geometry_crs,state_data_id
# global varr
global geojson_data1,geojson_data2
# global dataDf
global data_data
# Create your views here.
def india(request):
    india_data =serialize('geojson',India.objects.all())
    print(india_data)
    m= folium.Map(location=(3, -0.219), zoom_start =2)
    
    folium.GeoJson(india_data).add_to(m)
    draw = plugins.Draw(export=True)
    draw.add_to(m)
    export_data =[]
    # shapesLayer = folium.FeatureGroup(name ='circle1').add_to(m)
    shapesLayer2 = folium.FeatureGroup(name ='marker').add_to(m)
    # powerPlantsLayer = folium.FeatureGroup(name = 'circle2').add_to(m)
    folium.Marker([20.022141, 76.267103],
    #change marker category
        icon =folium.Icon(icon="glyphicon-star")).add_to(shapesLayer2)
    folium.Marker([19.022141, 75.267103],
        icon =folium.Icon(icon="pencil", prefix='fa', color ='red')).add_to(shapesLayer2)
    folium.Marker([21.022141, 77.267103],
        icon =folium.Icon(icon="eye", prefix='fa',color='orange')).add_to(shapesLayer2)
    folium.LayerControl().add_to(m)
    m =m._repr_html_()
    return render(request, 'djangopostgis/home1.html', {'m':m, 'india_data':india_data})

def ind_states(request):

    ind_states =serialize('geojson',country.objects.all())
    print(ind_states)
    m= folium.Map(location=(3, -0.219), zoom_start =2)
    # folium.GeoJson(ind_states).add_to(m)
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
    return render(request, 'djangopostgis/home1.html', {'states':ind_states, 'm':m})

def ind_district(request):

    ind_district =serialize('geojson',Indstates.objects.all())
    m= folium.Map(location=(3, -0.219), zoom_start =2)
    folium.GeoJson(ind_district).add_to(m)
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
    return render(request, 'djangopostgis/home1.html', {'ind_district':ind_district, 'm':m})


def blocks(request):
    blocks_data =serialize('geojson',Indblocks.objects.all())

    m= folium.Map(location=(3, -0.219), zoom_start =2)
    folium.GeoJson(blocks_data).add_to(m)
    draw = plugins.Draw(export=True)
    draw.add_to(m)
    m =m._repr_html_()
    return render(request, 'djangopostgis/home1.html', {'m':m, 'blocks_data':blocks_data})
# def block_database(request,pk):

    
#     blockmodel =Indblocks(id_0=id_0,name_0=name_0,id_1=id_1,name_1=name_1,
#     id_2=id_2,name_2=name_2,id_3=id_3,name_3=name_3,type_3=type_3,engtype_3=engtype_3,
#     geom=geom)
#     return HttpResponse(request,"Data save successfully")
def map_name(request):
    state_name = request.POST.get("state_name")
    print(state_name)
    # state_name1 = request.POST.get('state_name1')
    # ind1 =states_data.index(state_name1)
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
    # print(data_1)
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
    return render(request, 'djangopostgis/home1.html', context)
# from django.db.models import Q
def country_states(request):
    global state_data_id
    global data_to_json
    # id_tuple = (3,4,5)
    # states =serialize('geojson',country.objects.filter(id__in=id_tuple))
    states =serialize('geojson',country.objects.all())
    # states =country.objects.all()
    
    states =json.loads(states)
    global states_data
    global dist_data
    states_data = []
    state_data_id = []
    dist_data = []
    dist_data_id1 = []
    dist_data_id2 = []
    global geometry_coordinate
    geometry_coordinate = []
    
    for x in states['features']:
       

        states_data.append(x['properties']['name_1'])
        state_data_id.append(x['properties']['id_1'])
        geometry_coordinate.append(x['geometry']['coordinates'])
   
    my_dict = {}

    

    for i in range(len(states_data)):
        
        my_dict[states_data[i]]=geometry_coordinate[i]
        # my_dict[states_data[i]]={
        #         "id_1":state_data_id[i],
        #         "geometry_coordinate":geometry_coordinate[i]
        #     }
    district =serialize('geojson',Indstates.objects.all())
    #################
    # name_1 ="Bihar"
    # getstates =country.objects.get(name1=name_1)
    # # name_1 = request.GET.get('country')
    # # name_1 = "Uttar Pradesh"
    # name2 = Indstates.objects.filter(name_1=getstates)
    # print(name2)
    ##################
    district =json.loads(district)
    global district_names
    global district_geometry_crs
    district_names =[]
    district_geometry_crs =[]
    for y in district['features']:
        dist_data.append(y['properties']['name_2'])
        # dist_data_id1.append(y['properties']['id_1'])
        # dist_data_id2.append(y['properties']['id_2'])

        district_geometry_crs.append(y['geometry']['coordinates'])
   

    dist_dict={}
    for i in range(len(states_data)):
        
        dist_dict[dist_data[i]]=district_geometry_crs[i]
    ######optinal######
    # sorted_keys =   dist_dict.items()
    # new_values =sorted(dist_dict.keys())
    #####optinal######
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
    ####### district format
    #     {
    #    "type":"FeatureCollection",
    #    "crs":{
    #       "type":"name",
    #       "properties":{
    #          "name":"EPSG:4326"
    #       }
    #    },
    #    "features":[
    #       {
    #          "type":"Feature",
    #          "properties":{
    #             "id_0":105,
    #             "iso":"IND",
    #             "name_0":"India",
    #             "id_1":1,
    #             "name_1":"Andaman and Nicobar",
    #             "id_2":1,
    #             "name_2":"Andaman Islands",
    #             "type_2":"District",
    #             "engtype_2":"District",
    #             "pk":"2"
    #          },
    #          "geometry":{
    #             "type":"MultiPolygon",
    #             "coordinates":[
    #                [
    #                   [
    #                      [
                            
    #                      ]
    #                   ]
    #                ]
    #             ]
    #          }
    #       }
    #    ]
    # objctdata = json.loads(temp)
    # print(objctdata)    
    # print(temp['features'])    


    # print(my_dict.keys())
    # final_data=json.dumps(my_dict)
    # return redirect(india_district)
    m= folium.Map(location=(3, -0.219), zoom_start =2)
    folium.GeoJson(my_dict).add_to(m)
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
    # return render(request, 'djangopostgis/success.html',{'m':m,'data':states})

def upload_shapefile(request):
    global file_directory,geojson_data1

    
   
    if request.method =='POST':
        uploaded_file =request.FILES['docfile']
        # print(os.path.realpath(os.path.join(os.path.dirname(__file__))))
        
        # if uploaded_file.name.endswith('.xlsx'):
        if uploaded_file.name.endswith('.shp'):
            #save thre file in medisa storage
            savefile = FileSystemStorage()
            d = os.getcwd()
            # f = os.path.abspath("mydir/myfile.shp")
            # this is the name of your csv file
            name = savefile.save(d+'/data2//'+uploaded_file.name, uploaded_file)
            # name = savefile.save(f+'/data2//'+uploaded_file.name, uploaded_file)
            # os.path.abspath(name)

           
            # print(d)
            file_directory =name
            print("###############")
            print(file_directory)
            print("###############")
            # myshpfile = gpd.read_file('file_directory')
            # myshpfile.to_file('myJson.geojson', driver='GeoJSON')

            geojson_data1 = readfile(file_directory)
            
            return redirect(show_onmap)
            # m= folium.Map(location=(3, -0.219), zoom_start =2)
            # folium.GeoJson(geojson_data1).add_to(m)
            # if(geojson_data1):
            #     return render(request,'djangopostgis/uload.html',{'m':m,'geojson_data1':geojson_data1})
            # else:
            #     return render(request,'djangopostgis/uload.html')
    return render(request,'djangopostgis/uload.html')
   
    # states1 = serialize('geojson', shape)
    # m= folium.Map(location=(3, -0.219), zoom_start =2)
def show_onmap(request):
    global geojson_data1,geojson_data2
    m= folium.Map(location=(3, -0.219), zoom_start =2)
    # myshpfile = gpd.read_file('file_directory')
    # myshpfile.to_file('myJson.geojson', driver='GeoJSON')
    # print(type(myshpfile))
    # folium.GeoJson(geojson_data1).add_to(m)
    folium.GeoJson(geojson_data2).add_to(m)

    draw = plugins.Draw(export=True)
    draw.add_to(m)
    m =m._repr_html_()
    context1= {
        # 'm':m
    }
    # return render(request,'djangopostgis/uload.html',{'m':m,'geojson_data1':geojson_data1})
    # return render(request,'djangopostgis/uload.html',{'m':m,'geojson_data2':geojson_data2})
    return render(request,'djangopostgis/home1.html',{'m':m,'geojson_data2':geojson_data2})
def readfile(filename):
    global geojson_data
    # li = []
    
    # reader = csv.DictReader(filename)
    # print("###################################")
    # print(reader)
    # print("###################################")
    # for row in reader:
    #     d = OrderedDict()
    #     d['type'] = 'Feature'
    #     d['geometry'] = {
    #         'type': 'Point',
    #         'coordinates': [float(row['latitude']), float(row['longitude'])]
    #     }
    #     li.append(d)

    # d = OrderedDict()
    # d['type'] = 'FeatureCollection'
    # d['features'] = li

    # with open('output.json','w') as f:
    #     json.dump(d,f,indent=2)
    #     print(d)
    # global dataDf
    # # my_file =pd.read_excel(filename)
    # my_file =pd.read_csv(filename)
    # dataDf =pd.DataFrame(data=my_file, index=None)
    # print(dataDf)
    # global geojson_data

    geojson_data = shapefile.Reader(filename).__geo_interface__
    return geojson_data
    # #  global varr
    #  myshpfile = gpd.read_file(filename)
    #  myshpfile.to_file('myJson.geojson', driver='GeoJSON')
    # print(geojson_data)

    # #  geojson_data = shapefile.Reader(filename).__geo_interface__
    # print(type(geojson_data))

    # shapefile = gpd.read_file(filename)
    # print(shapefile)
#     shape = shapefile.Reader(filename)
# #first feature of the shapefile
#     feature = shape.shapeRecords()[0]
#     first = feature.shape.__geo_interface__  
#     print(first)

def india_district(request):
    district =serialize('geojson',Indstates.objects.all())
    # name_1 ="Bihar"
    # getstates =country.objects.get(name=name_1)
    # name_1 = request.GET.get('country')
    # name_1 = "Uttar Pradesh"
    # name2 = Indstates.objects.filter(name_1=getstates)
    # print(name2)
    district =json.loads(district)
    global district_names
    global district_geometry_crs
    district_names =[]
    district_geometry_crs =[]
    for x in district['features']:
        district_names.append(x['properties']['name_2'])
        district_geometry_crs.append(x['geometry']['coordinates'])
    # print(district_names)
    # count total number of items in list or tuple or dic or array
    # print(len(district_names))
    dist_dict ={}
    for i in range(len(district_names)):
        dist_dict[district_names[i]] = district_geometry_crs[i]

    sorted_keys =   dist_dict.items()
    new_values =sorted(dist_dict.keys())
    
    # print(new_values)
    m= folium.Map(location=(3, -0.219), zoom_start =2)
    folium.GeoJson(dist_dict).add_to(m)
    draw = plugins.Draw(export=True)
    draw.add_to(m)
    m =m._repr_html_()
    # return render(request,'djangopostgis/distric.html',{'m':m, 'district_data':new_values})
    return render(request,'djangopostgis/inddistrict.html',{'m':m, 'dist_dict':new_values})
   
def map2_name(request):
    global dist_data
    district_name = request.POST.get('district_name')
    # print(state_name)
    ind = district_names.index(district_name)
  
    data_2  ={
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
            "id_0":105,
            "iso":"IND",
            "name_0":"India",
            "id_1":1,
            "name_1":"Andaman and Nicobar",
            "id_2":1,
            "name_2":district_name,
            "type_2":"District",
            "engtype_2":"District",
            "pk":"2"
         },
         "geometry":{
            "type":"MultiPolygon",
            "coordinates":district_geometry_crs[ind]
               
         }
      }
   ]
}
    
    # {
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
    #                 "name_2":district_name,
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
    #                 "coordinates":district_geometry_crs[ind]
    #             }
    #         }
    #     ]
    #     }
    m= folium.Map(location=(3, -0.219), zoom_start =2)
   
    draw = plugins.Draw(export=True)
    draw.add_to(m)
    # folium.Marker(
    # [21.493963918393746, 81.51855520970668]).add_to(m)
    folium.GeoJson(data_2).add_to(m)
    # folium.GeoJson(data_to_json).add_to(m)
  
    m =m._repr_html_()
    context= {
        'm':m
    }
    return render(request, 'djangopostgis/final2_map.html', context)
def ind_blocks(request):
     blocks =serialize('geojson',Indblocks.objects.all())
     blocks =json.loads(blocks)
     global blocks_name,blocks_geometry_crs
     blocks_name=[]
     blocks_geometry_crs=[]
     for z in blocks['features']:
        blocks_name.append(z['properties']['name_3'])
        blocks_geometry_crs.append(z['geometry']['coordinates'])
     block_dict={}
     for i in range(len(blocks_name)):
        block_dict[blocks_name[i]] = blocks_geometry_crs[i]
     sorted_keys =   block_dict.items()
     new_values =sorted(block_dict.keys())
    
    # print(new_values)
     m= folium.Map(location=(3, -0.219), zoom_start =2)
     folium.GeoJson(block_dict).add_to(m)
     draw = plugins.Draw(export=True)
     draw.add_to(m)
     m =m._repr_html_()
    # return render(request,'djangopostgis/distric.html',{'m':m, 'district_data':new_values})
     return render(request,'djangopostgis/indblock.html',{'m':m, 'block_dict':new_values})
    
def map3_name(request):
    global blocks_name
    block_name = request.POST.get('block_name')
    # print(state_name)
    ind = blocks_name.index(block_name)


    data_3= {
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
            "id_0":105,
            "iso":"IND",
            "name_0":"India",
            "id_1":1,
            "name_1":"Andaman and Nicobar",
            "id_2":1,
            "name_2":"Andaman Islands",
            "id_3":1,
            "name_3":block_name,
            "type_3":"Taluk",
            "engtype_3":"Taluk",
            "pk":"1"
         },
         "geometry":{
            "type":"MultiPolygon",
            "coordinates":blocks_geometry_crs[ind]
         }
      }
   ]
}

    m= folium.Map(location=(3, -0.219), zoom_start =2)
   
    draw = plugins.Draw(export=True)
    draw.add_to(m)
    # folium.Marker(
    # [21.493963918393746, 81.51855520970668]).add_to(m)
    folium.GeoJson(data_3).add_to(m)
    # folium.GeoJson(data_to_json).add_to(m)
  
    m =m._repr_html_()
    context= {
        'm':m
    }
    return render(request, 'djangopostgis/final3_map.html', context)
   

    


#     {
#    "type":"FeatureCollection",
#    "crs":{
#       "type":"name",
#       "properties":{
#          "name":"EPSG:4326"
#       }
#    },
#    "features":[
#       {
#          "type":"Feature",
#          "properties":{
#             "id_0":105,
#             "iso":"IND",
#             "name_0":"India",
#             "id_1":1,
#             "name_1":"Andaman and Nicobar",
#             "id_2":1,
#             "name_2":"Andaman Islands",
#             "type_2":"District",
#             "engtype_2":"District",
#             "pk":"2"
#          },
#          "geometry":{
#             "type":"MultiPolygon",
#             "coordinates":[
#                [
#                   [
#                      [
                        
#                      ]
#                   ]
#                ]
#             ]
#          }
#       }
#    ]
# }

# def csv_to_geojson(request):
#     li = []
#     with open('static/djangopostgis/file/area1.csv') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             d = OrderedDict()
#             d['type'] = 'Feature'
#             d['geometry'] = {
#                 'type': 'Point',
#                 'coordinates': [float(row['lat']), float(row['long'])]
#             }
#             li.append(d)

#     d = OrderedDict()
#     d['type'] = 'FeatureCollection'
#     d['features'] = li

#     with open('output.json','w') as f:
#         json.dump(d,f,indent=2)
#         print(d)
def uploadshp(request):
    global geojson_data2
    if request.method=="POST":
        myfile =request.FILES.getlist('uploadfiles')
        print("###########")
        print(type(myfile))
        print("###########")
        # savefile = FileSystemStorage()
        # d = os.getcwd()
        # name=[]
        # name = savefile.save(d+'/data2//'+myfile.name, myfile)
        # print(name)
        savefile = FileSystemStorage()
        for f in myfile:
            # list(myfile[0].items())
           
            d = os.getcwd()
        
            name = savefile.save(d+'/data2//'+f.name, f)
            file_directory =name
            # print("###############")
            # print(file_directory)
            # print("###############")
            # myshpfile = gpd.read_file('file_directory')
            # myshpfile.to_file('myJson.geojson', driver='GeoJSON')

        geojson_data2 = readfile(file_directory)
            
        return redirect(show_onmap)
            # print(f)
    return render(request,'djangopostgis/uload.html')
#####upload csv file #########
def upload_csv(request):
    context={}
    global list_of_column, data_data
    # m = folium.Map(location=[3, -0.219], zoom_start=2)
   
    if request.method =='POST':
        uploaded_file =request.FILES['docfile']
        # if uploaded_file.name.endswith('.xlsx'):
        if uploaded_file.name.endswith('.csv'):
            #save thre file in medisa storage
            savefile = FileSystemStorage()
            d = os.getcwd()
            # this is the name of your csv file
            name = savefile.save(d+'/media//'+uploaded_file.name, uploaded_file)

           
            # print(d)
            file_directory1 =   name
            print(file_directory1)
        data_data =readfile2(file_directory1)
            
        print("#########")
        print(data_data)
        print("#########")
        return redirect(data_view_onmap2)
            # return redirect(service)
        # if(dataDf):
        #     return redirect(data_view_onmap)
        # else:
        #     print("Please upload first file after that you can procced next form...")    
                
            # return redirect(data_view_onmap)


                

            

            #  return redirect(data_view_onmap)
            
            
    # m= m._repr_html_()

    # context ={
    #     'm': m,
        
    # }

    return render(request, 'djangopostgis/csvfile.html')
    
def readfile2(filename):
    global dataDf
    # my_file =pd.read_excel(filename)
    my_file =pd.read_csv(filename)
    dataDf =pd.DataFrame(data=my_file, index=None)
    return dataDf
    # print(dataDf)
#     list_of_column_names = list(dataDf.columns)
 
# # displaying the list of column names
#     print('List of column names : ',
#       list_of_column_names)
   

def data_view_onmap2(request):
    # global dataDf
    global data_data
    # global list_of_column
   
    m = folium.Map(location=[3, -0.219], zoom_start=2)
        
    powerPlantsLayer = folium.FeatureGroup(name = 'circle2').add_to(m)
    # if(list_of_column is True):
    
    for i in range(len(data_data)):
            areaStr = data_data.iloc[i]['area']
            fuelStr = data_data.iloc[i]['fuel']
            capVal = data_data.iloc[i]['capacity']
            # derive the circle color
            clr = "blue" if fuelStr.lower() == 'wind' else "red"
            # derive the circle radius
            radius = capVal*10
            # derive the circle pop up html content 
            popUpStr = 'Patient - {0}<br>Type - {1}<br> - {2} TB'.format(
                areaStr, fuelStr, capVal)
            folium.Circle(
                location=[data_data.iloc[i]['lat'], data_data.iloc[i]['lng']],
                popup=folium.Popup(popUpStr, min_width=100, max_width=700),
                radius=radius,
                color=clr,
                weight=2,
                fill=True,
                fill_color=clr,
                fill_opacity=0.1
            ).add_to(powerPlantsLayer)
    legendHtml = '''
            <div style="position: fixed; 
            bottom: 50px; left: 50px; width: 150px; height: 70px; 
            border:2px solid grey; z-index:9999; font-size:14px;
            ">&nbsp; Fuel Types <br>
            &nbsp; <i class="fa fa-circle"
                        style="color:blue"></i> &nbsp; Wind<br>
            &nbsp; <i class="fa fa-circle"
                        style="color:red"></i> &nbsp; Solar<br>
            </div>
            '''

    # inject html corresponding to the legend into the map
    m.get_root().html.add_child(folium.Element(legendHtml))
    #     list_of_column_names = list(dataDf.columns)
    # # displaying the list of column names
    #     print('List of column names : ',
    #       list_of_column_names)
    
    m= m._repr_html_()

    context ={
        #    'list_of_column': list_of_column_names,
            'm': m,
        }
        
    return render(request, 'djangopostgis/home1.html', context)


# def service(request):
#      global dataDf
#      m = folium.Map(location=[3, -0.219], zoom_start=2)
#      context={}
#      list_of_column_names = list(dataDf.columns)
# # displaying the list of column names
#      print('List of column names : ',
#      list_of_column_names)
#      m= m._repr_html_()

#      context ={
#          'list_of_column': list_of_column_names,
#         'm': m,
#     }
#      return render(request, 'djangopostgis/csvfile.html', context)
   