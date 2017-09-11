import { Component, OnInit } from '@angular/core';
import { IEsxiHost } from './esxihost';

import { HostDataService } from "./host-data.service";

@Component({
  selector: 'app-listhosts',
  templateUrl: './listhosts.component.html',
  styleUrls: ['./listhosts.component.css']
})
export class ListhostsComponent implements OnInit {
  hosts: IEsxiHost[] = [];
  errorMessage: any;
  constructor(private _hostDataService: HostDataService) { 

  }

  ngOnInit() {
    this._hostDataService.getHosts()
    .subscribe(
        hosts => {
             this.hosts = hosts;
        },
        error => this.errorMessage = <any>error);
  }

}
