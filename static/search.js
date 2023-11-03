function tableSearch(){
    //Inlialising Variables
    let input= document.getElementById("search");
    let fliter = input.value.toUpperCase();
    let table= document.getElementById("patient_info");
    let tr = table.getElementsByTagName("tr");
    

    for(let i =0;i< tr.length;i++){
        let td =tr[i].getElementsByTagName("td")[0];
        if(td){
             let txtValue = td.textContent;
            if(txtValue.toUpperCase().indexOf(fliter)> -1){
                tr[i].style.display="";
            }
            else{
                tr[i].style.display ="none";

            }

        }
    }
}

