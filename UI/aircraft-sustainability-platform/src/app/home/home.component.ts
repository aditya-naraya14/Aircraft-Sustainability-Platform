import { HttpClient, HttpParams } from '@angular/common/http';
import { OnInit ,AfterViewInit, Component, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { FormGroup , FormBuilder } from '@angular/forms'

export interface MyObject {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent {
  displayedColumns;
  myList;
  public manufacturerList;
  public filterForm: FormGroup

  constructor(private httpClient: HttpClient, private fb: FormBuilder) {
    this.getData();
    this.getManufacturer();
  }

  @ViewChild(MatPaginator) paginator: MatPaginator;

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.myList.filter = filterValue.trim().toLowerCase();
  }
  ngOnInit() : void{
    
    this.filterForm = this.fb.group({
      manufacturer: ['']
    })
  }

  filterFormByValue(formValue){
    let params = new HttpParams();
    console.log(formValue);
    
    for(let key of formValue)
    {
      params.set(key, formValue[key][0])
    }
    this.httpClient.get('http://localhost:8000/api/get_data/').subscribe(
      (data)=>{
        this.myList = data;
      }
    )
  }
  getData() {
    this.httpClient.get('http://localhost:8000/api/get_data').subscribe(
      (data: any[]) => {
        if (data && data.length > 0) {
          this.myList = new MatTableDataSource(data);
          this.myList.paginator = this.paginator;
          this.displayedColumns = Object.keys(data[0]).filter(
            (key) => key != 'part_id'
          );
        }
      },
      (error) => {
        console.log('error', error);
      }
    );
  }

  getManufacturer(){
    this.httpClient.get('http://localhost:8000/api/get_manufacturer').subscribe(
      (data) =>{
        console.log(data);
        this.manufacturerList = data;
      }
    )
  }
}
