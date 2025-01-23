import requests
import sys
from xml.etree import ElementTree
from urllib.parse import quote

def fetch_bgg_game_data(game_name):
    search_url = f"https://boardgamegeek.com/xmlapi2/search?query={game_name}&type=boardgame"
    search_response = requests.get(search_url)
    
    # Print the raw XML response for debugging
    print(search_response.text)  # Add this to check the raw response
    
    if search_response.status_code == 200:
        search_tree = ElementTree.fromstring(search_response.content)
        items = search_tree.findall('item')  # Find all items in the search response
        
        if items:
            games = []
            for item in items[:20]:  # Limit to 20 results
                game_id = item.attrib['id']
                game_details = fetch_bgg_game_details(game_id)
                if game_details:
                    games.append(game_details)  # Append game details to the list
            return games
    return None

def fetch_bgg_game_details(game_id):
    details_url = f"https://boardgamegeek.com/xmlapi2/thing?id={game_id}"
    details_response = requests.get(details_url)
    
    # Check if the response is OK
    if details_response.status_code == 200:
        details_tree = ElementTree.fromstring(details_response.content)
        item = details_tree.find('item')
        
        # Debugging: Print the whole item to inspect the XML
        if item is not None:
            print("Item found:")
            print(ElementTree.tostring(item, encoding='unicode'))  # Print the raw XML of the item
            
            # Extracting game details
            name = item.find("name[@type='primary']").attrib.get('value', 'Unknown')
            description = item.find('description').text or 'No description available'
            minplayers = item.find('minplayers').attrib.get('value', 'Unknown')
            maxplayers = item.find('maxplayers').attrib.get('value', 'Unknown')
            image = item.find('image').text or 'No image available'
            
            # Debugging: Print out the details being extracted
            print(f"Game Name: {name}")
            print(f"Description: {description}")
            print(f"Min Players: {minplayers}")
            print(f"Max Players: {maxplayers}")
            print(f"Image URL: {image}")
            
            return {
                'name': name,
                'description': description,
                'minplayers': minplayers,
                'maxplayers': maxplayers,
                'image': image
            }
    else:
        print(f"Error: Failed to retrieve details for game ID {game_id}")
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bgg_api.py <game_name>")
        sys.exit(1)
    
    game_name = sys.argv[1]
    games = fetch_bgg_game_data(game_name)
    if games:
        for game in games:
            print(game)
    else:
        print("No games found.")