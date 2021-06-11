import wikipedia  
  
# wikipedia page object is created  
object = wikipedia.page("America")  
  
# printing html of page_object  
print(object.html)  
  
# printing title  
print(object.original_title)  
  
# printing links on that page object  
print(object.links[0:20])  