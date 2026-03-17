import { array, boolean, number, object, string } from 'yup';
import { Pokemon, Type } from '../../../types';

export const initialValues: Pokemon = {
  name: '',
  types: [],
  weaknesses: [],
  attackSkills: [],
  defenseSkills: [],

  spriteUrl: '',

  hp: 25,
  attack: 0,
  defense: 0,
  specialAttack: 0,
  specialDefense: 0,
  speed: 0,
  critRate: 0.0,
  height: 0.0,
  weight: 0.0,
  category: '',
  abilities: '',
  gender: 0,
};

export const schema = object({
  name: string().required(),
  types: array(number()),
  weaknesses: array(number()),
  attackSkills: array(
    object({
      name: string().required('name is a required field'),
      type: boolean().required(),
      damage: number()
        .required('damage is a required field')
        .positive('damage must be a positive integer')
        .integer('damage must be an integer'),
    })
  ),
  defenseSkills: array(
    object({
      name: string().required('name is a required field'),
      type: boolean().required(),
      damageReduction: number()
        .required('damage reduction is a required field')
        .positive('damage reduction must be a positive integer')
        .integer('damage reduction must be an integer'),
    })
  ),

  hp: number().required().positive().integer(),
  attack: number().positive().integer(),
  defense: number().positive().integer(),
  specialAttack: number().positive().integer(),
  specialDefense: number().positive().integer(),
  speed: number().positive().integer(),
  critRate: number().positive(),
  height: number().positive(),
  weight: number().positive(),
  category: string(),
  abilities: string(),
  gender: number().oneOf([0, 1, 2]),
});

export const types = Object.keys(Type).filter((key) =>
  Number.isNaN(parseInt(key))
);

const typeToWeaknesses = {
  [Type.Bug]: [Type.Fire, Type.Flying, Type.Rock],
  [Type.Dark]: [Type.Bug, Type.Fairy, Type.Fighting],
  [Type.Dragon]: [Type.Dragon, Type.Fairy, Type.Ice],
  [Type.Electric]: [Type.Ground],
  [Type.Fairy]: [Type.Poison, Type.Steel],
  [Type.Fighting]: [Type.Fairy, Type.Flying, Type.Psychic],
  [Type.Fire]: [Type.Ground, Type.Rock, Type.Water],
  [Type.Flying]: [Type.Electric, Type.Ice, Type.Rock],
  [Type.Ghost]: [Type.Dark, Type.Ghost],
  [Type.Grass]: [Type.Bug, Type.Fire, Type.Flying, Type.Ice, Type.Poison],
  [Type.Ground]: [Type.Grass, Type.Ice, Type.Water],
  [Type.Ice]: [Type.Fighting, Type.Fire, Type.Rock, Type.Steel],
  [Type.Normal]: [Type.Fighting],
  [Type.Poison]: [Type.Ground, Type.Psychic],
  [Type.Psychic]: [Type.Bug, Type.Dark, Type.Ghost],
  [Type.Rock]: [Type.Fighting, Type.Grass, Type.Ground, Type.Steel, Type.Water],
  [Type.Steel]: [Type.Fire, Type.Fighting, Type.Ground],
  [Type.Water]: [Type.Electric, Type.Grass],
};

export const getWeaknesses = (types: Type[]): Type[] => {
  return [
    ...new Set(
      types.reduce(
        (weaknesses, currType) => [
          ...weaknesses,
          ...typeToWeaknesses[currType],
        ],
        [] as Type[]
      )
    ),
  ].sort((a, b) => a - b);
};
