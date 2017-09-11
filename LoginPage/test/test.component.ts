import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.scss']
})
export class TestComponent implements OnInit {

  variable = "foo";
  constructor() { }

  ngOnInit() {
  }

  onClick(){
    alert ("You clicked me"); 
  }

  onHover(){
    alert ("You are about to click on me");
  }

}
