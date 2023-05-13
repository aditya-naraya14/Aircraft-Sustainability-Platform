import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

export interface MyObject {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {

  displayedColumns;
  myList: MyObject[];

  constructor( private httpClient: HttpClient) { 
    this.getData()
  }


  getData() {
    this.httpClient.get('http://localhost:8000/api/get_data').subscribe((data:any[]) => {
      if (data && data.length > 0) {
        this.myList = data;
        this.displayedColumns = Object.keys(data[0]).filter(key => key!='part_id')

      }
    },error => {
      console.log("error",error);
    })

  }



}