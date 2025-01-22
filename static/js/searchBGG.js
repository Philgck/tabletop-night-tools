// This script is used to search for games on BoardGameGeek and populate the game form with the selected game's details

async function searchBGGGame() {
    const gameName = document.getElementById('gameSearch').value;
    if (gameName) {
        showLoadingSpinner();
        try {
            const response = await fetch(`/search_bgg_games/?game_name=${encodeURIComponent(gameName)}`);
            if (response.ok) {
                const games = await response.json();
                populateGameOptions(games);
            } else {
                alert('No games found');
            }
        } catch (error) {
            console.error('Error fetching game data:', error);
            alert('An error occurred while searching for games');
        } finally {
            hideLoadingSpinner();
        }
    }
}
// Presents a loading spinner whilst the search is being performed

function showLoadingSpinner() {
    document.getElementById('loadingSpinner').style.display = 'block';
}

function hideLoadingSpinner() {
    document.getElementById('loadingSpinner').style.display = 'none';
}

function populateGameOptions(games) {
    const gameSelect = document.getElementById('gameSelect');
    gameSelect.innerHTML = '<option value="">Select a game</option>';
    games.forEach(game => {
        const option = document.createElement('option');
        option.value = JSON.stringify(game);
        option.textContent = game.name;
        gameSelect.appendChild(option);
    });
}



function selectGame() {
    const gameSelect = document.getElementById('gameSelect');
    const selectedGame = gameSelect.value;
    if (selectedGame) {
        const game = JSON.parse(selectedGame);
        document.getElementById('id_title').value = game.name;
        document.getElementById('id_description').value = game.description;
        document.getElementById('id_minimum_player_count').value = game.minplayers;
        document.getElementById('id_maximum_player_count').value = game.maxplayers;
        document.getElementById('id_image_url').value = game.image;
    }
}
