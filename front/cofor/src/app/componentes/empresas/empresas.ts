import { Component, computed, EventEmitter, Output, signal } from '@angular/core';

interface Empresa { id: number; nombre: string; correo: string; sector: string; estado: 'Activa' | 'Pendiente'; }

@Component({ selector: 'app-empresas', imports: [], templateUrl: './empresas.html', styleUrl: './empresas.css' })
export class Empresas {
  @Output() readonly logout = new EventEmitter<void>();
  @Output() readonly navigate = new EventEmitter<'alumnos' | 'gestion-empresas' | 'empresas' | 'entrega'>();
  protected readonly empresas = signal<Empresa[]>([
    { id: 1, nombre: 'Grupo Andino S.A.S.', correo: 'contacto@grupoandino.co', sector: 'Servicios empresariales', estado: 'Activa' },
    { id: 2, nombre: 'Tecnología Integral', correo: 'talento@tecnologiaintegral.co', sector: 'Tecnología', estado: 'Activa' },
    { id: 3, nombre: 'Comercializadora Nova', correo: 'alianzas@nova.co', sector: 'Comercio', estado: 'Pendiente' },
    { id: 4, nombre: 'Soluciones Logísticas', correo: 'gestion@solucioneslogisticas.co', sector: 'Logística', estado: 'Activa' },
  ]);
  protected readonly search = signal('');
  protected readonly selectedId = signal<number | null>(null);
  protected readonly editingId = signal<number | null>(null);
  protected readonly creating = signal(false);
  protected readonly confirmingDelete = signal(false);
  protected readonly message = signal('');
  protected readonly filteredEmpresas = computed(() => {
    const term = this.search().trim().toLowerCase();
    return this.empresas().filter((empresa) => `${empresa.nombre} ${empresa.correo} ${empresa.sector}`.toLowerCase().includes(term));
  });
  protected onSearch(value: string): void { this.search.set(value); this.selectedId.set(null); }
  protected selectEmpresa(id: number): void { this.selectedId.set(id); this.confirmingDelete.set(false); this.message.set(''); }
  protected editSelected(): void { this.editingId.set(this.selectedId()); }
  protected cancelEdit(): void { this.editingId.set(null); }
  protected cancelCreate(): void { this.creating.set(false); }
  protected createEmpresa(nombre: string, correo: string, sector: string): void {
    const id = Math.max(0, ...this.empresas().map((empresa) => empresa.id)) + 1;
    this.empresas.update((empresas) => [...empresas, { id, nombre, correo, sector, estado: 'Activa' }]);
    this.creating.set(false); this.message.set('Empresa agregada correctamente.');
  }
  protected saveEmpresa(id: number, nombre: string, correo: string, sector: string): void {
    this.empresas.update((empresas) => empresas.map((empresa) => empresa.id === id ? { ...empresa, nombre, correo, sector } : empresa));
    this.editingId.set(null); this.message.set('Empresa actualizada correctamente.');
  }
  protected addEmpresa(): void { this.creating.set(true); this.editingId.set(null); this.confirmingDelete.set(false); this.message.set(''); }
  protected deleteSelected(): void { if (this.selectedId() !== null) this.confirmingDelete.set(true); }
  protected cancelDelete(): void { this.confirmingDelete.set(false); }
  protected confirmDelete(): void { const id = this.selectedId(); if (id === null) return; this.empresas.update((empresas) => empresas.filter((empresa) => empresa.id !== id)); this.selectedId.set(null); this.confirmingDelete.set(false); this.message.set('Empresa eliminada correctamente.'); }
  protected openSection(section: 'alumnos' | 'gestion-empresas' | 'empresas' | 'entrega'): void { this.navigate.emit(section); }
  protected closeSession(): void { this.logout.emit(); }
}
