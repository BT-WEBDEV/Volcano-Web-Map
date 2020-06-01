#folium - lets us generate a map within python
#pandas - lets us read the csv file containing volcano locations. 
import folium
import pandas

#dataframe variable will let us read the txt file. 
df=pandas.read_csv("Volcanoes.txt") 

#map variable - this creates our map object.
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=4,tiles='Stamen Terrain')

#function color(elev) - determines color of map marker based on elevation
def color(elev): 

    #variable minimum to pull in the lowest elevation level
    minimum=int(min(df['ELEV']))

    #variable step is max elevation value minus the minmum elevation value
    #then divided by 3 - for the 3 different elevation levels
    step=int((max(df['ELEV'])-min(df['ELEV']))/3)

    if elev in range(minimum,minimum+step):
        col='green'
    elif elev in range(minimum+step,minimum+step*2):
        col='orange'
    else: 
        col='red'
    return col

#fg variable is the feature group - this will let us enable volcano locations on the layer control panel. 
fg=folium.FeatureGroup(name="Volcano Locations")

#for loop to generate through the latitude, longitude, and name of each volcano.
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    
    #this creates our markers on the map for each volcano location. 
    folium.Marker([lat,lon],popup=name,icon=folium.Icon(color=color(elev))).add_to(fg)

#this adds the feature group to the map
map.add_child(fg)

#this adds the layer control panel to the map. 
map.add_child(folium.LayerControl())

#this generates the map into an html file. 
map.save(outfile='test.html')
  