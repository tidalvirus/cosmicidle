# Cosmic Idle
Simple Idle Game - Space Themed

> [!WARNING]
> Very much a work in progress at this time.

## Game Outline:
* Gather resources
* Build ships from resources
* Gain technologies
* To explore the galaxy/universe
* Build empire

## How to run:
```
git clone https://github.com/tidalvirus/cosmicidle.git
cd cosmicidle
uv run main.py
```

## List of things to do:

- [x] Gather resources manually - DONE
- [ ] Technology Tree System - IN PROGRESS - can unlock technologies
 - [x] Technology for energy - DONE
 - [x] Technology for automators - DONE
 - [ ] Technology for ships - TODO
 - [ ] Technology for exploration - TODO
 - [ ] Technology for terraforming - TODO
 - [ ] Technology for empire - TODO
- [ ] Increase speed of resource collection - TODO


## Other notes:
Each planet in the empire will not consume resources after initial cost

There will be no combat

Technologies:
* Automators - resources, ships, exploration, empire building
* Ships - explore, empire building
* Terraforming - empire building

Goals:
* Get all the resources, explore all the planets/solar systems, 

Resources:
* Resources will be needed for every action. Resources will be infinite
* Resources will be generic: Metal, Minerals, Energy
* Energy will be: wood/oil/gas/solar/fission/fusion - but maybe will never be split out like that, and will just be simply 'energy'
* Start with metal and mineral resources, manual gathering, to then build an energy creation system.

Rough mermaid diagram:
```mermaid
flowchart TD
planet["Initial Planet"]
planet --> Resources
Resources --> Technology
Technology --> Resources
Technology --> Ships
Technology --> Exploration
Resources --> Ships
Resources --> Exploration
Resources <--> Empire
Ships --> Empire
Exploration --> Empire
```

Crazy diagram for initial tech tree:
```mermaid
flowchart LR

Ships --> Exploration --> Terraform --> Empire

Metals -- 50 --> Energy
Metals -- 500 --> Ships
Metals -- 5000 --> Exploration
Metals -- 50000 --> Terraform
Metals -- 500000 --> Empire
Minerals -- 50 --> Energy
Minerals -- 500 --> Ships
Minerals -- 5000 --> Exploration
Minerals -- 50000 --> Terraform
Minerals -- 500000 --> Empire

Energy -- 500 --> Ships
Energy -- 5000 --> Exploration
Energy -- 50000 --> Terraform
Energy -- 500000 --> Empire

Energy -- 50 --> Automators
Minerals -- 50 --> Automators
Metals -- 50 --> Automators
```