export interface Exercise {
  readonly id?: number;
  name: string;
  description: string;
  silent: boolean;
  equipment: boolean;
  type: string;
  author: number;
}
