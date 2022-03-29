import requests
# from urllib.parse import unquote
import json
import datetime
import re
# from flask import jsonify
# from html_scraper import scrapeWebpage


def magicId (content):
    from magic_lib import Magic
    m = Magic()
    return m.from_buffer(content)

def whatTheFile (uri):
    # uri = unquote(str(uri))
    uri = "https://arweave.net/" + uri
    data = requests.get(uri)
    # dtext = data.text
    # print(dtext)
    return magicId(data.content)




def runArweaveAPI():
    with open('height.txt', 'r') as f:
        last_block = f.readlines()[-1]


    url = 'https://arweave.net/graphql'

    height = int(last_block)+1
    query = """query {
        transactions(block: {min: """+str(height)+""", max: """+str(height)+"""}) {
            edges {
                node {
                    id,
                    data {
                        size
                        type
                    },
                    tags {
                        name,
                        value
                    },
                    block {
                        id
                        timestamp
                        height
                        previous
                    }
                }
            }
        }
    }"""
    response = requests.post(url, json={'query': query})
    json_data = json.loads(str(response.text))["data"]["transactions"]["edges"]

    arweave_api_data = []
    for i in json_data:
        tx_id = i["node"]["id"]
        timestamp = i["node"]["block"]["timestamp"]
        filetype = whatTheFile(tx_id)

        data = {"file_type": filetype,
                "data_type": i["node"]["data"]["type"],
                "data_size": i["node"]["data"]["size"],
                "block_height": i["node"]["block"]["height"],
                "timestamp": str(datetime.datetime.fromtimestamp(timestamp)),
                "tx_id": tx_id}

        # if "HTML" in str(filetype):
            # try:
            # webscrape = scrapeWebpage(tx_id)
            # try: data["language"] = webscrape["language"]
            # except: pass
            # print("-----------------------------------------------------------------------------")
            # print('length of data["entities"] = ' + str(webscrape["entities"]))
            # print('data["entities"][0] = ' + str(webscrape["entities"][0]))
            # data["entities"] = str([dict({"entity_type":webscrape["entities"][i][1], "entity_name":webscrape["entities"][i][0]}) for i in list(webscrape["entities"])])
            # except: pass
            # try: data["top_words"] = webscrape["top_words"]
            # except: pass
            # except:
            #     pass
        for tag in i["node"]["tags"]:
            data[tag["name"]] = tag["value"]

        arweave_api_data.append(data)

    with open('height.txt', 'a') as f:
        f.write("\n"+str(height))

    return [dict(i) for i in arweave_api_data]


# print(runArweaveAPI())