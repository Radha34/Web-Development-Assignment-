
   const likeBtn = document.querySelector(".like_btn");
   const likeIcon = document.querySelector("#icon");
   const count = document.querySelector("#count");
   let clicked = false;
   likeBtn.addEventListener("click",()=>{
       if(!clicked){
           clicked = true;
           likeIcon.innerHTML ='<i class="fas fa-heart" style="color:red;"></i>';
           count.textContent++;
       }
       else{
           clicked = false;
           likeIcon.innerHTML='<i class="far fa-heart"></i>';
           count.textContent--;
       }
   });

   const likeBtn2 = document.querySelector(".like_btn2");
   const likeIcon2 = document.querySelector("#icon2");
   const count2 = document.querySelector("#count2");
   let clicked2 = false;
   likeBtn2.addEventListener("click",()=>{
       if(!clicked2){
           clicked2 = true;
           likeIcon2.innerHTML ='<i class="fas fa-heart" style="color:red;"></i>';
           count2.textContent++;
       }
       else{
           clicked2 = false;
           likeIcon2.innerHTML='<i class="far fa-heart"></i>';
           count2.textContent--;
       }
   });

   const likeBtn3 = document.querySelector(".like_btn3");
   const likeIcon3 = document.querySelector("#icon3");
   const count3 = document.querySelector("#count3");
   let clicked3 = false;
   likeBtn3.addEventListener("click",()=>{
       if(!clicked3){
           clicked3 = true;
           likeIcon3.innerHTML ='<i class="fas fa-heart" style="color:red;"></i>';
           count3.textContent++;
       }
       else{
           clicked3 = false;
           likeIcon3.innerHTML='<i class="far fa-heart"></i>';
           count3.textContent--;
       }
   });
