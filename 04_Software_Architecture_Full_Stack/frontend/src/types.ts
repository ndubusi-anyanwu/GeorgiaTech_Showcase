export enum Type {
  Bug,
  Dark,
  Dragon,
  Electric,
  Fairy,
  Fighting,
  Fire,
  Flying,
  Ghost,
  Grass,
  Ground,
  Ice,
  Normal,
  Poison,
  Psychic,
  Rock,
  Steel,
  Water,
}

export enum Temp {
  Aggressive,
  Balanced,
  Defensive,
}

type Skill = {
  name: string;
  type: boolean;
};

export type Attack = Skill & {
  damage: number;
};

export type Defense = Skill & { damageReduction: number };

export type PokemonName = {
  id?: number;
  name: string;
};

export type PokemonSummary = PokemonName & {
  template: boolean;
  wins: number;
};

export type Pokemon = PokemonName & {
  types: Type[];
  weaknesses: Type[];
  attackSkills: Attack[];
  defenseSkills: Defense[];
  spriteUrl: string;

  hp: number;
  attack: number;
  defense: number;
  specialAttack: number;
  specialDefense: number;
  speed: number;
  critRate: number;
  height: number;
  weight: number;
  category: string;
  abilities: string;
  gender: number;
};

export type BattlePokemonRequest = {
  id: string;
  temperature: Temp;
};

export type BattleResult = {
  winner: number;
  loser: number;
  comments: string[];
};

export type Battle = {
  id: number;
  isTournament: boolean;
  pokemon: any;
  battles: BattleResult[];
  background: string;
};
