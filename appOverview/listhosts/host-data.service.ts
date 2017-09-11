import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/throw';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';

import { IEsxiHost } from './esxihost';

@Injectable()

export class HostDataService {
    private _hostUrl = './json/hosts.json';

    constructor(private _http: HttpClient){

    }

    getHosts(): Observable<IEsxiHost> {
        return this._http.get(this._hostUrl)
        .do(data => console.log('All: '+ JSON.stringify(data)))
        .catch(this.handleError);
    }
    private handleError(err:HttpErrorResponse) {
        console.log(err.message);
        return Observable.throw(err.message);
    }

}