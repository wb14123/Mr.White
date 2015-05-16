

var host = "http://192.168.2.120:5000";

var timer = null;
var intervalTime = 100;


function httpGet(theUrl) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", theUrl, true);
  xmlHttp.send(null);
}

function cmd(url) {
  timer = setInterval(function() {httpGet(host + url)}, intervalTime)
}

function stop() {
  httpGet(host + "/stop");
  clearInterval(timer)
}
