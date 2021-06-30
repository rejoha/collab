import geoplotlib
data = geoplotlib.utils.read_csv('prepared_locations.csv')
geoplotlib.dot(data)
geoplotlib.show()

#v = df.values.tolist()
#c = df.columns.values.tolist()
#[dict(zip(c,x)) for x in v]
#data_dict = df.to_dict()
#print(data_dict)
#haltestelledata = pd.read_csv("haltestellen.csv") #haltestellen
#haltestelledata.head()
#test = haltestelledata.head()
#print(test)
#CHSTNAME




