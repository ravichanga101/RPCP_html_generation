import os,json

path_to_json = 'json/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

display_card_str = ''
# Read all json files 
for json_file in json_files:
  with open('json/'+json_file) as f:
    data = json.load(f)
    content = data.values()
    
    title = list(content)[0]
    url = list(content)[1].split()[0]
    

    display_card_str += '<div class="card d-inline-block m-1 " style="width: 18rem;"><div class="card-body"><h5 class="card-title">'+title+'</h5><a href="'+url+'.html" class="btn btn-primary" >Get Details</a></div></div>'

print(display_card_str)

