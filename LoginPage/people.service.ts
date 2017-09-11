import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import "rxjs/add/operator/map";

@Injectable()
export class PeopleService {

  constructor(private http: Http) { }

  get(page = 1){
    let url = `http://192.168.3.113/api/hosts/`; 
    return this.http.get(url).map(data => data.json());
  }

}
