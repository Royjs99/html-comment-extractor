import requests
import argparse

#colors
def prRed(s): print("\033[91m {}\033[00m".format(s))
def prYellow(s): print("\033[93m {}\033[00m".format(s))

def extract_comments(text):
    position = 0
    for comment in text:
        total_string = str()
        if comment[:4] == "<!--":
            comment_position = position
            while comment_position != len(text)-1:
                total_string = total_string + text[comment_position]+" "
                if text[comment_position][:4] == "-->":
                    print(total_string)
                    position=comment_position
                    break

                comment_position+=1
        position+=1

    print("")

def page_request(url,dictionary):
    try:
        with open(dictionary,"r") as files:
            for file in files:
                try:
                    file = file.strip()
                    if file[0] == "/":
                        file = file.replace("/","")
                    url_compose = url+file
                    prYellow(f"Revisando comentarios de la dirección {url_compose}")
                    response = requests.get(url_compose)
                    if response.status_code != 200:
                        prRed(f"{url_compose} not found")
                        continue
                    
                except requests.exceptions.HTTPError:
                    prRed(f"URL {url_compose} not found")
                    return 1
                except requests.exceptions.ConnectionError:
                    prRed("Connection Error")
                    return 1

                file_content = str(response.text)
                file_content = file_content.split()
                extract_comments(file_content)
    except IsADirectoryError:
        prRed(f"{dictionary} is a directory")
        return 1
    except FileNotFoundError:
        prRed(f"{dictionary} file not found")
        return 1

    return 0
def main():
    parser = argparse.ArgumentParser(description="HTML comment extractor")

    parser.add_argument("-d","--dictionary",type=str,required=True, help="Pages dictionary")
    parser.add_argument("-u","--url", type=str,required=True,help="Hostname")

    args = parser.parse_args()
    page_request(args.url,args.dictionary)

if __name__ == "__main__":
    main()
