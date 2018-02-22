var counted = window.localStorage.getItem('count')

if (counted === null || counted === undefined) {
  window.localStorage.setItem('count', 1)
  counted = 1
} else {
  var tempCounter = parseInt(counted)
  var newCounter = tempCounter + 1

  window.localStorage.setItem('count', newCounter)
  counted = newCounter
}

var text = '<h1>counter: ' + counted + '</h1>'
document.getElementById('displayCount').innerHTML = text

var displayTime = function (state) {
  if (state === 'day') {
    document.body.setAttribute('class', 'day-theme')
  } else {
    document.body.setAttribute('class', 'night-theme')
  }
  return window.localStorage.getItem('theme')
}

var changeTime = function (state) {
  if (state === 'day') {
    document.body.setAttribute('class', 'night-theme')
    window.localStorage.setItem('theme', 'night')
  } else {
    document.body.setAttribute('class', 'day-theme')
    window.localStorage.setItem('theme', 'day')
  }
  return window.localStorage.getItem('theme')
}

var lightState = window.localStorage.getItem('theme')

lightState = displayTime(lightState)

if (lightState === null || lightState === undefined) {
  document.body.setAttribute('class', 'day-theme')
  window.localStorage.setItem('theme', 'day')
  lightState = window.localStorage.getItem('theme')
}

var switcher = function () {
  lightState = changeTime(lightState)
}

var buttonPress = document.getElementById('moveTime')
buttonPress.addEventListener('click', switcher)
