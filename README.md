<p align="center">
  <img src="titulo.svg" alt="Los Caballeros del Zodiaco: práctica de clases en Python" width="100%">
</p>

Práctica de **programación orientada a objetos** en Python: clases, herencia, métodos y relación entre clases, usando personajes de Los Caballeros del Zodiaco.

## Descripción

Todos los personajes son un `Guerrero`. De él heredan los caballeros, los espectros y los dioses, y los caballeros se dividen en Bronce y Oro. Cada guerrero puede tener varios ataques, que se guardan en una lista.

## Clases

| Clase | Hereda de | Atributos | Métodos |
|---|---|---|---|
| `Ataque` | - | `nombre`, `herida` | `mostrar_info()` |
| `Guerrero` | - | `nombre`, `cosmo`, `edad`, `ataques` | `mostrar_info()`, `anadir_ataque()`, `mostrar_ataques()` |
| `Caballero` | `Guerrero` | `armadura`, `constelacion` | `equiparse()` |
| `Espectro` | `Guerrero` | `sobrepelliz`, `estrella` | `equiparse()` |
| `Dios` | `Guerrero` | `reino` | `gobernar()` |
| `CaballeroDeBronce` | `Caballero` | `maestro` | `entrenar()`, `mostrar_info()` |
| `CaballeroDeOro` | `Caballero` | `casa`, `signo`, `septimosentido` | `mostrar_info()`, `mostrar_septimosentido()` |

**Herencia ("es un"):** un `Caballero` es un `Guerrero`, y un `CaballeroDeOro` es un `Caballero`. Las clases hijas usan `super().__init__()` para reutilizar los atributos del padre.

**Relación ("tiene"):** un `Guerrero` tiene de 1 a muchos `Ataque`.

## Personajes

- **Caballeros de Bronce:** Seiya, Shiryu, Hyoga, Shun e Ikki
- **Caballeros de Oro:** Mu, Aioria, Shaka y Afrodita
- **Espectros:** Radamanthys, Minos y Éaco
- **Dioses:** Hades y Atenea

  <img width="420" height="500" alt="caballeros-zodiaco" src="https://github.com/user-attachments/assets/1e7685c4-9d3c-453e-85fb-0ff714e9ac67" />


Todos los personajes se guardan en una lista y se recorren con un `for`, mostrando sus datos y sus ataques.

## Ejecución

Requisitos: Python 3.

```bash
python main.py
```

## Ejemplo de salida

```
--- Seiya ---
Maestro: Marin
Ataque: Meteoros de Pegaso 25

--- Afrodita ---
Casa: Casa de Piscis | Signo: Piscis
Ataque: Rosas Pirañas 30

--- Radamanthys ---
Nombre: Radamanthys | Cosmo: 150 | Edad: 30
Ataque: Gran Precaución 42
```

## Diagrama de clases

<img width="752" height="516" alt="PPO Caballeros del Zodiaco  drawio" src="https://github.com/user-attachments/assets/13753893-cd3f-425c-8bf9-4ca479f13427" />

[Diagrama draw.io](https://app.diagrams.net/#G1EtyxKHGZGf_ZtGiLtHdrhu-tMpYtURci#%7B%22pageId%22%3A%22kgbmIMx4C_ldpACMlDbA%22%7D)

## Autora

<img src="logo.png" alt="Logo de Beatriz Iñiguez Cascales" width="120">

**Beatriz Iñiguez Cascales**
