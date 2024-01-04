
# import gmplot package
import gmplot
  
# from_geocode method return the
# latitude and longitude of given location .
gmap2 = gmplot.GoogleMapPlotter.from_geocode( "Dehradun, India" )
  
gmap2.draw( "F:\\Downloads\\m.html" )