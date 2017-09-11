import { Component, OnInit } from '@angular/core';
//import { LoginService } from "app/login.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  messagelogin = "";
  user ="";
  password = "";

  constructor() { }

  ngOnInit() {
  }

  onClick(){
    
    if (this.password == "1234") {
        alert ("OK");
    }else{
      this.messagelogin = "Login Failed";
    }
    
  }

}
