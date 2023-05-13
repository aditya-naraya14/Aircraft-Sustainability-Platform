export class UserDetailsResponse {
    userId?: number;
    userName?: string;
    userType?: string;
}

export class UserDetailsRequest {
    userName?: string;
    password?: string;
}


export class UserDetails {
    userId?: number;
    userName?: string;
    password?: string;
    emailId?: string;
    createdTs?: Date;
    modifiedTs?: Date;
    userType?: string;
    lastLogon?: Date;
    isEnabled?: boolean;
}