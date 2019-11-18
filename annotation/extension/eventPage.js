var menuItem = {
  "id": "happySelection",
  "title": "Annotate it!",
  "contexts": ["selection"]
};

chrome.contextMenus.create(menuItem);

var d = {
  "context": "http://www.w3.org/ns/anno.jsonld",
  "type": "BasicContainer",
  "target" : "Test Happy",
  "body" : "Test Suzan"
}

chrome.contextMenus.onClicked.addListener(function (clickedData) {
  if (clickedData.menuItemId == "happySelection" && clickedData.selectionText) {
    // $.get("https://happy-annotation-server.herokuapp.com/getText", function(data, status){
    //   alert("Data: " + data + "\nStatus: " + status);
    // });

    //alert("You selected: " + clickedData.selectionText);

    // alert("Dummy post request with selection: '" + clickedData.selectionText + "' prevented!");

    // $.ajax({
    //   type: "POST",
    //   url:"https://happy-annotation-server.herokuapp.com/text",
    //   data:d
    // });

    alert("test finished..")
  }
});