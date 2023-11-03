console.log('hi')
const send_buttons=document.querySelectorAll("button")
for(const button of send_buttons){
    button.addEventListener("click",()=>{
        const schedule_id= button.id
        const data={
            schedule_id:schedule_id
        }
        fetch('/send-message',{
            method: 'POST',
            body:JSON.stringify(data),
            headers:{
                'Content-Type':'application/json',
            }
        })
        .then((response) => response.json())
        .then((responseJson) => {
            alert(responseJson.status);
        });
    });
}

