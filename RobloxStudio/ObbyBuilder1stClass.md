# 🎮 Mon Obby Builder — Guide du jour

Aujourd'hui on construit notre propre parcours (obby) dans Roblox Studio ! On va apprendre à :
1. Placer des blocs pour construire le parcours
2. Faire des blocs pièges qui **tuent**
3. Faire des blocs qui **disparaissent** après un moment

Tu n'as pas besoin de tout comprendre par cœur, juste de copier le bon code au bon endroit et de voir ce qui se passe ! 🚀

---

## 1️⃣ Placer des Parts (les blocs de base)

Pas de code pour ça, juste des clics :

1. En haut, clique sur **Home** puis sur **Part** → un bloc apparaît
2. Utilise l'outil **Move** (flèches) pour le déplacer
3. Utilise l'outil **Scale** pour l'agrandir ou le rétrécir
4. Clique sur ton bloc → dans **Properties** à droite, coche **Anchored** ✅
   → Sinon ton bloc va tomber à cause de la gravité !
5. Tu peux changer sa couleur avec **Color** dans les Properties

💡 **Astuce** : anchore TOUJOURS tes blocs de plateforme, sinon ils tombent dans le vide !

---

## 2️⃣ Le bloc piège qui tue 💀

**Où le mettre :**
1. Clique sur ton bloc piège dans **Explorer**
2. Clique sur le **+** qui apparaît → cherche **Script** → clique dessus
3. Un script s'ouvre avec du texte bleu déjà écrit dedans (`print("Hello world!")`)
4. **Efface tout** et colle le code ci-dessous

```lua
local part = script.Parent -- le bloc piège, c'est celui où on a mis le script

part.Touched:Connect(function(hit)
    local humanoid = hit.Parent:FindFirstChild("Humanoid")
    if humanoid then
        humanoid.Health = 0 -- on met la vie à 0 = le joueur meurt
    end
end)
```

**Ce que ça fait, ligne par ligne :**
- `script.Parent` → c'est le bloc lui-même (le parent du script)
- `part.Touched:Connect(...)` → "quand quelque chose touche ce bloc, fais ceci"
- `hit` → c'est le morceau qui a touché le bloc (souvent une jambe ou un bras du joueur)
- `hit.Parent:FindFirstChild("Humanoid")` → on cherche si c'est bien un joueur (les joueurs ont un "Humanoid")
- `humanoid.Health = 0` → on tue le joueur en mettant sa vie à zéro

🎨 **Astuce déco** : mets ton bloc piège en rouge et en matériau "Neon" pour que ce soit clair que c'est dangereux !

---

## 3️⃣ Le bloc qui disparaît ⏳

Même méthode : clique sur le bloc → **+** → **Script** → efface tout → colle ce code :

```lua
local part = script.Parent
local dejaTouche = false -- pour ne pas répéter l'action plusieurs fois d'affilée

part.Touched:Connect(function(hit)
    if dejaTouche then return end -- si c'est déjà en train de disparaître, on ne fait rien
    dejaTouche = true

    wait(1) -- attend 1 seconde après avoir été touché

    part.Transparency = 1   -- le bloc devient invisible
    part.CanCollide = false -- on peut passer à travers (tomber)

    wait(2) -- reste invisible pendant 2 secondes

    part.Transparency = 0  -- le bloc redevient visible
    part.CanCollide = true -- on ne peut plus passer à travers

    dejaTouche = false -- on remet à zéro pour la prochaine fois
end)
```

**Ce que ça fait, ligne par ligne :**
- `dejaTouche` → une mémoire pour savoir si le bloc est déjà en train de disparaître
- `wait(1)` → le jeu attend 1 seconde avant de continuer
- `Transparency = 1` → rend le bloc invisible (0 = visible, 1 = invisible)
- `CanCollide = false` → le joueur tombe à travers le bloc, comme s'il n'existait plus
- Ensuite le bloc réapparaît après 2 secondes

💡 **Astuce** : change les chiffres dans `wait(...)` pour rendre ton piège plus facile ou plus difficile !

---

## 4️⃣ Les checkpoints (pour ne pas recommencer au début !)

C'est le plus simple de tous, **pas besoin de code** :

1. Clique sur **Home** → cherche **SpawnLocation** (parfois caché dans le menu déroulant à côté de Part)
2. Place-le sur ta plateforme, à l'endroit où tu veux un checkpoint
3. Anchore-le (comme d'habitude)
4. C'est tout ! Quand un joueur le touche, il réapparaîtra ici s'il meurt, au lieu de recommencer tout au début

💡 **Astuce** : mets plusieurs SpawnLocation le long de ton parcours, un par étape difficile.

**Pour aller plus loin (avec un peu de code)** : si tu veux que le checkpoint change de couleur quand il est activé, ajoute un Script dans ton SpawnLocation :

```lua
local checkpoint = script.Parent

checkpoint.Touched:Connect(function(hit)
    local player = game.Players:GetPlayerFromCharacter(hit.Parent)
    if player then
        checkpoint.Color = Color3.fromRGB(0, 255, 0) -- devient vert = activé !
    end
end)
```

---

## 💀 D'autres idées de pièges (si tu as fini en avance)

### Le piège qui téléporte au checkpoint
Au lieu de tuer, il renvoie juste au dernier checkpoint.
```lua
local part = script.Parent

part.Touched:Connect(function(hit)
    local humanoid = hit.Parent:FindFirstChild("Humanoid")
    if humanoid then
        humanoid.Health = 0 -- le joueur meurt et réapparaît automatiquement au dernier checkpoint
    end
end)
```
(C'est en fait le même code que le piège qui tue — mais si tu as bien mis des checkpoints, l'effet est différent : le joueur ne repart plus du tout début !)

### Le piège qui pousse (catapulte)
```lua
local part = script.Parent

part.Touched:Connect(function(hit)
    local root = hit.Parent:FindFirstChild("HumanoidRootPart")
    if root then
        root.Velocity = Vector3.new(0, 80, 0) -- envoie le joueur en l'air !
    end
end)
```
Change les chiffres `(0, 80, 0)` pour pousser dans une autre direction (le 1er = gauche/droite, le 2e = hauteur, le 3e = avant/arrière).

### Le piège clignotant (prévient avant de tuer)
```lua
local part = script.Parent

while true do
    wait(1)
    part.Color = Color3.fromRGB(255, 255, 0) -- jaune = attention !
    wait(1)
    part.Color = Color3.fromRGB(255, 0, 0) -- rouge = danger, ne pas toucher maintenant
end
```
Combine-le avec le script du piège qui tue pour un effet "feu de circulation" 🚦

### Le piège glissant (sans code !)
Clique sur ton bloc → dans Properties, change **Material** en **Ice**. Le joueur glissera dessus, parfait juste avant un trou ou un piège !

---

## 🏆 Défi bonus

Essaie de :
- Faire une rangée de blocs qui disparaissent chacun leur tour
- Changer la couleur du bloc piège juste avant qu'il tue (pour prévenir le joueur)
- Combiner les deux : un bloc qui tue ET qui disparaît

Bon courage, et amuse-toi bien à piéger tes amis ! 😈