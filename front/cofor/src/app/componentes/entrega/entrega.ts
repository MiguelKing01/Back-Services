import { Component, computed, EventEmitter, Output, signal } from '@angular/core';

interface EntregaItem { id: number; nombre: string; fechaCierre: string; descripcion: string; }

@Component({ selector: 'app-entrega', imports: [], templateUrl: './entrega.html', styleUrl: './entrega.css' })
export class Entrega {
  @Output() readonly logout = new EventEmitter<void>();
  @Output() readonly navigate = new EventEmitter<'alumnos' | 'gestion-empresas' | 'empresas' | 'entrega'>();
  protected readonly entregas = signal<EntregaItem[]>([
    { id: 1, nombre: 'Informe de práctica empresarial', fechaCierre: '2026-09-20', descripcion: 'Presenta el informe de avance de la práctica empresarial.' },
    { id: 2, nombre: 'Plan de trabajo', fechaCierre: '2026-09-18', descripcion: 'Carga el plan de trabajo aprobado por la empresa.' },
    { id: 3, nombre: 'Evidencia de seguimiento', fechaCierre: '2026-09-25', descripcion: 'Adjunta las evidencias del seguimiento semanal.' },
  ]);
  protected readonly search = signal('');
  protected readonly selectedId = signal<number | null>(null);
  protected readonly editingId = signal<number | null>(null);
  protected readonly creating = signal(false);
  protected readonly confirmingDelete = signal(false);
  protected readonly message = signal('');
  protected readonly filteredEntregas = computed(() => {
    const term = this.search().trim().toLowerCase();
    return this.entregas().filter((item) => `${item.nombre} ${item.fechaCierre} ${item.descripcion}`.toLowerCase().includes(term));
  });
  protected onSearch(value: string): void { this.search.set(value); this.selectedId.set(null); this.confirmingDelete.set(false); }
  protected selectEntrega(id: number): void { this.selectedId.set(id); this.confirmingDelete.set(false); this.message.set(''); }
  protected addEntrega(): void { this.creating.set(true); this.editingId.set(null); this.confirmingDelete.set(false); this.message.set(''); }
  protected cancelCreate(): void { this.creating.set(false); }
  protected createEntrega(nombre: string, fechaCierre: string, descripcion: string): void {
    const id = Math.max(0, ...this.entregas().map((item) => item.id)) + 1;
    this.entregas.update((items) => [...items, { id, nombre, fechaCierre, descripcion }]);
    this.creating.set(false); this.message.set('Entrega agregada correctamente.');
  }
  protected editSelected(): void { this.editingId.set(this.selectedId()); this.message.set(''); }
  protected cancelEdit(): void { this.editingId.set(null); }
  protected saveEntrega(id: number, nombre: string, fechaCierre: string, descripcion: string): void {
    this.entregas.update((items) => items.map((item) => item.id === id ? { ...item, nombre, fechaCierre, descripcion } : item));
    this.editingId.set(null); this.message.set('Entrega actualizada correctamente.');
  }
  protected deleteSelected(): void { if (this.selectedId() !== null) this.confirmingDelete.set(true); }
  protected cancelDelete(): void { this.confirmingDelete.set(false); }
  protected confirmDelete(): void {
    const id = this.selectedId(); if (id === null) return;
    this.entregas.update((items) => items.filter((item) => item.id !== id));
    this.selectedId.set(null); this.confirmingDelete.set(false); this.message.set('Entrega eliminada correctamente.');
  }
  protected openSection(section: 'alumnos' | 'gestion-empresas' | 'empresas' | 'entrega'): void { this.navigate.emit(section); }
  protected closeSession(): void { this.logout.emit(); }
}
