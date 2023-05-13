import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
import { environment } from 'src/environments/environment';
import { Observable, Subject } from 'rxjs';
import { LOGIN_DETAILS } from '../common/app-constant';
import { UserDetails, UserDetailsRequest, UserDetailsResponse } from '../model/user-model';


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  
  private static LOGIN_DETAILS_API = environment.serverApiUrl + LOGIN_DETAILS;

  // public userDetails = new BehaviorSubject<UserDetailsResponse>(null);
  // userDetails$ = this.userDetails.asObservable();

  // private test = new BehaviorSubject(null);

  constructor(private httpClient: HttpClient) {

  }

  public loginDetails(userDetailsRequest: UserDetailsRequest) {
    return this.httpClient.post(AuthService.LOGIN_DETAILS_API, userDetailsRequest);
  }


}
