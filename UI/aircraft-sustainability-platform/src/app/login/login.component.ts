import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { AuthService } from '../serivces/auth.service';
import { HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';
import { UserDetailsRequest, UserDetailsResponse } from '../model/user-model';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  private subscription: Subscription
  loginForm: FormGroup;

  constructor(private router: Router, private authService: AuthService, private formBuilder: FormBuilder) {
    this.subscription = new Subscription();
  }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      userName: ['', [Validators.required, Validators.maxLength(15), Validators.minLength(5)]],
      password: ['', Validators.required]
    });
  }

  onNext() {
    // let userDetailsRequest = new UserDetailsRequest();
    // userDetailsRequest.userName = this.loginForm.value.userName;
    // userDetailsRequest.password = this.loginForm.value.password;

    // this.authService.loginDetails(userDetailsRequest)
    //   .subscribe((res: string) => {
    //     if (res == 'SUCCESS') {
    //       localStorage.setItem("userDetails", "SUCCESS");
    //       // this.authService.userDetails.next(userDetails);
    //       this.router.navigate(['/home']);
    //     } else {
    //       console.log("Error" + "login failed");
    //       alert('Invalid');
    //     }
    //   },
    //     (err: HttpErrorResponse) => {
    //       console.log("Error" + JSON.stringify(err.error.message));
    //       alert('Invalid');
    //     });



    let userDetailsRequest = new UserDetailsRequest();
    let uname = this.loginForm.value.userName;
    let pass = this.loginForm.value.password;

    if (uname == 'admin' && pass == "password") {
      localStorage.setItem("userDetails", "SUCCESS");
      // this.authService.userDetails.next(userDetails);
      this.router.navigate(['/home']);
    } else {
      console.log("Error" + "login failed");
      alert('Invalid');
    }

  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}
