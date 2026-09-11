import { Component, computed, EventEmitter, Output, signal } from '@angular/core';

interface Alumno {
  id: number;
  nombre: string;
  correo: string;
  programa: string;
  estado: 'Activo' | 'Pendiente';
}

@Component({
  selector: 'app-alumnos',
  imports: [],
  templateUrl: './alumnos.html',
  styleUrl: './alumnos.css',
})
export class Alumnos {
  @Output() readonly logout = new EventEmitter<void>();
  @Output() readonly navigate = new EventEmitter<'alumnos' | 'gestion-empresas' | 'empresas' | 'entrega'>();

  protected readonly alumnos = signal<Alumno[]>([
    { id: 1, nombre: 'Mariana Torres', correo: 'mariana.torres@co360.edu.co', programa: 'Administración de Empresas', estado: 'Activo' },
    { id: 2, nombre: 'Juan David Ruiz', correo: 'juan.ruiz@co360.edu.co', programa: 'Ingeniería de Sistemas', estado: 'Activo' },
    { id: 3, nombre: 'Sofía Hernández', correo: 'sofia.hernandez@co360.edu.co', programa: 'Contaduría Pública', estado: 'Pendiente' },
    { id: 4, nombre: 'Carlos Mendoza', correo: 'carlos.mendoza@co360.edu.co', programa: 'Mercadeo y Publicidad', estado: 'Activo' },
    { id: 5, nombre: 'Valentina Castro', correo: 'valentina.castro@co360.edu.co', programa: 'Negocios Internacionales', estado: 'Activo' },
  ]);
  protected readonly search = signal('');
  protected readonly selectedId = signal<number | null>(null);
  protected readonly editingId = signal<number | null>(null);
  protected readonly creating = signal(false);
  protected readonly confirmingDelete = signal(false);
  protected readonly actionMessage = signal('');
  protected readonly filteredAlumnos = computed(() => {
    const term = this.search().trim().toLowerCase();
    return this.alumnos().filter((alumno) =>
      `${alumno.nombre} ${alumno.correo} ${alumno.programa}`.toLowerCase().includes(term),
    );
  });

  protected onSearch(value: string): void {
    this.search.set(value);
    this.selectedId.set(null);
  }

  protected selectAlumno(id: number): void {
    this.selectedId.set(id);
    this.confirmingDelete.set(false);
    this.actionMessage.set('');
  }

  protected addAlumno(): void {
    this.creating.set(true);
    this.editingId.set(null);
    this.confirmingDelete.set(false);
    this.actionMessage.set('');
  }

  protected editSelected(): void {
    this.editingId.set(this.selectedId());
    this.actionMessage.set('');
  }

  protected cancelEdit(): void { this.editingId.set(null); }
  protected cancelCreate(): void { this.creating.set(false); }

  protected createAlumno(nombre: string, correo: string, programa: string): void {
    const id = Math.max(0, ...this.alumnos().map((alumno) => alumno.id)) + 1;
    this.alumnos.update((alumnos) => [...alumnos, { id, nombre, correo, programa, estado: 'Activo' }]);
    this.creating.set(false);
    this.actionMessage.set('Estudiante agregado correctamente.');
  }

  protected saveAlumno(id: number, nombre: string, correo: string, programa: string): void {
    this.alumnos.update((alumnos) => alumnos.map((alumno) =>
      alumno.id === id ? { ...alumno, nombre, correo, programa } : alumno,
    ));
    this.editingId.set(null);
    this.actionMessage.set('Estudiante actualizado correctamente.');
  }

  protected deleteSelected(): void {
    this.confirmingDelete.set(true);
  }

  protected cancelDelete(): void { this.confirmingDelete.set(false); }

  protected confirmDelete(): void {
    const selectedId = this.selectedId();
    if (selectedId === null) return;
    this.alumnos.update((alumnos) => alumnos.filter((alumno) => alumno.id !== selectedId));
    this.selectedId.set(null);
    this.confirmingDelete.set(false);
    this.actionMessage.set('Estudiante eliminado correctamente.');
  }

  protected closeSession(): void {
    this.logout.emit();
  }

  protected openSection(section: 'alumnos' | 'gestion-empresas' | 'empresas' | 'entrega'): void { this.navigate.emit(section); }
}
