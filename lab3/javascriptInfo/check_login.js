let log = prompt("Enter login:");
if (log == 'Admin'){
    let pass = prompt('Enter a password: ');
    if (pass == ''){
        alert('Canceled');
    }
    else if(pass == 'TheMaster'){
        alert("Welcome!");
    }
    else{
        alert("Wrong password");
    }
}
else if(log == ''){
    alert("Canceled");
}
else{
    alert("I don't know you");
}