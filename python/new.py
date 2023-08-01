#creat google map projet
def google_map_project(**info):
    print("my country budget", info["budget"] )
    print("my stuff bdget", info["staff"])
    print("MY Project name", info["projectName"])

google_map_project(projectName="google_map", stratDate="Dec2020", budget="1 million", staff= "1000", country="USA" )