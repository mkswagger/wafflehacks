// popup.js

document.addEventListener('DOMContentLoaded', function () {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, { action: 'getText' }, function (response) {
      if (response && response.text) {
        var text = response.text;
        checkText(text);
      }
    });
  });
});

function checkText(text) {
  fetch('http://localhost:5000/check_text', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ text: text })
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      var resultDiv = document.getElementById('result');
      resultDiv.textContent = data.result;
    })
    .catch(function (error) {
      console.error('Error occurred while checking text:', error);
    });
}