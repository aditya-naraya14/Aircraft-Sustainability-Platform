import { HttpClient } from '@angular/common/http';
import {AfterViewInit, Component, ViewChild} from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import {MatTableDataSource} from '@angular/material/table';


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
  myList;

  constructor( private httpClient: HttpClient) { 
    this.getData()
  }

  @ViewChild(MatPaginator) paginator: MatPaginator;

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.myList.filter = filterValue.trim().toLowerCase();
  }

  getData() {
    this.httpClient.get('http://localhost:8000/api/get_data').subscribe((data:any[]) => {
      if (data && data.length > 0) {
        this.myList = new MatTableDataSource(data);
        this.myList.paginator = this.paginator;
        this.displayedColumns = Object.keys(data[0]).filter(key => key!='part_id')

      }
    },error => {
      console.log("error",error);
    })

  }



}