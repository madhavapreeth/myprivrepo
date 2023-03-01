import requests
import json

def num_files_directories(url):
    token = "dapi7d6ef2e78b210214bc96a48bd61cd0c3-3"
    token_acces = {"Authorization": "Bearer " + token}

    directory = '/FileStore/'
    params = {'path': directory}
    response = requests.get(url, headers=token_acces, params=params)
    data = json.loads(response.text)

    folders = 0
    for i in data['files']:

        files=0
        dire=i['path']
        if i['is_dir']==True:
            print(f"{dire[len(directory):]}: It is a directory")
            folders+=1
            dire2=directory+dire[len(directory):]
            params = {'path': dire2}
            response = requests.get(url, headers=token_acces, params=params)
            data = json.loads(response.text)
            c=0
            try:
                for i in data['files']:
                    c=c+1
            except:
                c=0
            print(f"The number of files in : {dire[len(directory):]}: {c} ")
    print(f"Total Num of folders:{folders}")

url='https://adb-8533386130191487.7.azuredatabricks.net/api/2.0/dbfs/list'
num_files_directories(url)


output:
----------
my_folder: It is a directory

The number of files in : my_folder: 5
 
my_folder2: It is a directory

The number of files in : my_folder2: 0 

tables: It is a directory

The number of files in : tables: 1 

Total Num of folders:3




def deleting_files():

    token = "dapi7d6ef2e78b210214bc96a48bd61cd0c3-3"
    token_acces = {"Authorization": "Bearer "+token}
    url = "https://adb-8533386130191487.7.azuredatabricks.net/api/2.0/dbfs/list"
    directory='/FileStore/my_folder/'
    params={'path': directory}

    response = requests.get(url, headers=token_acces, params=params)
    data = json.loads(response.text)

    characters = input("Enter starting characters of file to remove: ")
    for i in data['files']:

            if i['path'][len(directory):][0:len(characters)]==characters:
                res=i['path']

                data2 = {
                    'path': res
                }
                print(f"The Actual Path Of File: {data2['path']}")

                url2 = "https://adb-8533386130191487.7.azuredatabricks.net/api/2.0/dbfs/delete"
                result = requests.post(url=url2, headers=token_acces, data=json.dumps(data2))
                if result.status_code==200:
                    print("File Deleted Successfully...")

deleting_files()

output:
----------
Enter starting characters of file to remove: example

The Actual Path Of File: /FileStore/my_folder/example.csv

File Deleted Successfully...

Enter starting characters of file to remove: hello.txt

The Actual Path Of File: /FileStore/my_folder/hello.txt

File Deleted Successfully...
