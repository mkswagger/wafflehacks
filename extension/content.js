// content_script.js
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === 'getText') {
    var text = document.body.innerText;
    sendResponse({ text: text });
  }
});