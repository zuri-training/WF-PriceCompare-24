function likeInteraction(){
    document.querySelector(".rating").innerHTML = "We are glad we could help!";
}
function dislikeInteraction(){
document.querySelector(".rating").innerHTML = "Thanks! We keep improving everyday.";
}

let like = document.querySelector(".like");
like.addEventListener("click", likeInteraction);
let dislike = document.querySelector(".dislike");
dislike.addEventListener("click", dislikeInteraction);
