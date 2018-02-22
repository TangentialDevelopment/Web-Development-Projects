var firstNameIn = document.getElementById('fName')
var lastNameIn = document.getElementById('lName')
var desIn = document.getElementById('description')
var emailIn = document.getElementById('email')
var phoneIn = document.getElementById('phone')

var updateProfile = function () {
  var formattedProfile = document.getElementById('refinedProfile')
  var unformattedProfile = document.getElementById('rawProfile')
  var firstName = firstNameIn.value
  var lastName = lastNameIn.value
  var description = desIn.value
  var email = emailIn.value
  var phone = phoneIn.value
  var text = '<h1>Hi, my name is ' + firstName + ' ' + lastName + '!</h1><p>' + description + '</p><p>' +
  'If you\'re interested in a date, you can email me at <a href="mailto:' + email + '" target="_blank">' + email +
  '</a> or give me a call at <a href=tel:' + phone + '" target="_blank">' + phone + '</a>.</p>'

  formattedProfile.innerHTML = text

  unformattedProfile.textContent = text
}

firstNameIn.addEventListener('input', updateProfile)
lastNameIn.addEventListener('input', updateProfile)
desIn.addEventListener('input', updateProfile)
emailIn.addEventListener('input', updateProfile)
phoneIn.addEventListener('input', updateProfile)
