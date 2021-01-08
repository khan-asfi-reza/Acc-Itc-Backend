
// State
let member = 0;
let exec = 0;
let event = 0;
let workshop = 0;

// DOM

const numberCounter = document.getElementById('member');
const execCounter = document.getElementById('exec');
const eventCounter = document.getElementById('event');
const workshopCounter = document.getElementById('workshop');
const inputName = document.getElementById('name');
const inputEmail = document.getElementById('email');
const inputMessage = document.getElementById('message');
const formButton = document.getElementById('work');
// Button Events


document.getElementById('learn_more').addEventListener('click', ()=>{
    document.getElementById('introduction').scrollIntoView()
});

// Dom Load Events
document.addEventListener('DOMContentLoaded', typeWriter);
startImageTransition();


const teamCounter = ()=> {
    function increaseMember(breakpoint, dom) {
        if (member < breakpoint) {
            member+=10;
            dom.innerHTML = `+${member}<br/>Members`;
        }
    }
    function increaseExec(breakpoint, dom) {
        if (exec < breakpoint) {
            exec+=1;
            dom.innerHTML = `+${exec}<br/>Executives`;
        }
    }
    function increaseEvent(breakpoint, dom) {
        if (event < breakpoint) {
            event+=1;
            dom.innerHTML = `+${event}<br/>Events`;
        }
    }
    function increaseWorkshop(breakpoint, dom) {
        if (workshop < breakpoint) {
            workshop+=10;
            dom.innerHTML = `+${workshop}<br/>Workshops`;
        }
    }

    const interval =setInterval(()=>{
        increaseMember(500, numberCounter);
        increaseExec(50, execCounter);
        increaseEvent(50, eventCounter);
        increaseWorkshop(100, workshopCounter);
        if(member === 500 && exec === 50 && event === 50 && workshop === 100){
            clearInterval(interval);
        }
    }, 10);
};
// Scroll Events
const viewport_functions = [
    {
        dom:document.getElementById('sector_header'),
        function:()=>{
            document.getElementById('sector').classList.add('sector-animated')
        }
    },
    {
        dom:document.getElementById('event_header'),
        function:()=>{
            document.getElementById('event_section').classList.add('sector-animated')
        }
    },
    {
        dom:document.getElementById('introduction_header'),
        function:()=>{
            document.getElementById('introduction').classList.add('sector-animated')
        }
    },
    {
        dom:document.getElementById('our_team_header'),
        function:()=>{
            document.getElementById('our_team').classList.add('sector-animated')
        }
    },
    {
        dom:document.getElementById('number_counter'),
        function:()=>{
            teamCounter()
        }
    },

];


(function f() {
    viewport_functions.forEach((each)=>{
        onViewPort(each.dom, each.function)
    })
})();




const loadingButtonHtml = `<div class="lds-dual-ring"></div>`;
const formSendButtonOnClick = () => {
    formButton.innerHTML = loadingButtonHtml;
    formButton.disabled = true;
    const response = postData('http://127.0.0.1:8000/api/message/', {
        'name':inputName.value,
        'email':inputEmail.value,
        'message':inputMessage.value
    }).then((res)=>{
        formButton.innerHTML = "Send";
        formButton.disabled = false;

        document.getElementById('form_').innerHTML = `<div class="form-heading"><p>Thank you for your response, we will get back to you soon</p></div>`

    }).catch((e)=>{

        formButton.innerHTML = "Send";
        formButton.disabled = false;
        document.getElementById('form_').innerHTML = `<div class="form-heading"><p>Thank you for your response, we will get back to you soon</p></div>`;

    })

};
formButton.addEventListener('click', formSendButtonOnClick);