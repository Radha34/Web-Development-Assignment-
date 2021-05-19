const openModalButtons = document.querySelectorAll('[data-modal-target]')
const closeModalButtons  = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')

openModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget)

        openModal(modal)
    })
})



closeModalButtons.forEach(button =>{
    button.addEventListener('click',() =>{
        const modal = button.closest('.popup')
        closeModal(modal)
    })
})

function openModal(popup){
    if(popup == null ) return 
    popup.classList.add('active')
    overlay.classList.add('active')

}

function closeModal(popup){
    if(popup == null ) return 
    popup.classList.remove('active')
    overlay.classList.remove('active')

    
}
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
  this.classList.toggle("active");
  var dropdownContent = this.nextElementSibling;
  if (dropdownContent.style.display === "block") {
  dropdownContent.style.display = "none";
  } else {
  dropdownContent.style.display = "block";
  }
  });
}

