// function searchGame() {
//     var gameName = document.getElementById('gameSearch').value;
    
//     if (gameName === "") {
//         alert("Please enter a game name.");
//         return;
//     }

//     var apiUrl = `https://www.boardgamegeek.com/xmlapi2/search?search=${encodeURIComponent(gameName)}&type=boardgame`;

//     fetch(apiUrl)
//         .then(response => response.text())
//         .then(data => {
//             var parser = new DOMParser();
//             var xmlDoc = parser.parseFromString(data, "text/xml");
//             displayGameInfo(xmlDoc);
//         })
//         .catch(error => {
//             console.error("Error fetching game data: ", error);
//             alert("Something went wrong. Please try again.");
//         });
// }