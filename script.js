fetch("Recipe.json")
.then(function(response){
   return response.json();
})
.then(function(products){
   let placeholder = document.querySelector("#data-output");
   let out = "";
   for(let product of products){
      out += `
         <tr>
            <td> <img src='${product.image}'> </td>
            <td>${product.name}</td>
            <td>${product.picture}</td>
            <td>${product.description}</td>
            <td>${product.rating}</td>
         </tr>
      `;
   }

   placeholder.innerHTML = out;
});
