''' 
Extract important metadata and grouping information from image file names in a specified directory
Use regex101.com (with PCRE2 flavour) to help create a regular expression (example below)
This function expects the syntax defining a capture group as follows: (?P<group_name>XXX)
'''
import os
import re
import pandas as pd

image_dir = "images/"
regex = "^r(?P<row>[0-9]{2})c(?P<column>[0-9]{2})f(?P<field>[0-9]{2})p(?P<stack>[0-9]{2})-ch(?P<channel>[0-9]{1}).tiff"

def get_meta_table(path, regex):
    groups = re.findall(r'\<.*?\>', regex)
  
    for chr in ["<", ">"]:
       groups = [i.replace(chr, "") for i in groups]
      
    image_list = os.listdir(path)  
    df = pd.DataFrame([], columns=groups)

    for image in image_list:
        df.loc[image]=re.search(regex, image).groups()
    return(df)

get_meta_table(image_dir, regex)
