// var images = document.getElementsByTagName('img');
// for (var i = 0, l = images.length; i < l; i++) {
//   images[i].src = 'http://placekitten.com/' + images[i].width + '/' + images[i].height;
// }

var tweet_box = document.getElementById("tweet-box-home-timeline");
var active_element = document.activeElement;


$(document).ready(function(){        
    setInterval(function() {
        // console.log($('#tweet-box-home-timeline div').text());

        $.ajax({
            url: "http://127.0.0.1:9000/api",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                text: $('#tweet-box-home-timeline div').text()
            }),
            success: function(response){
                console.log(response.results[0]);
                console.log(response.results[1]);
                // $('#tweet-box-home-timeline div').text(response.results[1])

                if(response.results[0] == "disclosure") {
                    $('#tweet-box-home-timeline').css("color", "red");
                } else {
                    $('#tweet-box-home-timeline').css("color", "#14171a");
                }
            }
        });

    }, 2000);
});