import { CSSProperties } from 'react';

const spriteStyle: CSSProperties = {
  position: 'absolute',
  bottom: 48,
  width: 128,
  height: 128,
  transition: 'bottom 0.4s',
};

type PokeSpriteProps = {
  active?: boolean;
  side: 'left' | 'right';
  url: string;
};

const PokeSprite = ({ active, side, url }: PokeSpriteProps) => (
  <img
    style={{
      ...spriteStyle,
      [side]: 32,
      ...(active ? { bottom: 96 } : {}),
      ...(side === 'left' ? { transform: 'scaleX(-1)' } : {}),
    }}
    src={url}
  />
);

export default PokeSprite;
