$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

$(document).ready(function() {

    function isTouchDevice() {
        return 'ontouchstart' in document.documentElement;
    }

    if (isTouchDevice()) {
        $(".up-arrow, .down-arrow").click(function () {
            var login = $(".login-button");
            var selected = $(this)
            console.log(selected)
            var pk = $(this).parent().attr("name");
            var which = $(this).attr("name");
            console.log(pk);
            console.log(which);

            var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();

            $.post(window.location.pathname,
            {
                item_pk: pk,
                item_vote: which,
                csrfmiddlewaretoken: CSRFtoken
            },
            function(response) {q
                console.log(response);
                console.log(response.logged_in)
                if ((response.logged_in == 'true') || (response.logged_in == undefined)) {
                    selected.css({'transition-timing-function':'ease','transition':'0.3s','background':'#F8F8F8', 'color':'#4f4f4f'});
                    setTimeout(function() {
                        selected.css({'transition-timing-function':'ease','transition':'0.3s','background':'white'});
                    }, 1000);
                } else {
                    console.log("not logged in");
                    selected.css({'transition-timing-function':'ease','transition':'0.3s','background':'#fff0f0', 'color':'#fa4848'});
//                        login.css({'transition-timing-function':'ease','transition':'0.3s','background':'#e1fadc', 'color':'#7cfc62'});
                    selected.tooltip('toggle');
                    setTimeout(function(){
                        selected.css({'transition-timing-function':'ease','transition':'0.3s','background':'white', 'color':'lightgrey'});
//                            login.css({'transition-timing-function':'ease','transition':'0.3s','background':'white', 'color':'lightgrey'});
                        selected.tooltip('toggle');
                    }, 1000);
                }
            });
        }).on("touchstart", function() {
            $(this).css({"background":"#F8F8F8", "cursor":"pointer"})
        }).on("touchend", function() {
            $(this).css({"background":"white"})
        })

        $(".menu-row").find("a").on("touchstart", function() {
            $(this).css({"background":"#F8F8F8", "cursor":"pointer"})
        }).on("touchend", function() {
            $(this).css({"background":"white"})
        })
    } else {
        $(".up-arrow, .down-arrow").click(function () {
            var login = $(".login-button");
            var selected = $(this)
            console.log(selected)
            var pk = $(this).parent().attr("name");
            var which = $(this).attr("name");
            console.log(pk);
            console.log(which);

            var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();
            $.post(window.location.pathname,

            {
                item_pk: pk,
                item_vote: which,
                csrfmiddlewaretoken: CSRFtoken
            },

            function(response) {
                console.log(response);
                console.log(response.logged_in)
                if ((response.logged_in == 'true') || (response.logged_in == undefined)) {
                    selected.css({'transition-timing-function':'ease','transition':'0.3s','background':'#F8F8F8', 'color':'#4f4f4f'});
                    setTimeout(function() {
                        selected.css({'transition-timing-function':'ease','transition':'0.3s','background':'white'});
                    }, 1000);
                } else {
                    console.log("not logged in");
                    selected.css({'transition-timing-function':'ease','transition':'0.3s','background':'#fff0f0', 'color':'#fa4848'});
//                        login.css({'transition-timing-function':'ease','transition':'0.3s','background':'#e1fadc', 'color':'#7cfc62'});
                    selected.tooltip('toggle');
                    setTimeout(function(){
                        selected.css({'transition-timing-function':'ease','transition':'0.3s','background':'white', 'color':'lightgrey'});
//                            login.css({'transition-timing-function':'ease','transition':'0.3s','background':'white', 'color':'lightgrey'});
                        selected.tooltip('toggle');
                    }, 1000);
                }
            })

        }).on("mouseover", function() {
//            if ($(this).css("background-color") == "rgba(0, 0, 0, 0)" || $(this).css("background-color") == "rgb(255, 255, 255)") { // condition for the case of button have background other than the lightgrey highlight
                    $(this).css({"background":"#F8F8F8", "cursor":"pointer"})
//            }
        }).on("mouseleave", function() {
//            if ($(this).css("background-color") == "rgb(248, 248, 248)") { // if the arrow button has been clicked (and color is wanted) then do not reset the background color as the post has been voted on
                    $(this).css({"background":"white"})
//            }
        })

        $(".menu-row").find("a").on("mouseover", function() {
            $(this).css({"background":"#F8F8F8", "cursor":"pointer"})
        }).on("mouseleave", function() {
            $(this).css({"background":"white"})
        })
    } //end else
})