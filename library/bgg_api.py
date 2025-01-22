import requests
from xml.etree import ElementTree

def fetch_bgg_game_data(game_name):
    search_url = f"https://boardgamegeek.com/xmlapi2/search?query={game_name}&type=boardgame,wargame"
    search_response = requests.get(search_url)
    if search_response.status_code == 200:
        search_tree = ElementTree.fromstring(search_response.content)
        items = search_tree.findall('item')  # Find all items in the search response
        if items:
            games = []
            for item in items:
                game_id = item.attrib['id']
                game_details = fetch_bgg_game_details(game_id)
                if game_details:
                    games.append(game_details)  # Append game details to the list
            return games
    return None

def fetch_bgg_game_details(game_id):
    details_url = f"https://boardgamegeek.com/xmlapi2/thing?id={game_id}"
    details_response = requests.get(details_url)
    if details_response.status_code == 200:
        details_tree = ElementTree.fromstring(details_response.content)
        item = details_tree.find('item')
        if item is not None:
            name = item.find("name[@type='primary']").attrib['value']
            description = item.find('description').text
            minplayers = item.find('minplayers').attrib['value']
            maxplayers = item.find('maxplayers').attrib['value']
            image = item.find('image').text
            return {
                'name': name,
                'description': description,
                'minplayers': minplayers,
                'maxplayers': maxplayers,
                'image': image
            }
    return None