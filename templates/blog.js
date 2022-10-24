//部落格
var title = document.getElementById("title");
var content = document.getElementById("content");
var btn = document.getElementById("btn");
var list = document.getElementById("list");
btn.addEventListener("click",function(){
    console.log(title.Value);
    console.log(content.Value);
    console.log(list.innerHTML);
    const date = new Date();    

    list.innerHTML = list.innerHTML + `
    <div class = "article">
        <h2>${title.value}</h2>
        <p>${content.value}</p>
        <p>${date.toLocaleString()}</p>
        <hr/>
    </div>
    `;
    title.value ="";
    content.value ="";
    
})