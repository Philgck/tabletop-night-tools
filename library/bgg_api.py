import requests
from xml.etree import ElementTree

def fetch_bgg_game_data(game_name):
    # Refine the query and use more specific keywords to increase the chance of fetching the correct game
    search_url = f"https://boardgamegeek.com/xmlapi2/search?query={game_name}&type=boardgame&exact=1"
    
    # Make a request to the BGG search API
    search_response = requests.get(search_url)
    
    if search_response.status_code == 200:
        search_tree = ElementTree.fromstring(search_response.content)
        items = search_tree.findall('item')  # Find all items in the search response
        if items:
            games = []
            
            for item in items:  # No need to limit to the first 20, since we're only interested in board games
                game_id = item.attrib['id']
                game_type = item.attrib.get('type')

                # Only process boardgame types, and ignore expansions or other game types
                if game_type == 'boardgame':
                    game_details = fetch_bgg_game_details(game_id)
                    if game_details:
                        # Ensure the game is the base game and not an expansion
                        if not any(link.attrib['type'] == 'boardgameexpansion' for link in item.findall('link')):
                            games.append(game_details)  # Append game details to the list
            return games
    return None

def fetch_bgg_game_details(game_id):
    # Fetch detailed information for the game using the game_id
    details_url = f"https://boardgamegeek.com/xmlapi2/thing?id={game_id}"
    details_response = requests.get(details_url)
    
    if details_response.status_code == 200:
        details_tree = ElementTree.fromstring(details_response.content)
        item = details_tree.find('item')
        
        if item is not None:
            name = item.find("name[@type='primary']").attrib.get('value', 'Unknown')
            description = item.find('description').text or 'No description available'
            minplayers = item.find('minplayers').attrib.get('value', 'Unknown')
            maxplayers = item.find('maxplayers').attrib.get('value', 'Unknown')
            image = item.find('image').text or 'No image available'
            
            return {
                'name': name,
                'description': description,
                'minplayers': minplayers,
                'maxplayers': maxplayers,
                'image': image
            }
    return None
