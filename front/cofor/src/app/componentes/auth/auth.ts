import { Component, EventEmitter, Output, signal } from '@angular/core';

@Component({
  selector: 'app-auth',
  imports: [],
  templateUrl: './auth.html',
  styleUrl: './auth.css',
})
export class Auth {
  @Output() readonly createAccount = new EventEmitter<void>();
  @Output() readonly loginSuccess = new EventEmitter<void>();

  protected readonly showPassword = signal(false);
  protected readonly submitted = signal(false);

  protected togglePassword(): void {
    this.showPassword.update((visible) => !visible);
  }

  protected login(): void {
    this.submitted.set(true);
    this.loginSuccess.emit();
  }

  protected openRegistration(): void {
    this.createAccount.emit();
  }

}
