// Require Node's http module and assign it to a variable
var http = require('http')

function getRandomInt (min, max) {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min)) + min
}

function displayJoke () {
  var displayText = ''
  var picker = getRandomInt(1, 4)
  if (picker === 1) {
    displayText = '<p>Can a kangaroo jump higher than a house? Of course, a house doesnt jump at all.</p>'
  } else if (picker === 2) {
    displayText = '<p>My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.</p>'
  } else {
    displayText = '<p>I heard women love a man in uniform. Cant wait to start working at McDonalds.</p>'
  }
  return displayText
}

// Create a new server that just says "Hi!!" at every route
var server = http.createServer(function (request, response) {
  if (request.url === '/') {
    response.end(
      '<h1>Hello and Welcome to my first Web Server</h1>'
    )
  } else if (request.url === '/cuteness') {
    response.end(
      '<h1>If you are looking down, have a cute animal</h1>' +
      '<img src="http://i.imgur.com/BxuIF4w.jpg" alt="Cute animal">' +
      '<p></p>' +
      '<a href="/">home page</a>'
    )
  } else if (request.url === '/random-joke') {
    var displayText = displayJoke()
    response.end(
      '<h1>Have a random joke</h1>' +
      displayText +
      '<a href="/">home page</a>'
    )
  } else {
    response.end(
      '<h1>Page Not Found</h1>' +
      '<p>The page you were looking for (' +
      request.url +
      ') doesnt exist.</p>' +
      '<a href="/">home page</a>'
    )
  }
})

// Listen on port 8080, so that we can reach the app at
// localhost:8080
var port = process.env.PORT || 8080
server.listen(port)

// Output a friendly message to the terminal
console.log('Server running at http://localhost:' + port + '/')
