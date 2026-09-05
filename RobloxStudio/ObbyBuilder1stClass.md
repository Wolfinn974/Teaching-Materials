# 🎮 Mon Obby Builder — Guide du jour

Aujourd'hui on construit notre propre parcours (obby) dans Roblox Studio ! On va apprendre à :
1. Placer des blocs pour construire le parcours
2. Faire des blocs pièges qui **tuent**
3. Faire des blocs qui **disparaissent** après un moment
4. Faire des blocs qui **bougent, tournent et font du bruit** 🎵

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

## 5️⃣ La plateforme qui tourne 🔄

Une plateforme qui tourne sur elle-même en boucle — un grand classique des obbys !

```lua
local part = script.Parent

while true do
    part.CFrame = part.CFrame * CFrame.Angles(0, math.rad(2), 0)
    wait()
end
```

**Ce que ça fait, ligne par ligne :**
- `while true do ... end` → une boucle qui ne s'arrête JAMAIS, elle répète le code à l'intérieur pour toujours
- `CFrame` → c'est la position ET l'orientation (rotation) d'un bloc, tout en un
- `CFrame.Angles(0, math.rad(2), 0)` → "tourne un tout petit peu (2 degrés) sur l'axe du milieu (la hauteur)"
- `part.CFrame = part.CFrame * ...` → "prends la position/rotation actuelle, et ajoute cette petite rotation par-dessus"
- `wait()` → une toute petite pause (sans elle, le jeu tournerait trop vite et planterait)

💡 **Astuce** : change le `2` pour une plus grande valeur (ex: `10`) pour une rotation plus rapide, ou change le `0, math.rad(2), 0` en `math.rad(2), 0, 0` pour tourner dans une autre direction !

⚠️ Cette plateforme peut rester **Anchored** — pas besoin de la désancrer pour la faire tourner.

---

## 6️⃣ La plateforme qui va et vient 🔁

Une plateforme qui glisse d'un point à un autre, en boucle, pour un passage plus difficile.

```lua
local TweenService = game:GetService("TweenService")
local part = script.Parent

local pointDepart = part.Position
local pointArrivee = pointDepart + Vector3.new(10, 0, 0) -- se déplace de 10 studs sur le côté

local infoDeplacement = TweenInfo.new(2, Enum.EasingStyle.Linear)

while true do
    local aller = TweenService:Create(part, infoDeplacement, {Position = pointArrivee})
    aller:Play()
    aller.Completed:Wait()

    local retour = TweenService:Create(part, infoDeplacement, {Position = pointDepart})
    retour:Play()
    retour.Completed:Wait()
end
```

**Ce que ça fait, ligne par ligne :**
- `TweenService` → un outil de Roblox qui fait bouger les choses **en douceur** (pas d'un coup sec)
- `pointDepart` et `pointArrivee` → les deux positions entre lesquelles la plateforme va faire l'aller-retour
- `TweenInfo.new(2, ...)` → le déplacement dure 2 secondes
- `TweenService:Create(part, infoDeplacement, {Position = ...})` → crée le mouvement, mais ne le lance pas encore
- `:Play()` → lance le mouvement
- `.Completed:Wait()` → attend que le mouvement soit terminé avant de continuer le code

💡 **Astuce** : change `Vector3.new(10, 0, 0)` pour changer la direction (1er chiffre = gauche/droite, 2e = haut/bas, 3e = avant/arrière) et le `2` dans `TweenInfo.new` pour la vitesse.

---

## 7️⃣ Le bruit quand on touche un bloc 🔊

Ajoute un petit son pour donner plus de sensations à ton obby (checkpoint, piège, victoire...).

```lua
local part = script.Parent

local son = Instance.new("Sound") -- on crée un son
son.SoundId = "rbxassetid://9042809906" -- change ce numéro par l'ID d'un son de ton choix
son.Parent = part

part.Touched:Connect(function(hit)
    local humanoid = hit.Parent:FindFirstChild("Humanoid")
    if humanoid then
        son:Play()
    end
end)
```

**Ce que ça fait, ligne par ligne :**
- `Instance.new("Sound")` → crée un objet Son "à partir de rien"
- `son.SoundId = "rbxassetid://..."` → indique QUEL son jouer (chaque son a un numéro unique)
- `son.Parent = part` → place le son dans ton bloc
- `son:Play()` → joue le son quand un joueur touche le bloc

💡 **Comment trouver un ID de son** : dans la barre de recherche en haut de Roblox Studio (onglet Toolbox), cherche "jump", "victory", "alarm"... et clique sur un son pour copier son ID.

---

## 8️⃣ Le message qui s'affiche à l'écran 💬

Pour féliciter le joueur ou le prévenir d'un danger, sans avoir besoin de dessiner une interface !

```lua
local checkpoint = script.Parent

checkpoint.Touched:Connect(function(hit)
    local player = game.Players:GetPlayerFromCharacter(hit.Parent)
    if player then
        game.StarterGui:SetCore("SendNotification", {
            Title = "Checkpoint !";
            Text = "Bien joué, continue comme ça 💪";
            Duration = 3;
        })
    end
end)
```

**Ce que ça fait, ligne par ligne :**
- `game.Players:GetPlayerFromCharacter(hit.Parent)` → vérifie que c'est bien un vrai joueur (et pas un simple objet) qui a touché
- `game.StarterGui:SetCore("SendNotification", {...})` → affiche une petite notification en haut à droite de l'écran, comme une vraie notification de jeu
- `Title` / `Text` → le titre et le texte du message
- `Duration = 3` → le message reste affiché 3 secondes

💡 **Astuce** : utilise-le sur ton bloc piège pour afficher "Aïe, recommence !" quand le joueur meurt.

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

### La plateforme qui monte et descend en boucle
Même principe que la plateforme qui tourne, mais avec la hauteur :
```lua
local part = script.Parent

while true do
    for i = 1, 10 do
        part.CFrame = part.CFrame + Vector3.new(0, 0.2, 0) -- monte petit à petit
        wait()
    end
    for i = 1, 10 do
        part.CFrame = part.CFrame - Vector3.new(0, 0.2, 0) -- redescend petit à petit
        wait()
    end
end
```

### Ajouter de la lumière ou des particules (sans code !)
Clique sur ton bloc piège dans Explorer → **+** → cherche **PointLight** (pour qu'il brille) ou **ParticleEmitter** / **Fire** (pour des étincelles ou du feu). Aucune ligne de code nécessaire, juste glisser l'objet dans ton bloc !

---

## 🏆 Défi bonus

Essaie de :
- Faire une rangée de blocs qui disparaissent chacun leur tour
- Changer la couleur du bloc piège juste avant qu'il tue (pour prévenir le joueur)
- Combiner une plateforme qui tourne ET qui monte-descend en même temps
- Ajouter un son de victoire à la fin du parcours
- Combiner les deux : un bloc qui tue ET qui disparaît

Bon courage, et amuse-toi bien à piéger tes amis ! 😈