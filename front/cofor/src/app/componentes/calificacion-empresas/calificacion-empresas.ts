import { Component, EventEmitter, Output } from '@angular/core';

interface EmpresaCalificada {
  nombre: string;
  sector: string;
  calificacion: number;
  imagen: string;
}

@Component({
  selector: 'app-calificacion-empresas',
  imports: [],
  templateUrl: './calificacion-empresas.html',
  styleUrl: './calificacion-empresas.css',
})
export class CalificacionEmpresas {
  @Output() readonly logout = new EventEmitter<void>();
  @Output() readonly navigate = new EventEmitter<'alumnos' | 'gestion-empresas' | 'empresas' | 'entrega'>();

  protected readonly empresas: EmpresaCalificada[] = [
    { nombre: 'Grupo Andino S.A.S.', sector: 'Servicios empresariales', calificacion: 4.8, imagen: 'https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=900&q=80' },
    { nombre: 'Tecnología Integral', sector: 'Tecnología', calificacion: 4.6, imagen: 'https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=900&q=80' },
    { nombre: 'Comercializadora Nova', sector: 'Comercio', calificacion: 4.4, imagen: 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=900&q=80' },
    { nombre: 'Soluciones Logísticas', sector: 'Logística', calificacion: 4.7, imagen: 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=900&q=80' },
  ];

  protected stars(rating: number): string[] {
    return Array.from({ length: 5 }, (_, index) => index < Math.round(rating) ? '★' : '☆');
  }

  protected openSection(section: 'alumnos' | 'gestion-empresas' | 'empresas' | 'entrega'): void { this.navigate.emit(section); }
  protected closeSession(): void { this.logout.emit(); }
}
