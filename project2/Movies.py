# Movies
# read movies.txt file
# movies.txt is from Bard and i don't agree
# convert input string to JSON format
# sort JSON (can use sort function)
# output to movies.json
# convert to xml

import requests
import json
from xml.dom import minidom


def read_txt_from_url(url: str) -> str:
    response = requests.get(url)
    content = response.content.decode('utf-8')
    return content


def read_txt_from_local(path: str) -> str:
    with open(path) as txtFile:
        content = txtFile.read()
    txtFile.close()
    return content


def movies_string_to_dictList(moviesString: str) -> list:
    # read line one
    movieDict = {}
    movieList = []
    lines = moviesString.splitlines()
    # print(lines)
    # pop out header
    header = lines.pop(0)
    # print(header)
    # convert to dict
    for line in lines:
        itemList = line.split(",")
        # pop out rank, no use
        itemList.pop(0)
        title = itemList.pop(0) # pop out title
        # exception! we have two movie name have ","
        if itemList[0].startswith(" "):
            title = title + "," + itemList.pop(0)
            # print("add title")
        # pop out genre
        genre = itemList.pop(0)
        director = {}
        # create director name list incase there are two or more director
        i = 0
        while i < len(itemList):
            if not itemList[i].isnumeric():
                if not director.get("Name"):
                    director["Name"] = [itemList[i]]
                else:
                    director["Name"] = director["Name"] + [itemList[i]]
            else:
                break
            i += 1

        year = itemList[i]
        studio = itemList[i+1]

        movieDict["Movie"] = {
            "Title":title,
            "Genre":genre,
            "Director":director,
            "Studio":studio,
            "Year":year,}

        # movieDict["Movie"] = [
        #     {"Title":title},
        #     {"Genre":genre},
        #     {"Director":director},
        #     {"Studio":studio},
        #     {"Year":year},]
        # print(movieDict)

        movieList.append(movieDict.copy())
        movieDict.clear()

    return movieList


def sort_movies_list(movieList):
    movieList.sort(key = lambda ele : ele["Movie"]["Title"])
    movieListSorted = movieList.copy()
    # print(movieListSorted[:5])
    return movieListSorted

def sorted_movies_to_xml(movieListSorted):
    doc = minidom.Document() # 建立DOM

    movieListSorted

    movies = doc.createElement("Movies") # create movies tag root element
    doc.appendChild(movies) # doc: movies

    # every movie have an element
    for movieDict in movieListSorted:
        # create movie tag element
        movieEle = doc.createElement("Movie")
        # other element will all attach to movie
        for key, value in movieDict["Movie"].items():
            if key == "Director":
                element = doc.createElement(key)
                for director in value["Name"]:
                    childElement = doc.createElement("Name")
                    childElementText = doc.createTextNode(director)
                    childElement.appendChild(childElementText)
                    element.appendChild(childElement)
                    movieEle.appendChild(element)

            else:
                element = doc.createElement(key)
                text = doc.createTextNode(value)
                element.appendChild(text)
                movieEle.appendChild(element)
        movies.appendChild(movieEle)

    # print(doc.toprettyxml(indent="  "))
    return doc


def main():
    # read txt file
    content = read_txt_from_url("https://www.public.asu.edu/~ychan175/Movies.txt")
    # content = read_txt_from_local("Movies.txt")
    # print(content)
    # convert to python list for later json output
    movieList = movies_string_to_dictList(content)
    # print(movieList)
    # jsonObject = json.dumps(movieList, indent = 4)
    # print(jsonObject)
    # I find out I need a movies key for my list
    movies = {"Movies": movieList}
    # output json file without sorting
    with open("movies_not_sorted.json", "w") as f:
        json.dump(movies, f, indent = 4)
    f.close()
    # sort python list
    movieListSorted = sort_movies_list(movieList)
    # I find out I need a movies key for my list
    sortedMovies = {"Movies": movieListSorted}
    # output json file with sorted list
    with open("movies_sorted.json", "w") as f:
        json.dump(sortedMovies, f, indent = 4)
    f.close()
    # convert list to xml tree
    xmlDoc = sorted_movies_to_xml(movieListSorted)

    xmlStr = xmlDoc.toprettyxml(indent="  ") # xmlDoc 轉成字串
    with open("Movies.xml", "w") as f:
        f.write(xmlStr)
    f.close()

if __name__ == "__main__":
    main()
