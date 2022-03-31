import requests
import json
import datetime
from html_scraper import scrape_url


def magicId (content):
    if content is not None:
        from magic_lib import Magic
        m = Magic()
        return m.from_buffer(content)
    else: pass

def whatTheFile (uri):
    if uri is not None:
        uri = "https://arweave.net/" + uri
        data = requests.get(uri)
        return magicId(data.content)
    else: pass

# def testWebscrape(tx_number):
#         webscrape = WebScraper(tx_number)
#         webscrape = webscrape.run()
        # data["named_entities"] = str(webscrape["named_entities"])
        # data["source_language"] = webscrape["source_language"]
        # data["source_text"] = webscrape["source_text"]
        # data["english_text"] = webscrape["english_text"]

# x = testWebscrape("IWdMfjLQo2mFlQ3ZBBVGwAghRI419mEw-HxufRIwF2g")
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
    print("arweave_api response received {}".format(str(response.status_code)))
    json_data = json.loads(str(response.text))["data"]["transactions"]["edges"]
    arweave_api_data = []
    for i in json_data:
        # print("working through each tx: {} of {}".format(i, str(len(json_data))))
        tx_id = i["node"]["id"]
        timestamp = i["node"]["block"]["timestamp"]
        filetype = whatTheFile(tx_id)

        data = {"timestamp": str(datetime.datetime.fromtimestamp(timestamp)),
                "tx_id": str(tx_id),
                "block_height": str(i["node"]["block"]["height"]),
                "file_type": str(filetype),
                "data_type": str(i["node"]["data"]["type"]),
                "data_size": str(i["node"]["data"]["size"])
                }
        for tag in i["node"]["tags"]:
            if "_" in str(tag["name"]):
                name = str(tag["name"]).replace(":","_")
            else:
                name = tag["name"]
            data[tag["name"]] = str(tag["value"])

        # # try:
        if "text" in str(filetype):
            webscrape = scrape_url(tx_id)
            # data["named_entities"] = str(webscrape["named_entities"])
            # data["source_language"] = webscrape["source_language"]
            # data["source_text"] = webscrape["source_text"]
            data["source_text"] = webscrape["source_text"]
            # # except:
            # #     pass
            print("done with webscrape stuff")
        arweave_api_data.append(data)
    print("about to open height.txt to write new height")
    with open('height.txt', 'a') as f:
        f.write("\n"+str(height))
    print("about to return arweave_api_data")
    # return json.dumps(arweave_api_data, indent=4)
    return arweave_api_data

# if __name__ == '__main__':
#     runArweaveAPI()


# print(runArweaveAPI())
