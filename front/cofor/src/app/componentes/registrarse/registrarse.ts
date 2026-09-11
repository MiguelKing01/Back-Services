import { Component, EventEmitter, Output, signal } from '@angular/core';

@Component({
  selector: 'app-registrarse',
  imports: [],
  templateUrl: './registrarse.html',
  styleUrl: './registrarse.css',
})
export class Registrarse {
  @Output() readonly goToLogin = new EventEmitter<void>();

  protected readonly showPassword = signal(false);
  protected readonly passwordsDoNotMatch = signal(false);

  protected togglePassword(): void {
    this.showPassword.update((visible) => !visible);
  }

  protected register(password: string, confirmation: string): void {
    this.passwordsDoNotMatch.set(password !== confirmation);

    if (password === confirmation) {
      this.goToLogin.emit();
    }
  }

  protected returnToLogin(): void {
    this.goToLogin.emit();
  }
}
