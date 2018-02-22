var stringScrubber = function (string) {
  if (string === false) {
    string = 'wrong input'
  } else if (string === null || string === undefined) {
    string = 'wrong input'
  }
  var trimmedString = string.trim()
  string = trimmedString.toLowerCase()
  return string
}
var startGame = function () {
  var descionOne = window.prompt('pick a starter pokemon (bulbsaur, squirtle, charmander)')
  var pokemon = 'nothing'
  descionOne = stringScrubber(descionOne)
  if (descionOne === 'wrong input') {
    window.alert('You choose something invalid')
  }
  if (descionOne === 'bulbsaur') {
    pokemon = '1'
  } else if (descionOne === 'squirtle') {
    pokemon = '2'
  } else if (descionOne === 'charmander') {
    pokemon = '3'
  } else {
    window.alert('That\'s not a pokemon')
    pokemon = '4'
    return pokemon
  }
  var choice = window.confirm('you\'ve choosen ' + descionOne + ' do you want this pokemon?')
  if (!choice) {
    pokemon = '4'
    return pokemon
  }
  return pokemon
}

var battle = function (pokemon, difficulty) {
  var starter = ''
  var gary = ''
  var health = 20
  var dmg = 0
  var move = ''
  var chance = 0
  if (pokemon === '1') {
    starter = 'bulbsaur'
    gary = 'charmander'
  } else if (pokemon === '2') {
    starter = 'squirtle'
    gary = 'bulbsaur'
  } else if (pokemon === '3') {
    starter = 'charmander'
    gary = 'squirtle'
  } else {
    window.alert('something has gone horribly wrong')
    return
  }
  window.alert('Gary wants to battle')
  window.alert('Gary sent out ' + gary)
  window.alert('Go ' + starter)
  if (difficulty === 1) {
    while (health > 0 && dmg < 20) {
      move = window.prompt('choose a move (scratch or claw)')
      move = stringScrubber(move)
      if (move === 'scratch') {
        chance = Math.random()
        if (chance >= 0.5) {
          window.alert('you did 4 points of damage!')
          dmg += 4
        } else {
          window.alert('the attack missed!')
        }
      } else if (move === 'claw') {
        chance = Math.random()
        if (chance >= 0.8) {
          window.alert('you did 10 points of damage!')
          dmg += 10
        } else {
          window.alert('the attack missed!')
        }
      } else {
        window.alert('that\'s not a move')
        continue
      }
      if (dmg >= 20) {
        break
      }
      window.alert('gary used tackle! ')
      chance = Math.random()
      if (chance >= 0.7) {
        window.alert('tackle did 5 damage!')
        health -= 5
      } else {
        window.alert('the attack missed!')
      }
    }
  } else if (difficulty === 2) {
    while (health > 0 && dmg < 20) {
      move = window.prompt('choose a move (scratch or claw)')
      move = stringScrubber(move)
      if (move === 'scratch') {
        chance = Math.random()
        if (chance >= 0.6) {
          window.alert('you did 4 points of damage!')
          dmg += 4
        } else {
          window.alert('the attack missed!')
        }
      } else if (move === 'claw') {
        chance = Math.random()
        if (chance >= 0.8) {
          window.alert('you did 10 points of damage!')
          dmg += 10
        } else {
          window.alert('the attack missed!')
        }
      } else {
        window.alert('that\'s not a move')
        continue
      }
      if (dmg >= 20) {
        break
      }
      window.alert('gary used tackle! ')
      chance = Math.random()
      if (chance >= 0.5) {
        window.alert('tackle did 5 damage!')
        health -= 5
      } else {
        window.alert('the attack missed!')
      }
    }
  } else if (difficulty === 3) {
    while (health > 0 && dmg < 20) {
      move = window.prompt('choose a move (scratch or claw)')
      move = stringScrubber(move)
      if (move === 'scratch') {
        chance = Math.random()
        if (chance >= 0.7) {
          window.alert('you did 4 points of damage!')
          dmg += 4
        } else {
          window.alert('the attack missed!')
        }
      } else if (move === 'claw') {
        chance = Math.random()
        if (chance >= 0.8) {
          window.alert('you did 10 points of damage!')
          dmg += 10
        } else {
          window.alert('the attack missed!')
        }
      } else {
        window.alert('that\'s not a move')
        continue
      }
      if (dmg >= 20) {
        break
      }
      window.alert('gary used tackle! ')
      chance = Math.random()
      if (chance >= 0.3) {
        window.alert('tackle did 5 damage!')
        health -= 5
      } else {
        window.alert('the attack missed!')
      }
    }
  }
  if (dmg >= 20) {
    window.alert('you win!')
  } else if (health <= 0) {
    window.alert('you lose')
  }
}

var main = function () {
  var difficultyChoice = 0
  var starterpokemon = startGame()
  if (starterpokemon === '4') {
    main()
  } else {
    while (difficultyChoice <= 0 || difficultyChoice > 3) {
      difficultyChoice = window.prompt('select difficulty (1: easy, 2: medium, 3: hard)')
      var difficulty = parseInt(difficultyChoice)
      if (isNaN(difficulty)) {
        window.alert('that\'s not a difficulty')
      } else if (difficulty > 3) {
        window.alert('whoa too challenging, lets tone it down a bit')
      } else if (difficulty <= 0) {
        window.alert('now that\'s not even trying')
      }
    }
    battle(starterpokemon, difficulty)
  }
}

main()
