window.onload = getUrl;

function getUrl() {
    myUrl = window.location.href;
    changeMenuBackground(myUrl);
}

function changeMenuBackground(url) {
    let myUrl = url;
    if ( myUrl.includes("/quests/") ) {
        let menuItem = document.getElementById("Quests");
        menuItem.classList.add("highlightMenu");
    } else if (myUrl.includes("/skills/")) {
        let menuItem = document.getElementById("Skills");
        let myChild = menuItem.children;
        let hiddenItems = myChild[1].children
        menuItem.classList.add("highlightMenu");
        menuItem.classList.toggle("active");
        
        for(let i=0; i<myChild.length; i++) {
            if (myChild[i].tagName =="DIV") {
                myChild[i].style.display = "block";
            }
        }

        if(myUrl.includes("/warrior")) {
            hiddenItems.item(0).children.item(0).classList.add("highlightMenu");
        } else if (myUrl.includes("/priest")) {
            hiddenItems.item(0).children.item(2).classList.add("highlightMenu");
        } else if (myUrl.includes("/mage")) {
            hiddenItems.item(0).children.item(1).classList.add("highlightMenu");
        } else {
            hiddenItems.item(0).children.item(3).classList.add("highlightMenu");
        }    
        
    } else if (myUrl.includes("/zones/") ) {
        let menuItem = document.getElementById("Zones");
        menuItem.classList.add("highlightMenu");
    } else if (myUrl.includes("/items/") ) {
        let menuItem = document.getElementById("Items");
        console.log(menuItem);
        let myChild = menuItem.children;
        let hiddenItems = myChild[1].children
        menuItem.classList.add("highlightMenu");
        menuItem.classList.toggle("active");
        
        for(let i=0; i<myChild.length; i++) {
            if (myChild[i].tagName =="DIV") {
                myChild[i].style.display = "block";
            }
        }

        if(myUrl.includes("/weapons")) {
            hiddenItems.item(0).children.item(0).classList.add("highlightMenu");
        }   else if (myUrl.includes("/armors")) {
            hiddenItems.item(0).children.item(1).classList.add("highlightMenu");
        }


    } else if (myUrl.includes("/monsters/") ) {
        let menuItem = document.getElementById("Monsters");
        menuItem.classList.add("highlightMenu");
    }  else if (myUrl.includes("/contacts/") ) {
        let menuItem = document.getElementById("Contacts");
        menuItem.classList.add("highlightMenu");
    } else {
        let menuItem = document.getElementById("News");
        menuItem.classList.add("highlightMenu");
    } 
}


const buttons = document.querySelectorAll("[data-carousel-button]")

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const offset = button.dataset.carouselButton === "next" ? 1 : -1
    const slides = button
      .closest("[data-carousel]")
      .querySelector("[data-slides]")

    const activeSlide = slides.querySelector("[data-active]")
    let newIndex = [...slides.children].indexOf(activeSlide) + offset
    if (newIndex < 0) newIndex = slides.children.length - 1
    if (newIndex >= slides.children.length) newIndex = 0

    slides.children[newIndex].dataset.active = true
    delete activeSlide.dataset.active
  })
})
// added selector to navigate screen to specified div
const buttonsItemMenu = document.querySelectorAll("[item-menu-button]")

buttonsItemMenu.forEach(buttonItemMenu => {
    buttonItemMenu.addEventListener("click", () => {
        const itemId = buttonItemMenu.children[1].children[0].innerHTML.toLowerCase()
        document
            .getElementById(itemId)
            .scrollIntoView({ behavior: "smooth" });
    })
})

