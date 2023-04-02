$(document).ready(function() {
  // Set up an empty array to hold the game collection
  var gameCollection = [];

  // Function to add a game to the collection
  function addGame(name, genre, console, completed, recommend) {
    gameCollection.push({
      name: name,
      genre: genre,
      console: console,
      completed: completed,
      recommend: recommend
    });
    updateTable();
  }

  // Function to remove a game from the collection
  function removeGame(index) {
    gameCollection.splice(index, 1);
    updateTable();
  }

  // Function to update the table with the current game collection
  function updateTable() {
    // Clear the current table contents
    $('#game-table tbody').empty();

    // Loop through the game collection and add each game to the table
    for (var i = 0; i < gameCollection.length; i++) {
      var game = gameCollection[i];
      var row = '<tr>' +
                '<td>' + game.name + '</td>' +
                '<td>' + game.genre + '</td>' +
                '<td>' + game.console + '</td>' +
                '<td>' + (game.completed ? 'Yes' : 'No') + '</td>' +
                '<td>' + (game.recommend ? 'Yes' : 'No') + '</td>' +
                '<td><button class="edit" data-index="' + i + '">Edit</button> ' +
                '<button class="delete" data-index="' + i + '">Delete</button></td>' +
                '</tr>';
      $('#game-table tbody').append(row);
    }
  }

  // Add a submit handler for the game form
  $('#game-form').submit(function(event) {
    event.preventDefault();
    var name = $('#name').val();
    var genre = $('#genre').val();
    var console = $('#console').val();
    var completed = $('#completed').is(':checked');
    var recommend = $('#recommend').is(':checked');
    addGame(name, genre, console, completed, recommend);
    $('#name').val('');
    $('#genre').val('');
    $('#console').val('');
    $('#completed').prop('checked', false);
    $('#recommend').prop('checked', false);
  });

  // Add a click handler for the delete buttons
  $('#game-table').on('click', '.delete', function() {
    var index = $(this).data('index');
    removeGame(index);
  });

  // Add a click handler for the edit buttons
  $('#game-table').on('click', '.edit', function() {
    var index = $(this).data('index');
    var game = gameCollection[index];
    $('#name').val(game.name);
    $('#genre').val(game.genre);
    $('#console').val(game.console);
    $('#completed').prop('checked', game.completed);
    $('#recommend').prop('checked', game.recommend);
    removeGame(index);
  });
});
