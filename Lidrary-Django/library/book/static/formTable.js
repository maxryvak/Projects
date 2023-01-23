function formTable(selector){
    let all_books = document.querySelector(selector);
    let form = all_books.getElementsByTagName("form")[0];
    let table = all_books.getElementsByTagName("table")[0];

    form.onkeyup = function(ev){
        let name = form.elements[0].value;
        let author = form.elements[1].value;
        let count = form.elements[2].value;

        for(let i = 1; i < table.rows.length; i++){
            table.rows[i].className = "";

            if(
                table.rows[i].cells[1].innerHTML.indexOf(name) == -1 ||
                table.rows[i].cells[2].innerHTML.indexOf(author) == -1 ||
                table.rows[i].cells[3].innerHTML.indexOf(count) == -1
            ){
                table.rows[i].className = "hide";
            }
        }
    }
}

formTable(".all_books")