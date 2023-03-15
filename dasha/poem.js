fragments = [
    "Hi Dasha :)"];
  
fetch("poem.json")
  .then(response => response.json())
  .then(json => fragments = json);

function animateText(container, index){
    // Increment the index and wrap around to the beginning of the array
    index = (index + 1) % fragments.length;
    console.log(index)

    // Fade out the old fragment over 1 second
    container.animate([
    { opacity: 1 },
    { opacity: 0 }
    ], {
    duration: 1000,
    fill: "forwards"
    });
    setTimeout(() => {
        while (container.childNodes.length > 0){
            container.childNodes[0].remove();
        }

        for (line of fragments[index]){
            // Create a new text node with the current fragment
            container.appendChild(document.createTextNode(line));
            container.appendChild(document.createElement("br"));
        }
    
        // Fade in the new fragment over 1 second
        container.animate([
            { opacity: 0 },
            { opacity: 1 }
        ], {
            duration: 1500,
            fill: "forwards"
        });


        }, 1000);
    setTimeout(() => {
        animateText(container, index);}, 2000 + fragments[index].length * 1000);
}

window.onload = function() {
    container = document.getElementById("text-container");
    let index = 0;
    const fragmentNode = document.createTextNode(fragments[0]);
    // Append the text node to the container
    container.appendChild(fragmentNode);

    animateText(container, index);
}