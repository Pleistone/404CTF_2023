# La Folie du jeu : descente aux enfers

**Difficulté** : Facile

## Enoncé

_Disclaimer : Vous ne devez, en aucun cas, utiliser vos fonds personnels pour résoudre les challenges de web3. Il n'est pas nécessaire de posséder des cryptomonnaies pour lancer les challenges, intéragir avec ou les valider. (Il est aussi inutile de soudoyer les concepteurs des challenges) Cordialement La trésorerie_

Narrativement, ce challenge vient avant "La folie du jeu : D'esclave à maître" cependant il n'est pas nécessaire de faire celui-ci pour faire le second. Nous vous conseillons néanmoins de lire l'énoncé de ce challenge pour comprendre le contexte. Alors que vous étiez assis à une table du café Le Procope, vos pensées furent interrompues par l'apparition de la magnifique Marguerite Gauthier. Son regard était aussi pénétrant que ses courbes gracieuses, et son air empreint d'un charme envoûtant ne laissait aucun doute quant à sa nature exceptionnelle.

Elle s'approcha de vous avec grâce, ses pas silencieux comme une promesse d'aventure. Elle vous confia alors les affres qui tourmentaient son âme : c'était à cause d'elle qu'Armand Duval était pris dans une spirale d'addiction aux jeux d'argent qui le détruisait.

Ce n'était pas n'importe quels jeux d'argent qui retenaient Armand prisonnier de leurs charmes sournois. Non, il s'était épris des loteries établies sur la blockchain Ethereum, ces jeux impitoyables où l'espoir et le désespoir se côtoyaient sans relâche, tels des amants inséparables. Ainsi, les dés étaient jetés, et la danse avec le destin commençait. Vous alliez donc vous plonger dans cet univers énigmatique de la blockchain Ethereum, où les paris étaient éternels et les gains fugaces. Pour Marguerite, vous braveriez les tourments, manipuleriez les nombres et les probabilités avec habileté, cherchant à renverser le cours du destin et à redonner à Armand Duval une chance de s'échapper des griffes implacables du jeu.

Les tasses de café fumaient encore devant vous, tandis que vous vous prépariez à affronter les défis à venir. Marguerite vous observait avec un mélange d'inquiétude et d'espoir dans ses yeux. Vous aviez maintenant un objectif commun : sauver l'âme tourmentée d'Armand et lui offrir une nouvelle vie.

Gagnez à la roulette décrite dans le contrat ci-joint.


## Solution

Dans ce défi, on nous donne le code Solidity ci-dessous : 
```Solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

contract Jeu {
    bool public isSolved = false;
    uint public m = 0x7fffffff;
    uint public a = 12345;
    uint public c = 1103515245;

    uint private currentState;

    constructor(uint _start) {
        currentState = _start;
    }

    function guess(uint _next) public returns (bool) {
        currentState = (a * currentState + c) % m;
        isSolved = (_next == currentState) || isSolved;
        return isSolved;
    }
```

Dans ce code, on voit que le contrat est initialisé la valeur _start passer en entrée du constructeur : 


<p align="center"><img src="Constructor Arguments.png" alt="Constructor Arguments" width="1000"></p>


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{r4Nd0Mn3ss_1S_NOt_s0_345y}
```
