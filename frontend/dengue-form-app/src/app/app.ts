import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { DengueFormComponent } from './dengue-form/dengue-form';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, DengueFormComponent],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = signal('dengue-form-app');
}
