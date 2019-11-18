var msgObj = ""

$(function () {
  $('#name').keyup(function () {

    msgObj = $('#name').val();
    $('#greet').text('Looking for: ' + $('#name').val());

    chrome.tabs.query({}, tabs => {
      tabs.forEach(tab => {
        chrome.tabs.sendMessage(tab.id, msgObj);
      });
    });


  })
})

