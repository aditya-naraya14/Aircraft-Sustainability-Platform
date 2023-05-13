import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './serivces/auth.service';
import { UserDetails } from './model/user-model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'project';

  constructor(private router: Router, private authService: AuthService) {
    console.log("In app component");
    let userDetails: string = localStorage.getItem("userDetails");
    console.log("UserId", userDetails);
    if (userDetails == 'SUCCESS') {
      console.log("when userId exist");
      // this.authService.userDetails.next(userDetails);
      this.router.navigate(['/home']);
    }
    else {
      console.log("when userId not exist");
      this.router.navigate(['/login']);
    }
  }
}
